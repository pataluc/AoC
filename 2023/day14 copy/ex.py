"""Imports"""
from os import path
import sys
# from collections import Counter
import math
import regex as re
# import numpy as np

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False

def g_to_str(grid: list):
    return '\n'.join([''.join(line) for line in grid]) + "\n"

def pretty_print(grid):
    for line in grid:
        e: set
        for e in line:
            if len(e) == 0:
                print('.', end='')
            elif len(e) == 1:
                print(list(e)[0], end='')
            else:
                print(len(e), end='')
        print('')

DIR_CAR = {
    (1, 0):  'v',
    (-1, 0): '^',
    (0, 1):  '>',
    (0, -1): '<'
}

def energizing(G, W, H, visited, pos: tuple, dir: tuple):
    if 0 <= pos[0] < H \
        and 0 <= pos[1] < W:
        visited[pos[0]][pos[1]].add(DIR_CAR[dir])
    
    # if DEBUG: pretty_print(visited)
    i = 1

    nextpos = (pos[0] + i * dir[0], pos[1] + i * dir[1])
    if DEBUG: print("pos:", nextpos, "dir:", dir, "char: ", DIR_CAR[dir], '  grid:', G[nextpos[0]][nextpos[1]])
    if DEBUG: pretty_print(visited)

    while 0 <= nextpos[0] < H \
        and 0 <= nextpos[1] < W \
        and (G[nextpos[0]][nextpos[1]] == '.' \
             or (G[nextpos[0]][nextpos[1]] == '-' \
             and dir[0] == 0) \
             or (G[nextpos[0]][nextpos[1]] == '|' \
             and dir[1] == 0)):
        
        visited[nextpos[0]][nextpos[1]].add(DIR_CAR[dir])

        # if DEBUG: print(nextpos)
        i += 1
        nextpos = (pos[0] + i * dir[0], pos[1] + i * dir[1])
    # if DEBUG: print(visited)
    
    if 0 <= nextpos[0] < H \
        and 0 <= nextpos[1] < W:
        # if DEBUG: print(G[nextpos[0]][nextpos[1]])
        if G[nextpos[0]][nextpos[1]] == '-':
            if DEBUG: print('splitting <->')
            if '>' not in visited[nextpos[0]][nextpos[1]]:
                energizing(G, W, H, visited, nextpos, (0, 1))
            if '<' not in visited[nextpos[0]][nextpos[1]]:
                energizing(G, W, H, visited, nextpos, (0, -1))
        elif G[nextpos[0]][nextpos[1]] == '|':
            if DEBUG: print('splitting ^-v')
            if 'v' not in visited[nextpos[0]][nextpos[1]]:
                energizing(G, W, H, visited, nextpos, (1, 0))
            if '^' not in visited[nextpos[0]][nextpos[1]]:
                energizing(G, W, H, visited, nextpos, (-1, 0))
        elif G[nextpos[0]][nextpos[1]] == '\\':
            newdir = (dir[1], dir[0])
            if DEBUG: print(f'Going from {DIR_CAR[dir]} to {DIR_CAR[newdir]}')
            if DIR_CAR[newdir] not in visited[nextpos[0]][nextpos[1]]:
                energizing(G, W, H, visited, nextpos, newdir)
        elif G[nextpos[0]][nextpos[1]] == '/':
            newdir = (-1 * dir[1], -1 * dir[0])
            if DEBUG: print(f'Going from {DIR_CAR[dir]} to {DIR_CAR[newdir]}')
            if DIR_CAR[newdir] not in visited[nextpos[0]][nextpos[1]]:
                energizing(G, W, H, visited, nextpos, newdir)


def ex1(data, init_pos = (0, -1), dir = (0, 1)):
    """Compute ex answer"""
    G = [[c for c in row] for row in data.split('\n')]
    W = len(G[0])
    H = len(G)

    # if DEBUG: print(g_to_str(G))

    visited = [[set() for _ in range(W)] for _ in range(H)]
    energizing(G, W, H, visited, init_pos, dir)

    if DEBUG: pretty_print(visited)
                
    result = 0
    for i, line in enumerate(visited):
        for j, e in enumerate(line):
            if len(e) > 0:
                result += 1
                if DEBUG: print((i,j))

    if DEBUG: print(result)

    return result

def ex2(data):
    """Compute ex answer"""
    G = [[c for c in row] for row in data.split('\n')]
    W = len(G[0])
    H = len(G)

    result = 0
    # start horiz
    for i in range(H):
        result = max(result, ex1(data, (i, -1), (0, 1)))
        result = max(result, ex1(data, (i, W), (0, -1)))
        
    # start vert
    for j in range(W):
        result = max(result, ex1(data, (-1, j), (1, 0)))
        result = max(result, ex1(data, (H, j), (-1, 0)))
    
    if DEBUG: print(result)
    return result


assert ex1(load("sample.txt")) == 46
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 51
print(f'ex2 : {ex2((load("input.txt")))}')
DEBUG = True
sys.exit()

