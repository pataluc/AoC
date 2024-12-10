"""Imports"""
from __future__ import annotations
from os import path
# from copy import deepcopy
import sys
from collections import defaultdict
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

def load_data(data: str) -> tuple:
    """Loads data as a tuple"""

    grid = [list(map(int, list(line))) for line in data.split('\n')]
    H = len(grid)
    W = len(grid[0])

    return grid, H, W

DEBUG = False

# def print_grid(H, W, antennas, antinodes):
#     for h in range(H):
#         for w in range(W):
#             if (h, w) in antinodes:
#                 print('#', end='')
#             elif any([(h, w) in antenna_letter for antenna_letter in antennas.values()]):
#                 print('@', end='')
#             else:
#                 print('.', end='')
#         print('')

# def pretty_print(data: list):
#     print(''.join(map(lambda x: str(x) if x >=0 else '.', data)))

def count_hiking_paths(grid, H, W, h, w):
    result = [set()]
    result[0].add((h, w))
    # print(result)

    for i in range(1, 10):
        result.append(set())
        for (h, w) in result[i-1]:
            for dh, dw in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if 0 <= dh + h < H and 0 <= dw + w < W and grid[dh+h][dw+w] == grid[h][w] + 1:
                    result[i].add((dh + h, dw + w))
    # print(result)
    # print(len(result[9]))
    return len(result[9])


def ex1(data: str) -> int:
    """Solve ex1"""

    grid, H, W = load_data(data)

    result = 0
    for h in range(H):
        for w in range(W):
            if grid[h][w] == 0:
                result += count_hiking_paths(grid, H, W, h, w)

    return result


def count_hiking_paths2(grid, H, W, h, w):
    result = [set()]
    result[0].add(tuple([(h, w)]))

    for i in range(1, 10):
        result.append(set())
        for path in result[i-1]:
            (h, w) = path[-1]
            for dh, dw in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if 0 <= dh + h < H and 0 <= dw + w < W and grid[dh+h][dw+w] == grid[h][w] + 1:
                    result[i].add(tuple(list(path) + [(dh + h, dw + w)]))
    # print(result)
    # print(len(result[9]))
    return len(result[9])

def ex2(data: str) -> int:
    """Solve ex1"""


    """Solve ex1"""

    grid, H, W = load_data(data)

    result = 0
    for h in range(H):
        for w in range(W):
            if grid[h][w] == 0:
                result += count_hiking_paths2(grid, H, W, h, w)

    return result

assert ex1(load("sample1.txt")) == 1
assert ex1(load("sample.txt")) == 36
print(f'ex1 : {ex1(load("input.txt"))}')


# DEBUG = True
assert ex2(load("sample.txt")) == 81
print(f'ex2 : {ex2(load("input.txt"))}')

sys.exit()
