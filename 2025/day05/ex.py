
"""Imports"""
from __future__ import annotations
from os import path
import sys


def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> list:
    """Loads data as a tuple"""

    data = data.split('\n\n')
    return [[list(map(int, line.split('-'))) for line in data[0].splitlines()], [int(line) for line in data[1].splitlines()]]


def ex1(data: str) -> int:
    """Solve ex1"""
    ranges, ingredients = load_data(data)

    fresh = set()

    for i in ingredients:
        for m, n in ranges:
            if m <+ i <= n:
                fresh.add(i)
    return len(fresh)


def ex2(data: str) -> int:
    """Solve ex1"""
    ranges, _ = load_data(data)

    fresh = []

    for m, n in sorted(ranges):
        if fresh and fresh[-1][1] >= m - 1:
            fresh[-1][1] = max(fresh[-1][1], n)
        else:
            fresh.append([m,n])

    result = sum([n + 1 - m for m, n in fresh])
    return result


assert ex1(load("sample.txt")) == 3
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 14
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()