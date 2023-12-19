"""Imports"""
from os import path
import sys
# from collections import Counter
# import math
# import regex as re
# import numpy as np

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

def pretty_print(grid):
    """Pretty printing grid"""
    for line in grid:
        element: set
        for element in line:
            if len(element) == 0:
                print('.', end='')
            elif len(element) == 1:
                print(list(element)[0], end='')
            else:
                print(len(element), end='')
        print('')

DIR_CAR = {
    (1, 0):  'v',
    (-1, 0): '^',
    (0, 1):  '>',
    (0, -1): '<'
}

def energizing(GRID, visited, pos: tuple, dir_: tuple):
    """Energy propagation"""
    ROWS = len(GRID)
    COLS = len(GRID[0])

    if 0 <= pos[0] < ROWS \
        and 0 <= pos[1] < COLS:
        visited[pos[0]][pos[1]].add(DIR_CAR[dir_])

    # if DEBUG: pretty_print(visited)
    steps = 1

    nextpos = (pos[0] + steps * dir_[0], pos[1] + steps * dir_[1])
    if DEBUG:
        print("pos:", nextpos, "dir:", dir_, "char: ",\
              DIR_CAR[dir_], '  grid:', GRID[nextpos[0]][nextpos[1]])
    if DEBUG:
        pretty_print(visited)

    while 0 <= nextpos[0] < ROWS \
        and 0 <= nextpos[1] < COLS \
        and (GRID[nextpos[0]][nextpos[1]] == '.' \
             or (GRID[nextpos[0]][nextpos[1]] == '-' \
             and dir_[0] == 0) \
             or (GRID[nextpos[0]][nextpos[1]] == '|' \
             and dir_[1] == 0)):

        visited[nextpos[0]][nextpos[1]].add(DIR_CAR[dir_])

        # if DEBUG: print(nextpos)
        steps += 1
        nextpos = (pos[0] + steps * dir_[0], pos[1] + steps * dir_[1])
    # if DEBUG: print(visited)

    if 0 <= nextpos[0] < ROWS \
        and 0 <= nextpos[1] < COLS:
        # if DEBUG: print(G[nextpos[0]][nextpos[1]])
        if GRID[nextpos[0]][nextpos[1]] == '-':
            if DEBUG:
                print('splitting <->')
            if '>' not in visited[nextpos[0]][nextpos[1]]:
                energizing(GRID, visited, nextpos, (0, 1))
            if '<' not in visited[nextpos[0]][nextpos[1]]:
                energizing(GRID, visited, nextpos, (0, -1))
        elif GRID[nextpos[0]][nextpos[1]] == '|':
            if DEBUG:
                print('splitting ^-v')
            if 'v' not in visited[nextpos[0]][nextpos[1]]:
                energizing(GRID, visited, nextpos, (1, 0))
            if '^' not in visited[nextpos[0]][nextpos[1]]:
                energizing(GRID, visited, nextpos, (-1, 0))
        elif GRID[nextpos[0]][nextpos[1]] == '\\':
            newdir = (dir_[1], dir_[0])
            if DEBUG:
                print(f'Going from {DIR_CAR[dir_]} to {DIR_CAR[newdir]}')
            if DIR_CAR[newdir] not in visited[nextpos[0]][nextpos[1]]:
                energizing(GRID, visited, nextpos, newdir)
        elif GRID[nextpos[0]][nextpos[1]] == '/':
            newdir = (-1 * dir_[1], -1 * dir_[0])
            if DEBUG:
                print(f'Going from {DIR_CAR[dir_]} to {DIR_CAR[newdir]}')
            if DIR_CAR[newdir] not in visited[nextpos[0]][nextpos[1]]:
                energizing(GRID, visited, nextpos, newdir)


def ex1(data, init_pos = (0, -1), dir_ = (0, 1)):
    """Compute ex answer"""
    GRID = [list(row) for row in data.split('\n')]
    ROWS = len(GRID)
    COLS = len(GRID[0])

    # if DEBUG: print(g_to_str(G))

    visited = [[set() for _ in range(COLS)] for _ in range(ROWS)]
    energizing(GRID, visited, init_pos, dir_)

    if DEBUG:
        pretty_print(visited)

    result = 0
    for step_i, line in enumerate(visited):
        for step_j, node in enumerate(line):
            if len(node) > 0:
                result += 1
                if DEBUG:
                    print((step_i,step_j))

    if DEBUG:
        print(result)

    return result

def ex2(data):
    """Compute ex answer"""
    GRID = [list(row) for row in data.split('\n')]
    ROWS = len(GRID)
    COLS = len(GRID[0])

    result = 0
    # start horiz
    for row in range(ROWS):
        result = max(result, ex1(data, (row, -1), (0, 1)))
        result = max(result, ex1(data, (row, ROWS), (0, -1)))

    # start vert
    for col in range(COLS):
        result = max(result, ex1(data, (-1, col), (1, 0)))
        result = max(result, ex1(data, (COLS, col), (-1, 0)))

    if DEBUG:
        print(result)
    return result


assert ex1(load("sample.txt")) == 46
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 51
print(f'ex2 : {ex2((load("input.txt")))}')

DEBUG = True
sys.exit()
