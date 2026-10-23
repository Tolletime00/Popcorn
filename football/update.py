#!/usr/bin/env python3
"""Builds football/data/data.json for the Football app.

Schedule, lines and scores come from nflverse (games.csv), with ESPN's scoreboard laid over it for
live scores, final status and the latest spreads. EPA per play comes straight from the nflverse
play-by-play data, the same data rbsdm.com is built on: offense and defense, all plays, dropbacks
and rushes, regular season only. The same play-by-play feeds a DVOA-style rating (dvoa_calc.py):
our own calculation built the way FTN describes DVOA, not FTN's numbers. Team logos are fetched
once from ESPN.

Runs on GitHub Actions on a schedule; writes only when something changed. Standard library only.
"""
import csv, gzip, io, json, os, sys, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dvoa_calc
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data', 'data.json')
LOGOS = os.path.join(HERE, 'logos')
SEASON = int(os.environ.get('SEASON') or (datetime.now(timezone.utc).year if datetime.now(timezone.utc).month >= 3 else datetime.now(timezone.utc).year - 1))
GAMES_URL = 'https://github.com/nflverse/nflverse-data/releases/download/schedules/games.csv'
PBP_URL = f'https://github.com/nflverse/nflverse-data/releases/download/pbp/play_by_play_{SEASON}.csv.gz'
ESPN_URL = 'https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?week={week}&seasontype=2&dates={season}'
LOGO_URL = 'https://a.espncdn.com/combiner/i?img=/i/teamlogos/nfl/500/{abbr}.png&w=120&h=120'
ESPN_TO_NFLVERSE = {'LAR': 'LA', 'WSH': 'WAS'}
NFLVERSE_TO_ESPN = {v: k for k, v in ESPN_TO_NFLVERSE.items()}
TEAMS = ['ARI', 'ATL', 'BAL', 'BUF', 'CAR', 'CHI', 'CIN', 'CLE', 'DAL', 'DEN', 'DET', 'GB', 'HOU', 'IND', 'JAX', 'KC', 'LA', 'LAC', 'LV', 'MIA', 'MIN', 'NE', 'NO', 'NYG', 'NYJ', 'PHI', 'PIT', 'SEA', 'SF', 'TB', 'TEN', 'WAS']
ET = ZoneInfo('America/New_York')


def fetch(url, timeout=120):
    req = urllib.request.Request(url, headers={'User-Agent': 'football-app-updater (github pages)'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def num(v):
    try:
        return float(v) if v not in (None, '', 'NA') else None
    except ValueError:
        return None


def schedule():
    """The season's regular-season games from nflverse, keyed by (week, away, home)."""
    text = fetch(GAMES_URL).decode('utf-8')
    games = {}
    for r in csv.DictReader(io.StringIO(text)):
        if r['season'] != str(SEASON) or r['game_type'] != 'REG':
            continue
        try:
            kick = datetime.strptime(f"{r['gameday']} {r['gametime'] or '13:00'}", '%Y-%m-%d %H:%M').replace(tzinfo=ET).astimezone(timezone.utc)
        except ValueError:
            kick = datetime.strptime(r['gameday'], '%Y-%m-%d').replace(hour=17, tzinfo=ET).astimezone(timezone.utc)
        away, home = r['away_team'], r['home_team']
        a, h = num(r['away_score']), num(r['home_score'])
        spread = num(r['spread_line'])   # positive: the home team is favored by that much
        games[(int(r['week']), away, home)] = {
            'id': r['game_id'], 'week': int(r['week']), 'kickoff': kick.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'away': away, 'home': home, 'awayScore': int(a) if a is not None else None, 'homeScore': int(h) if h is not None else None,
            'status': 'post' if a is not None and h is not None else 'pre', 'neutral': r['location'] == 'Neutral',
            'spread': spread,   # the away team's spread: +3 means the away team gets three points
        }
    return games


def parse_details(details, away, home):
    """ESPN's 'CHI -3' into the away team's spread; None if it cannot be read."""
    if not details:
        return None
    d = details.strip().upper()
    if d in ('EVEN', 'PK', 'PICK', "PICK 'EM"):
        return 0.0
    parts = d.split()
    if len(parts) != 2:
        return None
    team = ESPN_TO_NFLVERSE.get(parts[0], parts[0])
    n = num(parts[1])
    if n is None:
        return None
    if team == away:
        return n
    if team == home:
        return -n
    return None


def espn_overlay(games):
    """Live scores, finals, kickoff times and the latest spreads from ESPN, where they match a game."""
    hits = 0
    for week in range(1, 19):
        try:
            d = json.loads(fetch(ESPN_URL.format(week=week, season=SEASON), timeout=40))
        except Exception as e:   # ESPN is a bonus; the nflverse data stands on its own
            print(f'espn week {week}: {e}', file=sys.stderr)
            continue
        for ev in d.get('events', []):
            try:
                comp = ev['competitions'][0]
                side = {c['homeAway']: c for c in comp['competitors']}
                away = ESPN_TO_NFLVERSE.get(side['away']['team']['abbreviation'], side['away']['team']['abbreviation'])
                home = ESPN_TO_NFLVERSE.get(side['home']['team']['abbreviation'], side['home']['team']['abbreviation'])
                g = games.get((week, away, home))
                if not g:
                    continue
                st = comp.get('status', {}).get('type', {})
                state = st.get('state')
                if state in ('pre', 'in', 'post'):
                    g['status'] = state
                if state in ('in', 'post'):
                    g['awayScore'] = int(side['away'].get('score') or 0)
                    g['homeScore'] = int(side['home'].get('score') or 0)
                if state == 'in':
                    g['detail'] = st.get('shortDetail') or st.get('detail') or ''
                if ev.get('date'):
                    g['kickoff'] = datetime.strptime(ev['date'], '%Y-%m-%dT%H:%MZ').strftime('%Y-%m-%dT%H:%M:%SZ')
                if comp.get('neutralSite') is not None:
                    g['neutral'] = bool(comp['neutralSite'])
                odds = comp.get('odds') or []
                if odds and state != 'post':
                    s = parse_details(odds[0].get('details'), away, home)
                    if s is not None:
                        g['spread'] = s
                hits += 1
            except Exception as e:
                print(f'espn event: {e}', file=sys.stderr)
    return hits


def epa():
    """EPA per play for every team, offense and defense, from the play-by-play; the DVOA-style plays too."""
    raw = gzip.decompress(fetch(PBP_URL, timeout=300)).decode('utf-8')
    acc = {t: {'off': [[0.0, 0], [0.0, 0], [0.0, 0]], 'def': [[0.0, 0], [0.0, 0], [0.0, 0]]} for t in TEAMS}
    through = 0
    plays = []
    for r in csv.DictReader(io.StringIO(raw)):
        if r.get('season_type') != 'REG':
            continue
        p = dvoa_calc.play_from_row(r)
        if p:
            plays.append(p)
        e = num(r.get('epa'))
        if e is None:
            continue
        is_pass, is_rush = r.get('pass') == '1', r.get('rush') == '1'
        if not (is_pass or is_rush):
            continue
        pos, de = r.get('posteam'), r.get('defteam')
        if pos not in acc or de not in acc:
            continue
        through = max(through, int(r.get('week') or 0))
        for side, team in (('off', pos), ('def', de)):
            a = acc[team][side]
            a[0][0] += e; a[0][1] += 1
            if is_pass: a[1][0] += e; a[1][1] += 1
            if is_rush: a[2][0] += e; a[2][1] += 1
    out = {}
    for t, s in acc.items():
        out[t] = {side: [round(x[0] / x[1], 3) if x[1] else None for x in s[side]] for side in ('off', 'def')}
        out[t]['plays'] = s['off'][0][1]
    return out, through, dvoa_calc.compute(plays, TEAMS)


def logos():
    os.makedirs(LOGOS, exist_ok=True)
    for t in TEAMS:
        path = os.path.join(LOGOS, f'{t}.png')
        if os.path.exists(path) and os.path.getsize(path) > 500:
            continue
        try:
            with open(path, 'wb') as f:
                f.write(fetch(LOGO_URL.format(abbr=NFLVERSE_TO_ESPN.get(t, t).lower()), timeout=40))
        except Exception as e:
            print(f'logo {t}: {e}', file=sys.stderr)


def main():
    games = schedule()
    print(f'{len(games)} games for {SEASON}')
    print(f'espn matched {espn_overlay(games)} games')
    teams, through, dvoa = epa()
    print(f'epa and dvoa-style through week {through}')
    logos()
    body = {
        'app': 'Football', 'season': SEASON, 'throughWeek': through,
        'games': sorted(games.values(), key=lambda g: (g['week'], g['kickoff'], g['away'])),
        'epa': teams,
        'dvoa': dvoa,
        'dvoaNote': "DVOA-style: our own calculation from nflverse play-by-play, built the way FTN describes DVOA. Not FTN's numbers.",
    }
    old = None
    if os.path.exists(DATA):
        try:
            with open(DATA, encoding='utf-8') as f:
                old = json.load(f)
        except Exception:
            old = None
    if old and {k: v for k, v in old.items() if k != 'updated'} == body:
        print('no change')
        return
    body['updated'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    os.makedirs(os.path.dirname(DATA), exist_ok=True)
    with open(DATA, 'w', encoding='utf-8') as f:
        json.dump(body, f, separators=(',', ':'), ensure_ascii=False)
    print(f'wrote {DATA} ({os.path.getsize(DATA)} bytes)')


if __name__ == '__main__':
    main()
