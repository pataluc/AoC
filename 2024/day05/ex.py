"""Imports"""
from __future__ import annotations
from os import path
# from copy import deepcopy
import sys
# from collections import deque
# import math
import re
from colorama import Fore
# import numpy as np
# from heapq import *
# import networkx as nx

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False

def ex1(data: str) -> int:
    """Compute ex answer"""

    raw_rules, to_produce = data.split('\n\n')

    # rules = dict()
    # for rule in raw_rules.split('\n'):
    #     b, a = tuple(map(int, rule.split('|')))
    #     if b in rules:
    #         rules[b].add(a)
    #     else:
    #         rules[b] = {a}
    # print(rules)

    # result = 0
    # for pages in to_produce.split('\n'):
    #     pages = list(map(int, pages.split(',')))
    #     correct = True
    #     for i in range(len(pages)):
    #         for j in range(i+1, len(pages)):
    #             if pages[j] in rules and pages[i] in rules[pages[j]]:
    #                 correct = False
    #                 break
    #         if not correct:
    #             break
    #     print("pages are correct: ", pages)

    rules = [r"%s.*%s" % (a, b) for (b, a) in map(lambda r: r.split('|'), raw_rules.split('\n'))]
    print(rules)

    for pages in to_produce.split('\n'):
        print(pages)
        if any(map(lambda rule: re.match(rule, pages), rules)):
            print("pages are incorrect: ", pages)



def ex2(data: str) -> int:
    """Compute ex answer"""
    grid = [list(line) for line in data.split('\n')]
    R = len(grid)
    C = len(grid[0])

    result = 0
    xs = 0
    for r in range(1, R-1):
        for c in range(1, C-1):
            if grid[r][c] == 'A':
                xs += 1

                for (nw, ne, sw, se) in [
                    ('M', 'M', 'S', 'S'),
                    ('M', 'S', 'M', 'S'),
                    ('S', 'M', 'S', 'M'),
                    ('S', 'S', 'M', 'M')
                    ]:
                    if grid[r-1][c-1] == nw and grid[r-1][c+1] == ne and grid[r+1][c-1] == sw and grid[r+1][c+1] == se:
                        result += 1

    return result



assert ex1(load("sample.txt")) == 143
print(f'ex1 : {ex1(load("input.txt"))}')


# DEBUG = True
assert ex2(load("sample.txt")) == 9
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()

