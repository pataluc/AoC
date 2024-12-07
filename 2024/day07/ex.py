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

def load_data(data: str) -> list:
    """Loads data as a tuple"""

    result = []
    for line in data.split('\n'):
        l = line.split(': ')
        result.append((int(l[0]), list(map(int, l[1].split(' ')))))

    return result

DEBUG = False

def can_be_true(test_value: int, equation: list) -> bool:
    """Compute if adding operator in equation could give test_value"""
    
    operators_nb = len(equation) - 1
    for i in range(pow(2, operators_nb)):
        operators = format(i, '#0%db'% (2 + operators_nb))[2:]
        result = equation[0]
        for j, v in enumerate(operators):
            if v == '0':
                result += equation[j+1]
            else:
                result *= equation[j+1]
            if result > test_value:
                break
        if result == test_value:
            return True
        
    return False


def can_be_true2(test_value: int, equation: list) -> bool:
    """Compute if adding operator in equation could give test_value"""
    
    operators_nb = len(equation) - 1
    for i in range(pow(3, operators_nb)):

        operators = list(' ' * operators_nb)
        q = i
        for o in range(operators_nb):
            operators[o] = q % 3
            q = q // 3

        result = equation[0]
        for j, v in enumerate(operators):
            if v == 0:
                result += equation[j+1]
            elif v == 1:
                result *= equation[j+1]
            else:
                result = int('%d%d' % (result, equation[j+1]))
            if result > test_value:
                break
        if result == test_value:
            return True
        
    return False


def ex1(data: str) -> int:
    """Solve ex1"""
    equations = load_data(data)
    result = 0
    for test_value, equation in equations:
        if can_be_true(test_value, equation):
            result += test_value

    return result

def ex2(data: str) -> int:
    """Solve ex1"""
    equations = load_data(data)
    result = 0
    for test_value, equation in equations:
        if can_be_true2(test_value, equation):
            result += test_value

    return result


assert ex1(load("sample.txt")) == 3749
print(f'ex1 : {ex1(load("input.txt"))}')


# DEBUG = True
assert ex2(load("sample.txt")) == 11387
print(f'ex2 : {ex2(load("input.txt"))}')



sys.exit()
