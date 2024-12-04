"""Imports"""
from __future__ import annotations
from os import path
# from copy import deepcopy
import sys
# from collections import deque
# import math
import re
from colorama import Fore
# import numpy as np
# from heapq import *
# import networkx as nx

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False

def ex1(data: str) -> int:
    """Compute ex answer"""
    grid = [list(line) for line in data.split('\n')]
    R = len(grid)
    C = len(grid[0])

    result = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'X':
                for (x, y) in [
                    (0, 1),   # E
                    (0, -1),  # W
                    (-1, 0),  # N
                    (1, 0),   # W
                    (-1, 1),  # NE
                    (-1, -1), # NW
                    (1, 1),   # SE
                    (1, -1)   # SW
                    ]:
                    if 0 <= r + 3*x < R and 0 <= c + 3*y < C and grid[r+x][c+y] == 'M' and grid[r+2*x][c+2*y] == 'A' and grid[r+3*x][c+3*y] == 'S':
                        result += 1

    return result



def ex2(data: str) -> int:
    """Compute ex answer"""
    grid = [list(line) for line in data.split('\n')]
    R = len(grid)
    C = len(grid[0])

    result = 0
    xs = 0
    for r in range(1, R-1):
        for c in range(1, C-1):
            if grid[r][c] == 'A':
                xs += 1

                for (nw, ne, sw, se) in [
                    ('M', 'M', 'S', 'S'),
                    ('M', 'S', 'M', 'S'),
                    ('S', 'M', 'S', 'M'),
                    ('S', 'S', 'M', 'M')
                    ]:
                    if grid[r-1][c-1] == nw and grid[r-1][c+1] == ne and grid[r+1][c-1] == sw and grid[r+1][c+1] == se:
                        result += 1

    return result



assert ex1(load("sample.txt")) == 18
print(f'ex1 : {ex1(load("input.txt"))}')


# DEBUG = True
assert ex2(load("sample.txt")) == 9
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()

