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

def pretty_print(data: list):
    print(''.join(map(lambda x: str(x) if x >=0 else '.', data)))

def get_disk(data: str) -> list:
    """get disk content from disk map"""
    result = []
    for i in range(len(data) // 2):
        result.extend([i] * int(data[2*i]))
        result.extend([-1] * int(data[2*i+1]))
    result.extend([len(data)//2]*int(data[-1]))

    return result

def ex1(data: str) -> int:
    """Solve ex1"""

    disk_data = get_disk(data)

    while -1 in disk_data:
        i = disk_data.index(-1)
        disk_data[i] = disk_data[-1]
        disk_data.pop()
        while disk_data[-1] == -1:
            disk_data.pop()

        # pretty_print(disk_data)
    result = 0
    for i, v in enumerate(disk_data):
        result += i*v
    return result

def get_disk2(data: str) -> list:
    """get disk content from disk map"""
    result = []
    for i in range(len(data) // 2):
        result.append((i, int(data[2*i])))
        result.append((-1, int(data[2*i+1])))
    result.append((len(data) //2, int(data[-1])))

    return result

def pretty_print2(data: list):
    result = ''
    for i, l in data:
        result += (str(i) if i >= 0 else '.') * l
    return result

def ex2(data: str) -> int:
    """Solve ex1"""

    disk_data = get_disk2(data)
    # print(pretty_print2(disk_data))

    max_id = len(disk_data) // 2

    for file_id in range(max_id, 0, -1):
        index = -1
        for i in range(len(disk_data) - 1, 0, -1):
            if disk_data[i][0] == file_id:
                index = i
                break
        file_size = disk_data[index][1]
        print("procesing %d of size %d" % (file_id, file_size))
        if file_id % 100 == 0: print('trying to move %d which is %d blocks long' % (file_id, file_size))
        for i, file in enumerate(disk_data):
            if file[0] == -1 and i < index:
                if file[1] == file_size:
                    print("  there some space on %d" % i)
                    disk_data[i] = (file_id, file_size)
                    disk_data[index] = (-1, file_size)
                    break
                elif file[1] >= file_size:
                    print("  there some space on %d" % i)
                    disk_data[index] = (-1, file_size)
                    disk_data = disk_data[:i] + [(file_id, file_size), (-1, file[1] - file_size)] + disk_data[i+1:-1]
                    break
        else:
            print("  can't move it")

        # print(pretty_print2(disk_data))

    result = 0
    for i, v in enumerate(list(pretty_print2(disk_data))):
        # print(i, v)
        if v != '.':
            result += i*int(v)
    return result


# assert ''.join(map(lambda x: str(x) if x >=0 else '.', get_disk(load("sample.txt")))) == '00...111...2...333.44.5555.6666.777.888899'
# assert ex1(load("sample.txt")) == 1928
# print(f'ex1 : {ex1(load("input.txt"))}')


# DEBUG = True
assert ex2(load("sample.txt")) == 2858
# print(f'ex2 : {ex2(load("input.txt"))}')

sys.exit()
