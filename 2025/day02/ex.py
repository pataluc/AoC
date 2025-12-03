"""Imports"""
from __future__ import annotations
from os import path
import sys
from collections import deque, defaultdict
from itertools import combinations
import regex as re


def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> list:
    """Loads data as a tuple"""

    return data.split(',')


def ex1(data: str) -> int:
    """Solve ex1"""

    ranges = load_data(data)

    result = 0
    for r in ranges:
        m, n = [int(v) for v in r.split('-')]
        for i in range(m, n+1):
            if re.match(r'^(\d+)\1$', str(i)):
                result += i

    return result


def ex2(data: str) -> int:
    """Solve ex1"""

    ranges = load_data(data)

    result = 0
    for r in ranges:
        m, n = [int(v) for v in r.split('-')]
        for i in range(m, n+1):
            if re.match(r'^(\d+)\1+$', str(i)):
                result += i

    return result


assert ex1(load("sample.txt")) == 1227775554
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 4174379265
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()