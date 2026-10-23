"""A DVOA-style rating from nflverse play-by-play rows, built the way FTN describes DVOA.

Success points per play, compared with the league average for the situation, adjusted for the
opponent a few times over, then offense, defense and the pass/rush splits as percentages.
It is our own calculation, not FTN's DVOA: their exact curves and tables are not public, but on
the 2024 and 2025 seasons this lands within about three points of their published numbers for
the typical team (correlation 0.97 for offense, 0.92-0.95 for defense). Standard library only.
"""
from collections import defaultdict

THRESH = {1: 0.45, 2: 0.60, 3: 1.0, 4: 1.0}
PARTIAL_EXP = 2.75          # 8 yards on 3rd-and-10 -> 0.54 points, FTN's published example
LOSS_PENALTY = -1.0         # a loss of 3+ yards
INT_BASE = -4.5
TD_BONUS = 1.0
FUMBLE_PER_LOST = -4.5      # charged by how often that kind of fumble is lost, whoever recovered it
GARBAGE_WEIGHT = 0.5
SHRINK_K = 40               # plays of prior weight when a situation bucket is thin
PENALTIES = {'Defensive Pass Interference', 'Intentional Grounding', 'False Start', 'Delay of Game'}
FULL_ADJUST_WEEK = 10       # opponent adjustments phase in over the first ten weeks


def _f(v, d=0.0):
    try:
        return float(v) if v not in (None, '', 'NA') else d
    except ValueError:
        return d


def play_from_row(r):
    """One play's worth of fields from a nflverse row, or None if it is not a play DVOA counts."""
    if r.get('season_type') != 'REG' or not r.get('posteam') or not r.get('defteam') or r.get('down') in (None, '', 'NA'):
        return None
    if r.get('play_deleted') == '1' or r.get('two_point_attempt') == '1' or r.get('qb_kneel') == '1' or r.get('qb_spike') == '1':
        return None
    pt = r.get('play_type')
    p = {'pos': r['posteam'], 'def': r['defteam'], 'week': int(_f(r.get('week'))), 'down': int(_f(r.get('down'))),
         'togo': _f(r.get('ydstogo'), 10), 'yl': _f(r.get('yardline_100'), 50), 'qtr': int(_f(r.get('qtr'), 1)),
         'diff': abs(_f(r.get('score_differential'))), 'int': 0, 'fum': 0, 'lost': 0, 'td': 0, 'sack': 0, 'aborted': 0, 'air': 0.0, 'ret': 0.0}
    if pt in ('pass', 'run'):
        p['kind'] = 'pass' if r.get('pass') == '1' else 'rush' if r.get('rush') == '1' else 'other'
        if r.get('aborted_play') == '1':
            p['kind'] = 'other'; p['aborted'] = 1
        p['yards'] = _f(r.get('yards_gained'))
        p['fd'] = 1 if (r.get('first_down') == '1' or r.get('touchdown') == '1') else 0
        p['int'] = 1 if r.get('interception') == '1' else 0
        p['fum'] = 1 if r.get('fumble') == '1' else 0
        p['lost'] = 1 if r.get('fumble_lost') == '1' else 0
        p['td'] = 1 if r.get('touchdown') == '1' else 0
        p['sack'] = 1 if r.get('sack') == '1' else 0
        p['air'] = _f(r.get('air_yards')); p['ret'] = _f(r.get('return_yards'))
        return p
    if pt == 'no_play' and r.get('penalty_type') in PENALTIES:
        kind = r['penalty_type']
        p['kind'] = 'pass' if kind in ('Defensive Pass Interference', 'Intentional Grounding') else 'other'
        on_offense = r.get('penalty_team') == r['posteam']
        p['yards'] = -_f(r.get('penalty_yards'), 5) if on_offense else _f(r.get('penalty_yards'))
        p['fd'] = 1 if kind == 'Defensive Pass Interference' else 0
        return p
    return None


def _interp(x, xs, ys):
    if x <= xs[0]: return ys[0]
    for i in range(1, len(xs)):
        if x <= xs[i]:
            x0, x1, y0, y1 = xs[i - 1], xs[i], ys[i - 1], ys[i]
            return y0 if x1 == x0 else y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return ys[-1]


def success_points(p, fumble_rate):
    togo = max(1.0, p['togo']); yards = p['yards']; need = THRESH[p['down']] * togo
    if p['int']:
        pts = INT_BASE + min(1.5, max(0.0, (p['air'] - 10) / 20 * 1.5)) - min(1.5, max(0.0, p['ret'] / 30 * 1.5))
        if p['td']: pts -= 1.0
        return pts
    if yards <= -3:
        pts = LOSS_PENALTY
    elif yards >= need:
        pts = 1.0
        if p['fd']:   # the big-play ramp: 3 points at 10 yards, 4 at 20, 5 at 40, rising from 1 at the sticks
            start = min(togo, 10.0)
            xs = ([start] if start < 10 else []) + [10.0, 20.0, 40.0]; ys = ([1.0] if start < 10 else []) + [3.0, 4.0, 5.0]
            pts = _interp(yards, xs, ys)
    else:
        pts = max(0.0, yards / need) ** PARTIAL_EXP
    if p['td'] and not p['fum']:
        pts += TD_BONUS
    if p['fum']:
        cat = 'aborted' if p['aborted'] else 'sack' if p['sack'] else ('pass' if p['kind'] == 'pass' else 'rush')
        pts += max(-3.0, min(-1.3, FUMBLE_PER_LOST * fumble_rate.get(cat, 0.5)))
    return pts


def _dist_bucket(togo):
    return 0 if togo <= 1 else 1 if togo <= 3 else 2 if togo <= 6 else 3 if togo <= 10 else 4 if togo <= 15 else 5


def _zone(yl):
    return 0 if yl >= 90 else 1 if yl >= 70 else 2 if yl >= 50 else 3 if yl >= 30 else 4 if yl >= 20 else 5 if yl >= 10 else 6


def compute(plays, teams, iterations=12, damping=0.6):
    """plays: the list from play_from_row. Returns {team: {off, def, offPass, offRush, defPass, defRush, total}} in percent."""
    plays = [p for p in plays if p['pos'] in teams and p['def'] in teams]
    if not plays:
        return {}
    # how often each kind of fumble is lost, from the data itself
    fr = defaultdict(lambda: [0, 0])
    for p in plays:
        if p['fum']:
            cat = 'aborted' if p['aborted'] else 'sack' if p['sack'] else ('pass' if p['kind'] == 'pass' else 'rush')
            fr[cat][0] += p['lost']; fr[cat][1] += 1
    fumble_rate = {k: v[0] / v[1] for k, v in fr.items() if v[1]}
    through = max(p['week'] for p in plays)
    for p in plays:
        p['pts'] = success_points(p, fumble_rate)
        p['w'] = GARBAGE_WEIGHT if ((p['qtr'] >= 4 and p['diff'] > 21) or (p['qtr'] >= 3 and p['diff'] > 28)) else 1.0
        p['db'] = _dist_bucket(p['togo']); p['zn'] = _zone(p['yl'])
    # the baseline: the league average for the situation, shrunk toward the down-and-distance average when thin
    dd = defaultdict(lambda: [0.0, 0.0]); g = defaultdict(lambda: [0.0, 0.0])
    for p in plays:
        dd[(p['down'], p['db'])][0] += p['pts'] * p['w']; dd[(p['down'], p['db'])][1] += p['w']
        g[(p['down'], p['db'], p['zn'])][0] += p['pts'] * p['w']; g[(p['down'], p['db'], p['zn'])][1] += p['w']
    for p in plays:
        prior = dd[(p['down'], p['db'])]; prior_m = prior[0] / prior[1]
        s, n = g[(p['down'], p['db'], p['zn'])]
        p['base'] = (s + SHRINK_K * prior_m) / (n + SHRINK_K)
    kinds = ('pass', 'rush', 'other', 'all')
    off = {t: {k: 0.0 for k in kinds} for t in teams}; de = {t: {k: 0.0 for k in kinds} for t in teams}
    phase = min(1.0, through / FULL_ADJUST_WEEK)
    for it in range(iterations):
        num_o = defaultdict(float); den_o = defaultdict(float); num_d = defaultdict(float); den_d = defaultdict(float)
        for p in plays:
            k = p['kind'] if p['kind'] != 'other' else 'all'
            exp_o = p['base'] * (1 + phase * de[p['def']][k]); exp_d = p['base'] * (1 + phase * off[p['pos']][k])
            for key in (p['kind'], 'all'):
                num_o[(p['pos'], key)] += (p['pts'] - exp_o) * p['w']; den_o[(p['pos'], key)] += p['base'] * p['w']
                num_d[(p['def'], key)] += (p['pts'] - exp_d) * p['w']; den_d[(p['def'], key)] += p['base'] * p['w']
        new_o = {t: {k: (num_o[(t, k)] / den_o[(t, k)] if den_o[(t, k)] else 0.0) for k in kinds} for t in teams}
        new_d = {t: {k: (num_d[(t, k)] / den_d[(t, k)] if den_d[(t, k)] else 0.0) for k in kinds} for t in teams}
        # centre the league at 0% on the overall numbers; the splits keep their natural offsets
        mo = sum(new_o[t]['all'] for t in teams) / len(teams); md = sum(new_d[t]['all'] for t in teams) / len(teams)
        for t in teams:
            for k in kinds:
                to, td_ = new_o[t][k] - mo, new_d[t][k] - md
                off[t][k] = off[t][k] + damping * (to - off[t][k]) if it else to
                de[t][k] = de[t][k] + damping * (td_ - de[t][k]) if it else td_
    out = {}
    for t in teams:
        o, d = off[t], de[t]
        out[t] = {'off': round(o['all'] * 100, 1), 'def': round(d['all'] * 100, 1), 'offPass': round(o['pass'] * 100, 1), 'offRush': round(o['rush'] * 100, 1),
                  'defPass': round(d['pass'] * 100, 1), 'defRush': round(d['rush'] * 100, 1), 'total': round((o['all'] - d['all']) * 100, 1)}
    return out
