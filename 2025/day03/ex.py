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

    return data.splitlines()


def solve(data: str, nb: int) -> int:
    """Solve ex1"""

    banks = load_data(data)

    result = 0
    for bank in banks:
        digits = [ '' ] * nb
        for i in range(nb):
            m = 0 if i == 0 else bank[m:n].index(digits[i-1]) + m + 1
            n = -1 * (nb - 1 - i) if i < nb - 1 else len(bank)
            digits[i] = max(list(bank[m:n]))

        result += int(''.join(digits))

    return result

def ex1(data: str) -> int:
    """Solve ex1"""

    return solve(data, 2)


def ex2(data: str) -> int:
    """Solve ex@"""

    return solve(data, 12)


assert ex1(load("sample.txt")) == 357
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 3121910778619
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()