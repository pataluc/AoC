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
    valid_instructions = re.findall(r'mul\(([0-9]+),([0-9]+)\)', data)

    return sum([int(x)*int(y) for (x, y) in valid_instructions])

def ex2(data: str) -> int:
    """Compute ex answer"""
    # print(data)
    # data = re.sub(r'don\'t\(\).*?do\(\)', '', data)
    # print(data)

    valid_instructions = re.findall(r'(mul\(([0-9]+),([0-9]+)\)|do\(\)|don\'t\(\))', data)
    result = 0
    do = True
    for instruction in valid_instructions:
        if instruction[0] == 'do()':
            do = True
        elif instruction[0] == 'don\'t()':
            do = False
        elif do:
            result += int(instruction[1])*int(instruction[2])

    return result


assert ex1(load("sample.txt")) == 161
print(f'ex1 : {ex1(load("input.txt"))}')


# DEBUG = True
assert ex2(load("sample2.txt")) == 48
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()

