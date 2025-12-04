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

    return [list(line) for line in data.splitlines()]



def ex1(data: str) -> int:
    """Solve ex1"""
    G = load_data(data)
    R = len(G)
    C = len(G[0])

    D = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    result = 0
    for r in range(R):
        for c in range(C):
            if G[r][c] == '@' and sum([1 for dr, dc in D if 0 <= r+dr < R and 0 <= c+dc < C and G[r+dr][c+dc] == '@']) < 4:
                result += 1
    return result


def ex2(data: str) -> int:
    """Solve ex1"""
    G = load_data(data)
    R = len(G)
    C = len(G[0])

    D = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    result = 0
    while True:
        has_removed = False
        for r in range(R):
            for c in range(C):
                if G[r][c] == '@' and (r, c) and sum([1 for dr, dc in D if 0 <= r+dr < R and 0 <= c+dc < C and G[r+dr][c+dc] == '@']) < 4:
                    G[r][c] = '.'
                    result += 1
                    has_removed = True
        if not has_removed:
            return result

assert ex1(load("sample.txt")) == 13
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 43
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()