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

def blink(stones: list) -> list:
    result = []

    for stone in stones:
        stone_string = str(stone)
        if stone == 0:
            result.append(1)
        elif len(str(stone)) % 2 == 0:
            result.append(int(stone_string[:len(stone_string) // 2]))
            result.append(int(stone_string[len(stone_string) // 2:]))
        else:
            result.append(stone * 2024)
    return result

seen_stones = dict()

def blink_by_stone(stone: int, times_left: int) -> int:
    stone_string = str(stone)
    if times_left == 0:
        return 1
    elif (stone, times_left) in seen_stones:
        return seen_stones[(stone, times_left)]
    elif stone == 0:
        res = blink_by_stone(1, times_left - 1)
        seen_stones[(stone, times_left)] = res
        return res
    elif len(str(stone)) % 2 == 0:
        res = blink_by_stone(int(stone_string[:len(stone_string) // 2]), times_left - 1) + blink_by_stone(int(stone_string[len(stone_string) // 2:]), times_left - 1)
        seen_stones[(stone, times_left)] = res
        return res
    else:
        res = blink_by_stone(stone * 2024, times_left - 1)
        seen_stones[(stone, times_left)] = res
        return res

def ex(data: str, blinks = 25) -> int:
    """Solve ex1"""

    stones = list(map(int, data.split()))

    return sum([blink_by_stone(stone, blinks) for stone in stones])

assert blink([0, 1, 10, 99, 999]) == [1, 2024, 1, 0, 9, 9, 2021976]
assert ex('125 17', 6) == 22
assert ex('125 17', 25) == 55312
print(f'ex1 : {ex(load("input.txt"))}')
print(f'ex2 : {ex(load("input.txt"), 75)}')


sys.exit()
