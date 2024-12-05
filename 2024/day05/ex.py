"""Imports"""
from __future__ import annotations
from os import path
# from copy import deepcopy
import sys
# from collections import deque
# import math
# import re
# from colorama import Fore
# import numpy as np
# from heapq import *
# import networkx as nx
import functools

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False

def load_data(data: str) -> tuple:
    """Loads data as a tuple of list(tuple) and list(list)"""
    rules, updates = data.split('\n\n')

    rules = [tuple(map(int, rule.split('|'))) for rule in rules.split('\n')]
    updates = [list(map(int, update.split(','))) for update in updates.split('\n')]

    return rules, updates

def is_update_correct(rules, update):
    """Check whether an update follows the rules"""
    index_map = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in index_map and y in index_map and index_map[x] > index_map[y]:
            return False
    return True


def ex1(data: str) -> int:
    """Compute ex answer"""

    rules, updates = load_data(data)

    result = 0
    for update in updates:
        if is_update_correct(rules, update):
            result += int(update[len(update) // 2])

    return result

def ex2(data: str) -> int:
    """Compute ex answer"""

    rules, updates = load_data(data)

    def compare_updates(x, y):
        """Compare pages based on rules"""
        if (x, y) in rules:
            return 1
        if (y, x) in rules:
            return -1

        return 0

    result = 0
    for update in updates:
        if not is_update_correct(rules, update):
            update_sorted = sorted(update, key=functools.cmp_to_key(compare_updates))

            result += int(update_sorted[len(update_sorted) // 2])

    return result

assert ex1(load("sample.txt")) == 143
print(f'ex1 : {ex1(load("input.txt"))}')


# DEBUG = True
assert ex2(load("sample.txt")) == 123
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()
