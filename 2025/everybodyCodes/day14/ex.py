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
    return [list(line) for line in data.split('\n')]

def change_floor(tiles: list) -> list:
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    R = len(tiles)
    C = len(tiles[0])

    make_active = []
    make_inactive = []

    for r in range(R):
        for c in range(C):
            if tiles[r][c] == '#' and (sum(
                1 for dr, dc in directions
                if 0 <= r + dr < R and 0 <= c + dc < C and tiles[r + dr][c + dc] == '#'
            ) % 2) == 0:
                make_inactive.append((r, c))
            elif tiles[r][c] == '.' and (sum(
                1 for dr, dc in directions
                if 0 <= r + dr < R and 0 <= c + dc < C and tiles[r + dr][c + dc] == '#'
            ) % 2) == 0:
                make_active.append((r, c))

    # print("To activate: ", make_active)
    # print("To inactivate: ", make_inactive)

    for r, c in make_active:
        tiles[r][c] = '#'
    for r, c in make_inactive:
        tiles[r][c] = '.'

    return tiles


def part1(tiles: list, times: int = 10) -> int:
    R = len(tiles)
    C = len(tiles[0])

    result = 0

    for i in range(times):
        tiles = change_floor(tiles)
        print("Round ", i+1)
        # print('\n'.join(''.join(row) for row in tiles))
        result += sum(row.count('#') for row in tiles)

    return result

assert part1(load_data(load('sample1'))) == 200
print("Part 1: ", part1(load_data(load('notes1'))))


print("Part 2: ", part1(load_data(load('notes2')), 2025))

exit()
print("Part 3: ", part2(load_data2(load('notes3')), 202520252025))
