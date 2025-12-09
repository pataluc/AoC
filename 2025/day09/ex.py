

"""Imports"""
from __future__ import annotations
from os import path
import sys
import math
import networkx as nx

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> list:
    """Loads data as a tuple"""

    return [list(map(int, line.split(','))) for line in data.split('\n')]

def distance(box1: tuple, box2: tuple) -> float:
    x1, y1, z1 = box1
    x2, y2, z2 = box2

    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

def ex1(data: str) -> int:
    """Solve ex1"""
    redtiles = load_data(data)
    result = 0
    for i, (x1, y1) in enumerate(redtiles):
        for j in range(i+1, len(redtiles)):
            x2, y2 = redtiles[j]
            area = (1+abs(x2-x1))*(1+abs(y2-y1))
            if area > result:
                result = area
    return result

def between(x: int, y: int, z: int) -> bool:
    return (x < z < y or x > z > y)

def ex2(data: str) -> int:
    """Solve ex2"""
    redtiles = load_data(data)

    result = 0
    for i, (x1, y1) in enumerate(redtiles):
        for j in range(i+1, len(redtiles)):
            x2, y2 = redtiles[j]
            area = (1+abs(x2-x1))*(1+abs(y2-y1))
            if area > result:
                c = True
                for k, (x3, y3) in enumerate(redtiles):
                    print(result, area, (x1, y1, i), (x2, y2, j), (x3, y3, k), k not in [i,j] , between(x1, x2, x3) , between(y1, y2, y3))
                    if k not in [i,j] and between(x1, x2, x3) and between(y1, y2, y3):
                        c = False
                        break
                if c:
                    result = area
    print(result)
    return result



assert ex1(load("sample.txt")) == 50
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 24
print(f'ex2 : {ex2(load("input.txt"))}')
sys.exit()

