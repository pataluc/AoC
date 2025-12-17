"""Imports"""
from __future__ import annotations
from os import path
import sys
import math
# import regex as re
from collections import deque


def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> list:
    """Loads data as a tuple"""

    return [tuple(map(int, line.split(' '))) for line in data.splitlines()]

def solve(dimensions: int, size: tuple[int]) -> int:
    numerator = math.factorial(sum([s-1 for s in size]))
    denominator = math.prod([math.factorial(s - 1) for s in size])

    return numerator // denominator


def ex1(data: str) -> int:
    """Solve ex1"""
    return sum([solve(2, m) for m in load_data(data)])


def ex2(data: str) -> int:
    """Solve ex2"""
    return sum([solve(3, (x, y, x)) for x, y in load_data(data)])


def ex3(data: str) -> int:
    """Solve ex3"""
    return sum([solve(x, tuple([y]*x)) for x, y in load_data(data)])

assert ex1(load("sample.txt")) == 11
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 108
print(f'ex2 : {ex2(load("input.txt"))}')

assert ex3("2 2") == 2
assert ex3("3 3") == 90
assert ex3("2 3") == 6
assert ex3("4 3") == 2520
print(f'ex3 : {ex3(load("input.txt"))}')

sys.exit()
