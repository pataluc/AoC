"""Imports"""
from os import path
import sys
from collections import Counter
import math
# import regex as re
# import numpy as np

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False
def dprint(*s):
    """Print function. Prints or not according to DEBUG"""
    if DEBUG:
        print(*s)

def ex1(data, start='AAA', end='ZZZ'):
    """Compute ex answer"""
    instructions, network = data.split('\n\n')
    l_instructions = len(instructions)
    network = {g.split()[0]: [g.split()[2][1:-1], g.split()[3][:-1]] for g in network.split('\n')}

    dprint(instructions, network)
    step = 0
    pos = start
    while not pos.endswith(end):
        rl = 0 if instructions[step % l_instructions] == 'L' else 1
        pos = network[pos][rl]
        step += 1

    return step

def ex2(data):
    """Compute ex answer"""
    instructions, network = data.split('\n\n')
    l_instructions = len(instructions)
    network = {g.split()[0]: [g.split()[2][1:-1], g.split()[3][:-1]] for g in network.split('\n')}

    return math.lcm(*[ ex1(data, s, 'Z') for s in network.keys() if s[2] == 'A' ])


assert ex1(load("sample.txt")) == 2
assert ex1(load("sample2.txt")) == 6
print(f'ex1 : {ex1(load("input.txt"))}')


assert ex2(load("sample3.txt")) == 6
print(f'ex2 : {ex2(load("input.txt"))}')
DEBUG = True
sys.exit()
