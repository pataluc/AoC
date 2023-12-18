"""Imports"""
from os import path
import sys
from collections import Counter
import math
# import regex as re
# import numpy as np
from shapely.geometry import Polygon

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False
def dprint(*s, end='\n'):
    """Print function. Prints or not according to DEBUG"""
    if DEBUG:
        print(*s, end)

def find_adjacents(data, i, j):
    if data[i][j] == '|':
        return [(i-1, j), (i+1, j)]
    if data[i][j] == '-':
        return [(i, j-1), (i, j+1)]
    if data[i][j] == 'L':
        return [(i-1, j), (i, j+1)]
    if data[i][j] == 'J':
        return [(i-1, j), (i, j-1)]
    if data[i][j] == '7':
        return [(i, j-1), (i+1, j)]
    if data[i][j] == 'F':
        return [(i, j+1), (i+1, j)]
    return []

def find_paths(data):
    """Compute ex answer"""
    start_pos = (0,0)
    for i, _ in enumerate(data):
        if 'S' in data[i]:
            start_pos = (i, data[i].index('S'))
            break
    # dprint(data)
    # dprint('start :', start_pos)

    start_positions=[]
    for p in [(-1 ,0), (0, -1), (0, 1), (1, 0)]:
        if start_pos in find_adjacents(data, start_pos[0] + p[0], start_pos[1] + p[1]):
            start_positions.append((start_pos[0] + p[0], start_pos[1] + p[1]))
    
    path1 = [start_pos, start_positions[0]]
    path2 = [start_pos, start_positions[1]]

    while path1[-1] != path2[-1] and path1[-1] != start_pos:
        # dprint('path1: ', path1)
        # dprint('path2: ', path2)
        adj1 = find_adjacents(data, *path1[-1])
        adj2 = find_adjacents(data, *path2[-1])
        # dprint(adj1)
        # dprint(adj2)
        adj1.remove(path1[-2])
        adj2.remove(path2[-2])
        path1 += adj1
        path2 += adj2

    return path1, path2

def ex1(data):
    """Compute ex answer"""
    data = [list(line) for line in data.split('\n')]

    return len(find_paths(data)[0]) - 1

def ex2(data):
    """Compute ex answer"""
    data = [list(line) for line in data.split('\n')]

    path1, path2 = find_paths(data)
    path = (path1 + path2[::-1])[:-1]

    area = int(Polygon(path).area)
    perimeter = len(path)
    
    result = area - perimeter // 2 +1

    if DEBUG: print(result)
    return result

assert ex1(load("sample.txt")) == 4
assert ex1(load("sample2.txt")) == 8
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample3.txt")) == 4
assert ex2(load("sample4.txt")) == 8
assert ex2(load("sample5.txt")) == 10
print(f'ex2 : {ex2(load("input.txt"))}')
DEBUG = True
sys.exit()
