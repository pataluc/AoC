
"""Imports"""
from __future__ import annotations
from os import path
import sys
import numpy as np

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> list:
    """Loads data as a tuple"""

    return [line.split() for line in data.split('\n')]


def ex1(data: str) -> int:
    """Solve ex1"""
    problems = load_data(data)

    R = len(problems)
    C = len(problems[0])

    result = 0
    for c in range(C):
        if problems[-1][c] == '+':
            p = 0
            for r in range(R - 1):
                p += int(problems[r][c])
        else:
            p = 1
            for r in range(R - 1):
                p *= int(problems[r][c])
        result += p
    return result


def ex2(data: str) -> int:
    """Solve ex1"""
    problems = data.splitlines()

    R = len(problems)
    C = len(problems[0])


    result = 0
    P = []
    for c in range(C-1, -1, -1):
        n = ''.join([problems[r][c] for r in range(R-1)])

        if n != ' ' * (R-1):
            P.append(int(n))
        else:
            if problems[R-1][c+1] == '+':
                result += sum(P)
            else:
                result += np.prod(P)
            P = []

    if problems[R-1][0] == '+':
        result += sum(P)
    else:
        result += np.prod(P)

    print(result)
    return result


assert ex1(load("sample.txt")) == 4277556
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 3263827
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()