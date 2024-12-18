"""Imports"""
from __future__ import annotations
from os import path, system
# from copy import deepcopy
import sys
from collections import defaultdict
# import math
import re
# from colorama import Fore
import numpy as np
# from heapq import *
# import networkx as nx
# import functools
# from sympy import solve, symbols, Eq

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> tuple:
    """Loads data as a tuple"""

    robots_map, moves = data.split('\n\n')
    robots_map = list(map(list, robots_map.split('\n')))
    moves = list(moves.replace('\n', ''))

    return robots_map, moves, len(robots_map), len(robots_map[0])

DEBUG = False

directions = {
    "v": np.array(( 1,  0)),
    "^": np.array((-1,  0)),
    ">": np.array(( 0,  1)),
    "<": np.array(( 0, -1)),
}

def move_robot(grid: list, H: int, W: int, robot: np.array, move: np.array) -> np.array:
    new_pos = robot + move
    rh, rw = robot
    nh, nw = new_pos
    mh, mw = new_pos
    if 0 < nh < H - 1 and 0 < nw < W - 1:
        if grid[nh][nw] == '.':
            grid[rh][rw] = '.'
            grid[nh][nw] = '@'
            return np.array((nh, nw))
        elif grid[nh][nw] == 'O':
            while grid[mh][mw] == 'O':
                new_pos += move
                mh, mw = new_pos
            if grid[mh][mw] == '.':
                grid[mh][mw] = 'O'
                grid[rh][rw] = '.'
                grid[nh][nw] = '@'
                return robot + move

    return robot

def ex1(data: str) -> int:
    """Solve ex1"""

    grid, moves, H, W = load_data(data)
    h, w = (1, 1)
    while grid[h][w] != '@':
        w += 1
        if w == W:
            w = 1
            h += 1

    robot = np.array((h, w))

    for move in moves:
        robot = move_robot(grid, H, W, robot, directions[move])

    ans = 0
    for h in range(H):
        for w in range(W):
            if grid[h][w] == 'O':
                ans += 100 * h + w


    return ans

def move_robot2(grid: list, H: int, W: int, robot: np.array, move: np.array) -> np.array:
    new_pos = robot + move
    rh, rw = robot
    nh, nw = new_pos
    mh, mw = new_pos
    if 0 < nh < H - 1 and 0 < nw < W - 1:
        if grid[nh][nw] == '.':
            grid[rh][rw] = '.'
            grid[nh][nw] = '@'
            return np.array((nh, nw))
        elif grid[nh][nw] in '[]':
            if move[0] == 0: # Déplacement horiz
                while grid[mh][mw] in '[]':
                    new_pos += move
                    mh, mw = new_pos
                if grid[mh][mw] == '.':
                    # on revient vers la position du robot en décalant
                    nh, nw = mh, mw
                    while (nh, nw) != (rh, rw):
                        ph, pw = new_pos
                        new_pos -= move
                        nh, nw = new_pos
                        grid[ph][pw] = grid[nh][nw]
                    grid[rh][rw] = '.'

                    return np.array(robot + move)
            else: # Déplacement vertical
                points_to_move = [{(nh, nw), (nh, nw + 1 if grid[nh][nw] == '[' else nw - 1)}]
                floor = nh
                ws = [p[1] for p in points_to_move[-1]]
                f = grid[nh + move[1]][min(ws):max(ws)+1]
                # print(grid[nh + move[1]], ws, f)

                while ('[' in f or ']' in f) and not '#' in f:
                    next_floor = set()
                    for ph, pw in points_to_move[-1]:
                        if grid[ph+move[0]][pw] == '[':
                            next_floor.add((ph+move[0], pw))
                            next_floor.add((ph+move[0], pw + 1))
                        elif grid[ph+move[0]][pw] == ']':
                            next_floor.add((ph+move[0], pw - 1))
                            next_floor.add((ph+move[0], pw))
                        elif grid[ph+move[0]][pw] == '#':
                            return np.array(robot)

                    if len(next_floor) > 0:
                        points_to_move.append(next_floor)
                    floor += move[0]
                    ws = [p[1] for p in points_to_move[-1]]
                    f = grid[floor][min(ws):max(ws)+1]

                if '#' not in f:
                    points_to_move.reverse()
                    for points in points_to_move:
                        for xh, xw in points:
                            grid[xh+move[0]][xw] = grid[xh][xw]
                            grid[xh][xw] = '.'
                    grid[rh][rw] = '.'
                    grid[rh+move[0]][rw] = '@'

                    return np.array(robot + move)


    return robot

def ex2(data: str):
    """Solve ex1"""

    grid, moves, H, W = load_data(data)
    double_grid = [[''] * W * 2 for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if grid[h][w] == '#':
                double_grid[h][2*w] = '#'
                double_grid[h][2*w +1] = '#'
            elif grid[h][w] == 'O':
                double_grid[h][2*w] = '['
                double_grid[h][2*w +1] = ']'
            elif grid[h][w] == '.':
                double_grid[h][2*w] = '.'
                double_grid[h][2*w +1] = '.'
            else:
                double_grid[h][2*w] = '@'
                double_grid[h][2*w +1] = '.'

    grid = double_grid
    W = 2*W

    h, w = (1, 1)
    while grid[h][w] != '@':
        w += 1
        if w == W:
            w = 1
            h += 1

    robot = np.array((h, w))

    for i, move in enumerate(moves):
        robot = move_robot2(grid, H, W, robot, directions[move])



    ans = 0
    for h in range(H):
        for w in range(W):
            if grid[h][w] == '[':
                ans += 100 * h + w


    return ans


assert ex1(load("samplesmall.txt")) == 2028
assert ex1(load("samplebig.txt")) == 10092
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("samplebig.txt")) == 9021
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()
