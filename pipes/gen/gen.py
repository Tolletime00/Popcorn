#!/usr/bin/env python3
"""Makes Numberlink ("Flow") puzzles with exactly one solution, and rates how hard they are.

A puzzle is a square grid carved into winding paths; the dots are the ends of the paths. A random
carve is one solution; a solver then counts solutions (to two) and the puzzle is kept only if the
carve is the only one. Difficulty is how much a plain solver has to search.

Usage: python3 gen.py <out.json>
"""
import json, random, sys, time
from collections import deque

random.seed(20261024)
DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
STRAIGHT = 0.85


# ----------------------------------------------------------------- carving paths
def carve(n, min_len, max_len, tries=200):
    """Split the n×n grid into paths of min_len..max_len cells, Warnsdorff-style so corners don't strand."""
    for _ in range(tries):
        grid = [[-1] * n for _ in range(n)]
        paths = []
        cells = [(r, c) for r in range(n) for c in range(n)]
        ok = True
        while True:
            empty = [rc for rc in cells if grid[rc[0]][rc[1]] < 0]
            if not empty:
                break
            # start where the board is tightest, so no cell gets stranded
            def freedom(rc):
                return sum(1 for dr, dc in DIRS if 0 <= rc[0] + dr < n and 0 <= rc[1] + dc < n and grid[rc[0] + dr][rc[1] + dc] < 0)
            empty.sort(key=lambda rc: (freedom(rc), random.random()))
            start = empty[0]
            pid = len(paths); path = [start]; grid[start[0]][start[1]] = pid
            target_len = random.randint(min_len, max_len)
            while len(path) < target_len:
                r, c = path[-1]
                nxt = [(r + dr, c + dc) for dr, dc in DIRS if 0 <= r + dr < n and 0 <= c + dc < n and grid[r + dr][c + dc] < 0]
                if not nxt:
                    break
                nxt.sort(key=lambda rc: (freedom(rc), random.random()))
                # keep going straight when we can (taut pipes make for unique puzzles), else the tightest cell
                straight = None
                if len(path) >= 2:
                    pr, pc = path[-2]; sr, sc = r + (r - pr), c + (c - pc)
                    if (sr, sc) in nxt: straight = (sr, sc)
                if straight and random.random() < STRAIGHT:
                    pick = straight
                else:
                    pick = nxt[0] if random.random() < 0.75 else random.choice(nxt)
                path.append(pick); grid[pick[0]][pick[1]] = pid
            if len(path) < min_len:
                ok = False; break
            paths.append(path)
        if ok and len(paths) >= 2:
            return paths
    return None


# ----------------------------------------------------------------- solving
def solve(n, pairs, limit=2, node_cap=3_000_000, strong=True):
    """Count solutions up to `limit` for the puzzle; returns (count, nodes) or (None, nodes) if the cap hit."""
    k = len(pairs)
    grid = [[-1] * n for _ in range(n)]
    heads = []; targets = []
    for i, (r1, c1, r2, c2) in enumerate(pairs):
        grid[r1][c1] = i; grid[r2][c2] = i
        heads.append((r1, c1)); targets.append((r2, c2))
    done = [False] * k
    nodes = 0
    sols = 0

    def inb(r, c):
        return 0 <= r < n and 0 <= c < n

    def avail_count(r, c):
        # a path has to pass through an empty cell: it needs two ways in or out
        cnt = 0
        for dr, dc in DIRS:
            rr, cc = r + dr, c + dc
            if not inb(rr, cc): continue
            if grid[rr][cc] < 0: cnt += 1
            else:
                for i in range(k):
                    if not done[i] and ((rr, cc) == heads[i] or (rr, cc) == targets[i]):
                        cnt += 1; break
        return cnt

    def dead_near(*cells):
        # only cells next to what just changed can have become dead
        for r0, c0 in cells:
            for dr, dc in DIRS + [(0, 0)]:
                r, c = r0 + dr, c0 + dc
                if inb(r, c) and grid[r][c] < 0 and avail_count(r, c) < 2:
                    return True
        return False

    def reachable(i):
        # can colour i's head still get to its target through empty cells?
        hr, hc = heads[i]; tr, tc = targets[i]
        seen = {(hr, hc)}; dq = deque([(hr, hc)])
        while dq:
            r, c = dq.popleft()
            for dr, dc in DIRS:
                rr, cc = r + dr, c + dc
                if not inb(rr, cc) or (rr, cc) in seen: continue
                if (rr, cc) == (tr, tc): return True
                if grid[rr][cc] < 0:
                    seen.add((rr, cc)); dq.append((rr, cc))
        return False

    def moves(i):
        hr, hc = heads[i]; out = []
        for dr, dc in DIRS:
            rr, cc = hr + dr, hc + dc
            if not inb(rr, cc): continue
            if (rr, cc) == targets[i] or grid[rr][cc] < 0:
                out.append((rr, cc))
        return out

    def rec():
        nonlocal nodes, sols
        nodes += 1
        if nodes > node_cap:
            raise TimeoutError
        if all(done):
            if all(grid[r][c] >= 0 for r in range(n) for c in range(n)):
                sols += 1
                if sols >= limit:
                    raise StopIteration
            return
        # the colour with the fewest moves goes first
        best = None; best_m = None
        for i in range(k):
            if done[i]: continue
            m = moves(i)
            if not m: return
            if best is None or len(m) < len(best_m):
                best, best_m = i, m
        for rr, cc in best_m:
            prev = heads[best]
            if (rr, cc) == targets[best]:
                done[best] = True; heads[best] = (rr, cc)
                if not dead_near(prev, (rr, cc)) and (not strong or all(reachable(j) for j in range(k) if not done[j])):
                    rec()
                done[best] = False; heads[best] = prev
            else:
                grid[rr][cc] = best; heads[best] = (rr, cc)
                if not dead_near(prev, (rr, cc)) and (not strong or reachable(best)):
                    rec()
                grid[rr][cc] = -1; heads[best] = prev

    try:
        if any(grid[r][c] < 0 and avail_count(r, c) < 2 for r in range(n) for c in range(n)):
            return 0, 0
        rec()
    except StopIteration:
        pass
    except TimeoutError:
        return None, nodes
    return sols, nodes


def puzzle_from(paths):
    return [[p[0][0], p[0][1], p[-1][0], p[-1][1]] for p in paths]


def make(n, count, min_len, max_lens, seconds, weak_cap=60_000):
    """Unique puzzles of size n with their difficulty, as many as `seconds` allows, up to `count`."""
    out = []; seen = set(); t0 = time.time()
    while len(out) < count and time.time() - t0 < seconds:
        paths = carve(n, min_len, random.choice(max_lens))
        if not paths: continue
        pairs = puzzle_from(paths)
        key = tuple(sorted(tuple(sorted(((p[0], p[1]), (p[2], p[3])))) for p in pairs))
        if key in seen: continue
        seen.add(key)
        if any(abs(p[0] - p[2]) + abs(p[1] - p[3]) == 1 for p in pairs):   # no dots touching their partner
            continue
        sols, _ = solve(n, pairs, limit=2, node_cap=250_000, strong=True)
        if sols != 1: continue
        sols2, effort = solve(n, pairs, limit=1, node_cap=weak_cap, strong=False)   # how hard a plain search finds it
        if sols2 is None: effort = weak_cap
        turns = sum(1 for p in paths for a, b, c in zip(p, p[1:], p[2:]) if (b[0] - a[0], b[1] - a[1]) != (c[0] - b[0], c[1] - b[1]))
        out.append({'n': n, 'pairs': pairs, 'solution': [[list(rc) for rc in p] for p in paths], 'colors': len(pairs), 'effort': effort, 'turns': turns, 'longest': max(len(p) for p in paths)})
    return out


PLAN = {   # size: (how many to keep, shortest pipe, longest-pipe choices, time budget in seconds, search cap for the difficulty rating)
    4: (8, 3, [5, 6, 7], 60, 60_000), 5: (10, 3, [6, 8, 10], 90, 60_000), 6: (12, 3, [8, 10, 12], 240, 60_000),
    7: (12, 4, [10, 12, 15], 420, 150_000), 8: (8, 4, [12, 14, 16], 900, 300_000),
}

if __name__ == '__main__' and sys.argv[1] == 'pool':
    n = int(sys.argv[2]); keep, lo, his, secs, cap = PLAN[n]
    random.seed(20261024 + n)
    pool = make(n, 800, lo, his, secs, cap)
    json.dump(pool, open(sys.argv[3], 'w'))
    print(f'{n}x{n}: {len(pool)} unique puzzles', file=sys.stderr)
    sys.exit()

if __name__ == '__main__':
    levels = []
    for n in (4, 5, 6, 7, 8):
        keep = PLAN[n][0]
        pool = json.load(open(f'pool{n}.json'))
        pool.sort(key=lambda p: (p['effort'], p['turns']))
        print(f'{n}x{n}: {len(pool)} unique puzzles, effort {pool[0]["effort"]}..{pool[-1]["effort"]}', file=sys.stderr)
        if n == 4:      # from trivial to mildly tricky, across the easier half of the 4×4s
            top = int(len(pool) * 0.55)
            idx = [round(i * (top - 1) / (keep - 1)) for i in range(keep)]
            pick = [pool[i] for i in idx]
        elif n == 8:    # the hardest end of the hardest size
            pick = pool[-keep:]
        else:           # a spread from fairly easy to the hardest found
            idx = [round((0.15 + 0.85 * i / (keep - 1)) * (len(pool) - 1)) for i in range(keep)]
            pick = [pool[i] for i in idx]
        levels.extend(pick)
    for i, lv in enumerate(levels, 1):
        lv['level'] = i
    json.dump(levels, open(sys.argv[1], 'w'), separators=(',', ':'))
    print(f'{len(levels)} levels written', file=sys.stderr)
    for lv in levels:
        print(lv['level'], f"{lv['n']}x{lv['n']}", lv['colors'], 'colours', 'effort', lv['effort'], 'turns', lv['turns'], 'longest', lv['longest'], file=sys.stderr)
