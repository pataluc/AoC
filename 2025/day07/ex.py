
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

    return [list(line) for line in data.split('\n')]


def ex1(data: str) -> int:
    """Solve ex1"""
    G = load_data(data)

    R = len(G)
    C = len(G[0])

    result = 0
    for r in range(1, R):
        for c in range(C):
            if G[r-1][c] in ['S', '|']:
                if G[r][c] == '.':
                    G[r][c] = '|'
                elif G[r][c] == '^':
                    G[r][c-1] = '|'
                    G[r][c+1] = '|'
                    result += 1
    #     print(''.join(G[r]))

    # print(result)
    return result


def ex2(data: str) -> int:
    """Solve ex1"""
    G = load_data(data)

    R = len(G)
    C = len(G[0])

    for r in range(1, R):
        for c in range(C):
            if G[r-1][c] == 'S':
                G[r][c] = 1
            elif G[r-1][c] not in ['.', '^']:
                if G[r][c] == '.':
                    G[r][c] = G[r-1][c]
                elif G[r][c] == '^':
                    G[r][c-1] = G[r-1][c] if G[r][c-1] == '.' else (G[r][c-1] + G[r-1][c])
                    G[r][c+1] = G[r-1][c] if G[r][c+1] == '.' else (G[r][c+1] + G[r-1][c])
                else:
                    G[r][c] = G[r-1][c] + G[r][c]

    return sum([v for v in G[R-1] if v != '.'])


assert ex1(load("sample.txt")) == 21
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 40
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()