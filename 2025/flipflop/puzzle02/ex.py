

"""Imports"""
from __future__ import annotations
from os import path
import sys
import math
import regex as re


def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> list:
    """Loads data as a tuple"""

    return data.splitlines()

def ex1(data: str) -> int:
    """Solve ex1"""

    result = 0
    pos = 0

    for c in list(data):
        if c == '^':
            pos += 1
        else:
            pos -= 1
        result = max(result, pos)

    return result

def ex2(data: str) -> int:
    """Solve ex2"""

    result = 0
    pos = 0
    last = ''
    i = 1

    for c in list(data):
        if c == last:
            i += 1
        else:
            i = 1
        last = c
        if c == '^':
            pos += i
        else:
            pos -= i
        result = max(result, pos)

    return result

def fib(i: int) -> int:
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i - 1) + fib(i - 2)

assert fib(6) == 8
assert fib(15) == 610

def ex3(data: str) -> int:
    """Solve ex3"""

    result = 0

    pos = 0
    for g in re.findall(r'(\^+|v+)', data):
        print(g, fib(len(g)))
        if g[0] == '^':
            pos += fib(len(g))
        else:
            pos -= fib(len(g))
        result = max(result, pos)
    print(result)
    return result

assert ex1('^v^v^v^v^v') == 1
assert ex1('^^^v^^^^vvvvvvv') == 6
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2('^^^v^^^^vvvvvvv') == 15
print(f'ex2 : {ex2(load("input.txt"))}')

assert ex3('^^^^^') == 5
assert ex3('^^^v^^^^vvvvvvv') == 4
assert ex3('^^^^^^^^^^^^vvvvvvvvv^') == 144
print(f'ex3 : {ex3(load("input.txt"))}')
sys.exit()

