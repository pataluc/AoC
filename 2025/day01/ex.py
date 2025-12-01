"""Imports"""
from __future__ import annotations
from os import path
import sys
from collections import deque, defaultdict
from itertools import combinations

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> list:
    """Loads data as a tuple"""

    return data.splitlines()


def ex1(data: str) -> int:
    """Solve ex1"""

    instructions = load_data(data)
    position = 50
    result = 0

    for instruction in instructions:
        d = instruction[0]
        v = int(instruction[1:])

        if d == 'R':
            position = (position + v) % 100
        else:
            position = (position - v) % 100
        if position == 0:
            result += 1

    return result


def ex2(data: str) -> int:
    """Solve ex2"""

    instructions = load_data(data)
    position = 50
    result = 0

    for instruction in instructions:
        d = instruction[0]
        v = int(instruction[1:])

        dint = 1 if d == 'R' else -1

        for _ in range(v):
            position += dint
            position = position % 100
            if position == 0:
                result += 1


    return result


assert ex1(load("sample.txt")) == 3
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 6
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()