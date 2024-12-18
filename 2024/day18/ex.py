"""Imports"""
from __future__ import annotations
from os import path
# from copy import deepcopy
import sys
from collections import defaultdict, deque
# import math
import re
# from colorama import Fore
# import numpy as np
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

def load_data(data: str) -> list[tuple]:
    """Loads data as a tuple"""

    bytes = [tuple(int(coord) for coord in line.split(',')) for line in data.split('\n')]

    return bytes

DEBUG = False

def get_neighbours(pos, bytes, L):
    x, y = pos
    ans = []
    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 <= nx < L and 0 <= ny < L and (nx, ny) not in bytes:
            ans.append((nx, ny))
    return ans

def bfs(bytes, start, end, L):
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        current, cost = queue.popleft()
        # print("queue: ", queue)
        # print("visited: ", visited)
        # print("current: ", current)
        # print("neighbours: ", get_neighbours(current, bytes, L))
        # print()
        for neighbour in get_neighbours(current, bytes, L):
            if neighbour == end:
                return cost + 1
            if neighbour not in visited:
                queue.append((neighbour, cost + 1))
                visited.add(neighbour)

def ex1(data: str, L = 71, after = 1024) -> int:
    """Solve ex1"""

    bytes = load_data(data)
    # print(bytes)

    # for y in range(L):
    #     for x in range(L):
    #         print('#' if (x, y) in bytes[:after] else '.', end='')
    #     print()
    
    ans = bfs(bytes[:after], (0, 0), (L-1, L-1), L)
    # print(ans)
    return ans

def ex2(data: str, L = 71, after = 1024):

    bytes = load_data(data)

    while bfs(bytes[:after], (0, 0), (L-1, L-1), L):
        print(after)
        after += 1

    ans = "%d,%d" % bytes[after-1]
    print(ans)
    return ans

assert ex1(load("sample.txt"), 7, 12) == 22
print(f'ex1 : {ex1(load("input.txt"))}')

# DEBUG = True
assert ex2(load("sample.txt"), 7, 12) == '6,1'
print(f'ex2 : {ex2(load("input.txt"), after = int(sys.argv[1] if len(sys.argv) > 1 else 1024))}')


sys.exit()
