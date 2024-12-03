"""Imports"""
from os import path
# from copy import deepcopy
import sys
from collections import deque
# import math
import re
from colorama import Fore
# import numpy as np
# from heapq import *

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False

def part1(data):
    """Compute ex answer"""
    return data.count('B') + 3 * data.count('C')

def potions_for_pair(pair):
    if 'x' in pair:
        return pair.count('B') + 3 * pair.count('C') + 5 * pair.count('D')
    else:
        return 2 + pair.count('B') + 3 * pair.count('C') + 5 * pair.count('D')

def potions_for_brelan(pair):
    if pair.count('x') == 0:
        return 6 + pair.count('B') + 3 * pair.count('C') + 5 * pair.count('D')
    elif pair.count('x') == 1:
        return 2 + pair.count('B') + 3 * pair.count('C') + 5 * pair.count('D')
    else:
        return pair.count('B') + 3 * pair.count('C') + 5 * pair.count('D')

def part2(data):
    """Compute ex answer"""
    return sum(map(potions_for_pair, re.findall('..', data)))

def part3(data):
    """Compute ex answer"""
    # print(' '.join(re.findall('...', data)))
    # print(' '.join(map(str, map(potions_for_brelan, re.findall('...', data)))))
    return sum(map(potions_for_brelan, re.findall('...', data)))

assert part1("ABBAC") == 5
print(f'Result Part I: {part1(load("input.txt"))}')

assert part2("AxBCDDCAxD") == 28
print(f'Result Part II: {part2(load("input2.txt"))}')

assert part3("xBxAAABCDxCC") == 30
print(f'Result Part III: {part3(load("input3.txt"))}')


