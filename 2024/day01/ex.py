"""Imports"""
from __future__ import annotations
from os import path
from copy import deepcopy
import sys
from collections import deque
# import math
# import regex as re
from colorama import Fore
import numpy as np
# from heapq import *
import networkx as nx

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False

def data_load(data: str) -> tuple:
    return tuple(list(zip(*[list(map(int, line.split('   '))) for line in data.split('\n')])))

def ex1(data: str) -> int:
    """Compute ex answer"""
    left, right = map(sorted, data_load(data))
    
    return sum(map(lambda t: abs(t[0]-t[1]), zip(left, right)))

def ex2(data: str) -> int:
    """Compute ex answer"""
    left, right = data_load(data)
    
    result = 0
    for l in left:
        result += l * right.count(l)
    return result


assert ex1(load("sample.txt")) == 11
print(f'ex1 : {ex1(load("input.txt"))}')


# DEBUG = True
assert ex2(load("sample.txt")) == 31
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()
