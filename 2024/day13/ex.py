"""Imports"""
from __future__ import annotations
from os import path
# from copy import deepcopy
import sys
from collections import defaultdict
# import math
import re
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

def load_data(data: str) -> tuple:
    """Loads data as a tuple"""
    
    machines = []
    for machine in data.split('\n\n'):
        lines = machine.split('\n')
        machines.append({
            'a': tuple(map(int, re.findall(r'Button .: X\+(\d\d), Y\+(\d\d)', lines[0])[0])),
            'b': tuple(map(int, re.findall(r'Button .: X\+(\d\d), Y\+(\d\d)', lines[1])[0])),
            'p': tuple(map(int, re.findall(r'Prize: X=(\d+), Y=(\d+)', lines[2])[0]))
        })

    return machines

DEBUG = False

def min_cost_to_win(machine: dict, shift_p = 0) -> int:
    """Computes how much tokens are needed to win this machine"""

    ax, ay = machine['a']
    bx, by = machine['b']
    px, py = machine['p']

    # ex2
    px += shift_p
    py += shift_p

    b = (ax * py - ay * px) / (ax*by - ay*bx)
    a = (px - b*bx) / ax
    
    if b >= 0 and int(b) == b and a >= 0 and a == int(a):
        return int(3*a + b)
    else:
        return 0

def ex(data: str, shift_p = 0) -> int:
    """Solve ex1"""

    machines = load_data(data)

    ans = sum([min_cost_to_win(machine, shift_p) for machine in machines])

    return ans


assert ex(load("sample.txt")) == 480
print(f'ex1 : {ex(load("input.txt"))}')

print(f'ex2 : {ex(load("input.txt"), 10000000000000)}')


sys.exit()
