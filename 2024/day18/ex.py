"""Imports"""
from __future__ import annotations
from os import path
# from copy import deepcopy
import sys
from collections import deque
# import math
# import re
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

    bytes_positions = [tuple(int(coord) for coord in line.split(',')) for line in data.split('\n')]

    return bytes_positions

DEBUG = False

def get_neighbours(x: int, y: int, bytes_positions: list, L: int) -> list:
    """Neighbours of (x, y) in bytes map"""
    ans = []
    for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
        if 0 <= nx < L and 0 <= ny < L and (nx, ny) not in bytes_positions:
            ans.append((nx, ny))
    return ans

def bfs(bytes_positions: list, L: int)-> int:
    """BFS algo"""
    queue = deque([(0, 0, 0)])
    visited = set()

    while queue:
        x, y, cost = queue.popleft()
        # print("queue: ", queue)
        # print("visited: ", visited)
        # print("current: ", current)
        # print("neighbours: ", get_neighbours(current, bytes, L))
        # print()
        if (x, y) == (L-1, L-1):
            return cost
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for nx, ny in get_neighbours(x, y, bytes_positions, L):
            queue.append((nx, ny, cost + 1))
    return 0

def ex1(data: str, L = 71, after = 1024) -> int:
    """Solve ex1"""

    bytes_positions = load_data(data)

    ans = bfs(bytes_positions[:after], L)
    return ans

def ex2(data: str, L = 71, after = 1024):
    """Solving ex2"""

    bytes_positions = load_data(data)
    low = after
    high = len(bytes_positions) - 1
    while low + 1 < high:
        mid = (high + low) // 2
        res = bfs(bytes_positions[:mid], L)
        if res:
            low = mid
        else:
            high = mid

    ans = f"{bytes_positions[low][0]},{bytes_positions[low][1]}"
    return ans

assert ex1(load("sample.txt"), 7, 12) == 22
print(f'ex1 : {ex1(load("input.txt"))}')

# DEBUG = True
assert ex2(load("sample.txt"), 7, 12) == '6,1'
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()
