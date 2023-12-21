"""Imports"""
from os import path
# from copy import deepcopy
import sys
from collections import deque
# import math
# import regex as re
from colorama import Fore
# import numpy as np
# from heapq import *

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False

def g_to_str(grid: list):
    """Printing grid"""
    return '\n'.join([''.join(line) for line in grid]) + "\n"

def pretty_print(grid, points):
    """Pretty printing grid"""
    print('#' * len(grid[0]))
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if (row, col) in points:
                print(Fore.RED + 'O', end='')
            else:
                print(Fore.WHITE + char, end='')
        print(Fore.WHITE + '')

def find_start_pos(grid, R, C):
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'S':
                return (r, c)

def get_neighbours(point):
    row, col = point
    return [
        (row - 1, col),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col)
        ]

def ex1(data, steps = 64):
    """Compute ex answer"""
    grid = [list(line) for line in data.split('\n')]

    if DEBUG: pretty_print(grid, [])

    R = len(grid)
    C = len(grid[0])

    start_pos = find_start_pos(grid, R, C)
    if DEBUG: print(start_pos)

    points = set()
    points.add(start_pos)

    for _ in range(steps):
        previous_points = points
        points = set()

        if DEBUG: print(previous_points)

        for point in previous_points:
            for new_point in get_neighbours(point):
                if grid[new_point[0]][new_point[1]] != '#':
                    points.add(new_point)

        if DEBUG: pretty_print(grid, points)

    return len(points)

def ex2(data, steps = 26501365):
    """Compute ex answer"""
    grid = [list(line) for line in data.split('\n')]

    # if DEBUG: pretty_print(grid, [])

    R = len(grid)
    C = len(grid[0])

    start_pos = find_start_pos(grid, R, C)
    # start_pos = (0, C-1)

    # if DEBUG: print(start_pos)

    points = set()
    points.add(start_pos)

    cards = []
    diags = []

    # for _ in range(steps):
    i = 0
    INSIDE1 = INSIDE2 = N = S = W = E = NW = NE = SW = SE = 0
    # while i < 3*R:
    while i < steps:
        i += 1
        previous_points = points
        points = set()

        # if DEBUG: print(previous_points)
        for point in previous_points:
            for new_point in get_neighbours(point):
                if grid[new_point[0] % R][new_point[1] % C] != '#' and new_point not in points:
                    points.add(new_point)

        # 632418504591521 to low
        # 632418504592008 to low
        # 632424756890765 to high

        j = 1 + i // R

        if i < R:
            INSIDE1 = len(list(filter(lambda p: 0 <= p[0] < R and 0 <= p[1] < C, points)))
        if i == R:
            INSIDE2 = len(list(filter(lambda p: 0 <= p[0] < R and 0 <= p[1] < C, points)))
        if i < int(1.5*R):
            N = len(list(filter(lambda p: p[0] < 0, points)))
            S = len(list(filter(lambda p: p[0] >= R, points)))
            W = len(list(filter(lambda p: p[1] < 0, points)))
            E = len(list(filter(lambda p: p[1] >= C, points)))
            cards.append((N, S, W, E))
        else:
            N, S, W, E = cards[(i - R//2) % R + R//2]
        if i < 2.5 *R:
            NW = len(list(filter(lambda p: p[0] < 0 and p[1] < 0, points)))
            NE = len(list(filter(lambda p: p[0] < 0 and p[1] >= C, points)))
            SW = len(list(filter(lambda p: p[0] >= R and p[1] < 0, points)))
            SE = len(list(filter(lambda p: p[0] >= R and p[1] >= C, points)))
            diags.append((NW, NE, SW, SE))
        else:
            NW, NE, SW, SE = diags[i % R]

        # if DEBUG: pretty_print(grid, points)
        # total = INSIDE1*(j**2) + INSIDE2*((j-1)**2) + N+S+W+E + (j-1)*(NW+NE+SW+SE)
        # if DEBUG: print(i, f'score: {len(points)} nb de demi carré en diag: {j-1}', (INSIDE1, INSIDE2), (N, S, W, E), (NW, NE, SW, SE), total, total - len(points))
        # assert total == len(points), f"Le total calculé {total} devrait correspondre au total réel {len(points)}"
        # print(i, f'score: {len(points)}   below {R * (1-j)} or above {-1 + j * R}, nb de demi carré en diag: {j-1}', (INSIDE1, INSIDE2), (N, S, W, E), (NW, NE, SW, SE))

        if i == steps:
            return total
        # elif i > 0:
        # N, S, W, E, NW, NE, SW, SE = values[i % R - 1]
        total = INSIDE1*(j-2)**2 + INSIDE2*(j-1)**2 + N+S+W+E + (j-1)*(NW+NE+SW+SE)
        # print(i, f'score: {len(points)}   below {R * (1-j)} or above {-1 + j * R}, nb de demi carré en diag: {((j-2)}', (INSIDE, N, S, W, E, NW, NE, SW, SE))
        if DEBUG: print(i, f'score: {len(points)} nb de demi carré en diag: {j-1}', (INSIDE1, INSIDE2), (N, S, W, E), (NW, NE, SW, SE), total, total - len(points))

    j = 1 + steps // R

    total = INSIDE1*(j**2) + INSIDE2*((j-1)**2) + N+S+W+E + (j-1)*(NW+NE+SW+SE)
    print(total)
    return total

assert ex1(load("sample.txt"), 6) == 16
print(f'ex1 : {ex1(load("input.txt"))}')

DEBUG = True
print(f'ex2 : {ex2((load("input.txt")))}')
assert ex2(load("sample.txt"), 6) == 16
assert ex2(load("sample.txt"), 10) == 50
assert ex2(load("sample.txt"), 50) == 1594
assert ex2(load("sample.txt"), 100) == 6536
assert ex2(load("sample.txt"), 500) == 167004
assert ex2(load("sample.txt"), 1000) == 668697
assert ex2(load("sample.txt"), 5000) == 16733044

sys.exit()
