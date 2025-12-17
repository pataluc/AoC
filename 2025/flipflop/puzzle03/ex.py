

"""Imports"""
from __future__ import annotations
from os import path
import sys
import math
import regex as re
from collections import Counter


def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> list:
    """Loads data as a tuple"""

    return [tuple(map(int, line.split(','))) for line in data.splitlines()]

def ex1(data: str) -> int:
    """Solve ex1"""

    bushes = load_data(data)
    c = Counter()
    for bush in bushes:
        c[bush] += 1

    return ','.join(map(str, c.most_common(1)[0][0]))


def ex2(data: str) -> int:
    """Solve ex2"""

    bushes = load_data(data)
    result = 0
    for r, g, b in bushes:
        if g > r and g > b and r != b:
            result += 1

    return result


def ex3(data: str) -> int:
    """Solve ex3"""

    bushes = load_data(data)
    result = 0
    for r, g, b in bushes:
        if g == r or g == b or r == b: # Special
            result += 10
        elif g > r and g > b: # Green
            result += 2
        elif r > g and r > b: # Red
            result += 5
        else: # Blue
            result += 4
    return result


assert ex1(load("sample.txt")) == '10,20,30'
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 0
print(f'ex2 : {ex2(load("input.txt"))}')

assert ex3(load("sample.txt")) == 37
print(f'ex3 : {ex3(load("input.txt"))}')
sys.exit()

