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

def load_data(data: str) -> dict:
    """Loads data as a tuple"""

    result = defaultdict(list)
    grid = [line for line in data.split('\n')]
    H = len(grid)
    W = len(grid[0])

    for h in range(H):
        for w in range(W):
            c = grid[h][w]
            if c != '.':
                result[c].append((h, w))

    return result, H, W

DEBUG = False

def print_grid(H, W, antennas, antinodes):
    for h in range(H):
        for w in range(W):
            if (h, w) in antinodes:
                print('#', end='')
            elif any([(h, w) in antenna_letter for antenna_letter in antennas.values()]):
                print('@', end='')
            else:
                print('.', end='')
        print('')


def ex1(data: str) -> int:
    """Solve ex1"""

    antennas, W, H = load_data(data)
    antinodes = set()

    for positions in antennas.values():
        l = len(positions)
        for l1 in range(l):
            for l2 in range(l1 + 1, l):
                h1, w1 = positions[l1]
                h2, w2 = positions[l2]
                if 0 <= (2*h1 - h2) < H and 0 <= (2*w1 - w2) < W:
                    antinodes.add((2*h1 - h2, 2*w1-w2))
                if 0 <= (2*h2 - h1) < H and 0 <= (2*w2 - w1) < W:
                    antinodes.add((2*h2  - h1, 2*w2-w1))

    return len(antinodes)

def ex2(data: str) -> int:
    """Solve ex1"""

    antennas, W, H = load_data(data)
    antinodes = set()

    for positions in antennas.values():
        l = len(positions)
        for l1 in range(l):
            for l2 in range(l1 + 1, l):
                h1, w1 = positions[l1]
                h2, w2 = positions[l2]
                for ha in range(H):
                    for wa in range(W):
                        va1 = (h1 -ha, w1-wa)
                        va2 = (h2 -ha, w2-wa)
                        if (va1[0] * va2[1]) - (va1[1] * va2[0]) == 0:
                            antinodes.add((ha, wa))

    return len(antinodes)


assert ex1(load("sample.txt")) == 14
print(f'ex1 : {ex1(load("input.txt"))}')


# DEBUG = True
assert ex2(load("sample.txt")) == 34
print(f'ex2 : {ex2(load("input.txt"))}')

sys.exit()
