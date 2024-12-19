"""Imports"""
from __future__ import annotations
from os import path
# from copy import deepcopy
import sys
from collections import defaultdict
from operator import itemgetter

# import math
# import re
# from colorama import Fore
# import numpy as np
# from heapq import *
# import networkx as nx
# import functools
# from sympy import solve, symbols, Eq

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> list[tuple]:
    """Loads data as a tuple"""

    data = data.split('\n\n')
    return sorted(((towel, len(towel)) for towel in data[0].split(', ')), key=itemgetter(1), reverse=True), data[1].split('\n')

DEBUG = False

def prune_towels(towels):
    index = 0
    while index < len(towels) and towels[index][1] > 1:
        # a towel that can be made from other towels is redundant
        if design_is_possible_with_towels(towels[index][0], towels[index+1:]):
            towels.pop(index)
        else:
            index += 1

def design_is_possible_with_towels(pattern, towels):
    todo = {pattern, }
    counts = defaultdict(int, {pattern: 1})

    while len(todo) > 0:
        part = max(todo, key=len)
        todo.remove(part)
        for towel, towel_len in towels:
            if part[:towel_len] == towel:
                new_part = part[towel_len:]
                counts[new_part] += counts[part]

                if new_part != '':
                    todo.add(new_part)

    return counts['']

def ex(data: str, part2 = False) -> int:
    """Solve ex"""

    towels, designs = load_data(data)

    if not part2:
        prune_towels(towels)

    ans = 0
    for design in designs:
        possible = design_is_possible_with_towels(design, towels)
        if DEBUG: print(design, possible)
        ans += min(possible, 1 if not part2 else possible)

    return ans

assert ex(load("sample.txt")) == 6
print(f'ex1 : {ex(load("input.txt"))}')

assert ex(load("sample.txt"), True) == 16
print(f'ex2 : {ex(load("input.txt"), True)}')


sys.exit()
