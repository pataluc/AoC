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

def file_path(file: str) -> str:
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file: str) -> list:
    """Load file"""
    return list(map(int, open(file_path(file), "r", encoding='utf-8').read().rstrip().split(',')))

def process(array,  pos = 0):
    op = array[pos]

    if op == 1:
        a, b = array[array[pos + 1]], array[array[pos + 2]]
        output = array[pos + 3]
        array[output] = a + b
        process(array, pos + 4)
    elif op == 2:
        a, b = array[array[pos + 1]], array[array[pos + 2]]
        output = array[pos + 3]
        array[output] = a * b
        process(array, pos + 4)
    elif op == 3:
        a, b = array[array[pos + 1]], array[array[pos + 2]]
        output = array[pos + 3]
        array[output] = a * b
        process(array, pos + 4)
    return array

def ex1(data: list) -> int:
    mem = data.copy()
    mem[1] = 12
    mem[2] = 2
    return process(mem)[0]

def ex2(data: list) -> int:
    for noun in range(100):
        for verb in range(100):
            mem = data.copy()
            mem[1] = noun
            mem[2] = verb
            mem = process(mem)

            if mem[0] == 19690720:
                return 100 * noun + verb


assert ex1(load("input-day2.txt")) == 6568671
assert ex2(load("input-day2.txt")) == 3951
print(f'ex1 : {ex1(load("input.txt"))}')


assert ex1(load("sample.txt")) == 161
print(f'ex1 : {ex1(load("input.txt"))}')