

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

    lines = load_data(data)
    result = 0

    for line in lines:
        c = len(re.findall(r'(ba|na|ne)', line))
        result += c

    return result

def ex2(data: str) -> int:
    """Solve ex2"""

    lines = load_data(data)
    result = 0

    for line in lines:
        c = len(re.findall(r'(ba|na|ne)', line))
        if c % 2 == 0:
            result += c

    return result

def ex3(data: str) -> int:
    """Solve ex3"""

    lines = load_data(data)
    result = 0

    for line in lines:
        if 'ne' not in line:
            c = len(re.findall(r'(ba|na|ne)', line))
            result += c

    return result

assert ex1(load("sample.txt")) == 24
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 16
print(f'ex2 : {ex2(load("input.txt"))}')

assert ex3(load("sample.txt")) == 19
print(f'ex3 : {ex3(load("input.txt"))}')
sys.exit()

