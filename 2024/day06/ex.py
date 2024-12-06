"""Imports"""
from __future__ import annotations
from os import path
# from copy import deepcopy
import sys
# from collections import deque
# import math
# import re
# from colorama import Fore
# import numpy as np
# from heapq import *
# import networkx as nx
import functools

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> list:
    """Loads data as a tuple of list(tuple) and list(list)"""
    grid = list(map(list, data.split('\n')))
    return grid, len(grid), len(grid[0])

DEBUG = False

def g_to_str(grid: list):
    """Printing grid"""
    return '\n'.join([''.join(line) for line in grid]) + "\n"

def solve(grid: list, H: int, W: int, h: int, w: int) -> int:
    """Compute ex answer"""

    dir_index = 0
    dir_rotations = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    visited = set()
    visited_with_dir = set()

    while True:
        dir = dir_rotations[dir_index % 4]
        # print(dir, h, w)
        if (h + dir[0] >= H) or (h + dir[0] < 0) or (w + dir[1] >= W) or (w + dir[1] < 0):
            # print(1+len(visited))
            return 1+len(visited)
        if grid[h+dir[0]][w + dir[1]] != '#':
            visited.add((h,w))
            h += dir[0]
            w += dir[1]
        else:
            dir_index += 1
        # if DEBUG: print((h, w, dir_index), visited_with_dir)
        if (h, w, dir_index % 4) in visited_with_dir:
            return None
        else:
            visited_with_dir.add((h, w, dir_index % 4))
        # if DEBUG: print(g_to_str(grid))


def ex1(data: str) -> int:
    """Solve ex1"""
    grid, H, W = load_data(data)
    h = data.index('^') // (W + 1)
    w = data.index('^') % (W + 1)
    grid[h][w] = '.'

    return solve(grid, H, W, h, w)

def ex2(data: str) -> int:
    """Compute ex answer"""
    grid, H, W = load_data(data)
    h = data.index('^') // (W + 1)
    w = data.index('^') % (W + 1)
    grid[h][w] = '.'

    result = 0
    for ho in range(H):
        for wo in range(W):
            # print("Trying to obstacle in ", ho, wo)
            grid, H, W = load_data(data)
            grid[h][w] = '.'

            if (ho, wo) != (h, w) and grid[ho][wo] != '#':
                grid[ho][wo] = '#'
                if not solve(grid, H, W, h, w):
                    result += 1
    
    return result


assert ex1(load("sample.txt")) == 41
print(f'ex1 : {ex1(load("input.txt"))}')


DEBUG = True
assert ex2(load("sample.txt")) == 6
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()
