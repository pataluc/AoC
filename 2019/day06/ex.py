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

def count_orbits(orbits: dict, star: str, parents = 1) -> int:
    if star in orbits:
        return parents * len(orbits[star]) + sum([count_orbits(orbits, substar, parents + 1) for substar in orbits[star]])
    else:
        return 0

def ex1(data: str) -> int:
    """Compute ex answer"""
    orbits = dict()
    for orbit in data.split('\n'):
        p, c = orbit.split(')')
        if p not in orbits:
            orbits[p] = [c]
        else:
            orbits[p].append(c)

    return count_orbits(orbits, 'COM')

def ex2(data: str) -> int:
    """Compute ex answer"""
    parents = dict()
    for orbit in data.split('\n'):
        p, c = orbit.split(')')
        parents[c] = p
    
    san_to_com = ['SAN']
    current = san_to_com[0]
    while current != 'COM':
        san_to_com.append(parents[current])
        current = parents[current]

    jumps = 0
    current = 'YOU'

    while current not in san_to_com:
        jumps += 1
        current = parents[current]

    return jumps + san_to_com.index(current) - 2


assert ex1(load("sample.txt")) == 42
print(f'ex1 : {ex1(load("input.txt"))}')


# DEBUG = True
assert ex2(load("sample2.txt")) == 4
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()

