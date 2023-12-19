"""Imports"""
from os import path
import sys
# from collections import deque
# import math
import regex as re
from colorama import Fore
# import numpy as np
# from heapq import *
from shapely.geometry import Polygon

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False

def g_to_str(grid: list):
    """Printing grid"""
    return '\n'.join([''.join(line) for line in grid]) + "\n"

def pretty_print(grid, path_):
    """Pretty printing grid"""
    print('#' * len(grid[0]))
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if (row, col) in path_:
                print(Fore.RED + char, end='')
            else:
                print(Fore.WHITE + char, end='')
        print(Fore.WHITE + '')

def get_area(moves):
    """Get polygon area"""
    points = [(0, 0)]
    perimeter = 0
    for move in moves:
        pos = points[-1]
        perimeter += move[1]
        if move[0] == 'R':
            points.append((pos[0], pos[1] + move[1]))
        elif move[0] == 'L':
            points.append((pos[0], pos[1] - move[1]))
        elif move[0] == 'D':
            points.append((pos[0] + move[1], pos[1]))
        elif move[0] == 'U':
            points.append((pos[0] - move[1], pos[1]))

    return int(Polygon(points).area) + 1 + perimeter // 2


def ex1(data):
    """Compute ex answer"""
    edges = [re.match(r'(.) (\d+) .*', line).groups() for line in data.split('\n')]


    return get_area([(edge[0], int(edge[1])) for edge in edges])

def ex2(data):
    """Compute ex answer"""
    edges = [re.match(r'.*\(#(.*)(\d)\)', line).groups() for line in data.split('\n')]
    dirs = ['R', 'D', 'L', 'U']

    return get_area([(dirs[int(edge[1])], int(edge[0], 16)) for edge in edges])

assert ex1(load("sample.txt")) == 62
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 952408144115
print(f'ex2 : {ex2((load("input.txt")))}')

DEBUG = True
sys.exit()
