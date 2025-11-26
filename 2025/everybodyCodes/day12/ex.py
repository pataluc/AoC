from os import path
import sys
from collections import deque

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

# Custo starts here
def load_data(data: str) -> tuple:
    """Loads data as a tuple"""
    return [list(map(int, line)) for line in data.split('\n')]

def chain_reaction(barrels: list, destroyed: set) -> int:
    R = len(barrels)
    C = len(barrels[0])

    q = deque(destroyed)
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0,-1)]:
            if 0 <= r + dr < R and 0 <= c + dc < C and barrels[r][c] >= barrels[r + dr][c + dc] \
                and (r+dr, c+dc) not in destroyed:
                q.append((r+dr, c+dc))
                destroyed.add((r+dr, c+dc))
    return destroyed

def part1(barrels: list) -> int:

    result = len(chain_reaction(barrels, {(0, 0)}))
    return result

assert part1(load_data(load('sample1'))) == 16
print("Part 1: ", part1(load_data(load('notes1'))))

def part2(barrels: list) -> int:
    R = len(barrels)
    C = len(barrels[0])

    result = len(chain_reaction(barrels, {(0, 0), (R-1, C-1)}))
    return result

    # result = double_chain_reaction(barrels)
    # return result

assert part2(load_data(load('sample2'))) == 58
print("Part 2: ", part2(load_data(load('notes2'))))

def part3(barrels: list) -> int:
    R = len(barrels)
    C = len(barrels[0])

    result = 0

    maxd = 0
    maxv = None
    for r in range(R):
        for c in range(C):
            destroyed = chain_reaction(barrels, {(r, c)})
            if len(destroyed) > maxd:
                maxd = len(destroyed)
                maxv = destroyed
    result = maxv

    maxd2 = 0
    maxv2 = None
    for r in range(R):
        for c in range(C):
            if (r, c) not in maxv:
                newv = maxv.copy()
                newv.add((r, c))
                destroyed = chain_reaction(barrels, newv)
                if len(destroyed) > maxd2:
                    maxd2 = len(destroyed)
                    maxv2 = destroyed

    maxd3 = 0
    maxv3 = None
    for r in range(R):
        for c in range(C):
            if (r, c) not in maxv2:
                newv = maxv2.copy()
                newv.add((r, c))
                destroyed = chain_reaction(barrels, newv)
                if len(destroyed) > maxd3:
                    maxd3 = len(destroyed)
                    maxv3 = destroyed

    return len(maxv3)


assert part3(load_data(load('sample3-1'))) == 14
assert part3(load_data(load('sample3-2'))) == 136
print("Part 3: ", part3(load_data(load('notes3'))))
