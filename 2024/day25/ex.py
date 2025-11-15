"""Imports"""
from __future__ import annotations
from os import path
import sys
from collections import deque, defaultdict
from itertools import combinations
import numpy as np

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> defaultdict[str, list[str]]:
    """Loads data as a tuple"""

    locks_or_keys = data.split('\n\n')
    locks = list()
    keys = list()
    for lk in locks_or_keys:
        lines = lk.split('\n')
        e = np.array([sum(1 if lines[j][i] == '#' else 0 for j in range(7)) for i in range(5)]) - np.array([1, 1, 1, 1, 1])
        if lines[0] == '#####':
            locks.append(e)
        else:
            keys.append(e)

    return locks, keys

def ex1(data: str) -> int:
    """Solve ex1"""

    locks, keys = load_data(data)

    ans = 0

    for lock in locks:
        # print("lock:  ", lock)
        for key in keys:
            # print("  key: ", key)
            # print("       ", lock+key)
            if all(map(lambda x: x <= 5, lock + key)):
                ans += 1
    print(ans)
    return ans


def ex2(data: str) -> int:
    """Solve ex2"""

    wires, gates = load_data(data)

    return ''


assert ex1(load("sample.txt")) == 3
print(f'ex1 : {ex1(load("input.txt"))}')

# ex2('123')
# exit()
# ex2(load("sample2.txt"))
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()
