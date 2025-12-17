

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

    trashes = load_data(data)
    result = 0
    px, py = (0, 0)

    for x, y in trashes:
        result += abs(x - px) + abs(y - py)
        px, py = x, y

    return result


def ex2(data: str) -> int:
    """Solve ex2"""

    trashes = load_data(data)
    result = 0
    px, py = (0, 0)

    for x, y in trashes:
        result += max(abs(x - px), abs(y - py))
        px, py = x, y

    return result


def ex3(data: str) -> int:
    """Solve ex3"""

    trashes = load_data(data)
    ordered_trashes = sorted([(x+y, x, y) for x, y in trashes])

    result = 0
    px, py = (0, 0)

    for _, x, y in ordered_trashes:
        result += max(abs(x - px), abs(y - py))
        px, py = x, y
    return result


assert ex1(load("sample.txt")) == 24
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 12
print(f'ex2 : {ex2(load("input.txt"))}')

assert ex3(load("sample.txt")) == 9
print(f'ex3 : {ex3(load("input.txt"))}')
sys.exit()

