

"""Imports"""
from __future__ import annotations
from os import path
import sys
import math
# import regex as re
# from collections import Counter


def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> list:
    """Loads data as a tuple"""

    return [tuple(map(int, line.split(','))) for line in data.splitlines()]

def ex1(data: str, D: int = 100, S: int = 1000, F: int = 500) -> int:
    """Solve ex1"""

    birds = load_data(data)

    result = 0
    for i, (vx, vy) in enumerate(birds):
        if (S // 4) <= vx*D % S < (3*S // 4) and (S // 4) <= vy*D % S < (3*S // 4):
            result += 1
        # print(f"Bird {i}: x: {vx*D % S}, y: {vy*D % S}")
    return result


def ex2(data: str) -> int:
    """Solve ex2"""

    return sum([ex1(data, t) for t in range(3600, 3600*1000, 3600)])


def ex3(data: str) -> int:
    """Solve ex3"""

    return sum([ex1(data, t) for t in range(31556926, 31556926*1000, 31556926)])


print(f'ex1 : {ex1(load("input.txt"))}')

print(f'ex2 : {ex2(load("input.txt"))}')

print(f'ex3 : {ex3(load("input.txt"))}')

sys.exit()
