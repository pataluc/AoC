

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

    return list(data)

def search_exit(tunnels: str, pos: int, power_tunnels: bool = False) -> int:
    s = tunnels[pos]
    for i, c in enumerate(tunnels):
        if c == s and i != pos:
            # print(f'Entering tunnel {s} in {pos} and exiting in {i} ({abs(pos - i)} steps)')
            return i, -1 * abs(pos - i) if power_tunnels and s.isupper() else abs(pos - i)


def ex1(data: str) -> int:
    """Solve ex1"""

    tunnels = load_data(data)
    result = 0
    pos = 0

    while pos < len(tunnels):
        new_pos, steps = search_exit(tunnels, pos)
        result += steps
        pos = new_pos + 1

    return result


def ex2(data: str) -> int:
    """Solve ex2"""

    tunnels = load_data(data)
    pos = 0
    visited = set()

    while pos < len(tunnels):
        visited.add(tunnels[pos])
        new_pos, _ = search_exit(tunnels, pos)
        pos = new_pos + 1

    for v in visited:
        tunnels.remove(v)
        tunnels.remove(v)
    tunnels.reverse()
    for v in set(tunnels):
        tunnels.remove(v)
    tunnels.reverse()

    return ''.join(tunnels)


def ex3(data: str) -> int:
    """Solve ex3"""

    tunnels = load_data(data)
    result = 0
    pos = 0

    while pos < len(tunnels):
        new_pos, steps = search_exit(tunnels, pos, True)
        result += steps
        pos = new_pos + 1

    return result


assert ex1(load("sample.txt")) == 38
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 'Bc'
print(f'ex2 : {ex2(load("input.txt"))}')

assert ex3(load("sample.txt")) == -6
print(f'ex3 : {ex3(load("input.txt"))}')

sys.exit()
