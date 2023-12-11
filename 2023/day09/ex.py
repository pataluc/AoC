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

def get_next_value(serie: list):
    dprint(serie)

    if all(map(lambda x: x==0, serie)):
        dprint([0] + serie)
        return 0
    else:
        sub_serie = []
        for i, _ in enumerate(serie):
            if i > 0:
                sub_serie.append(serie[i] - serie[i-1])
        return serie[-1] + get_next_value(sub_serie)


def get_previous_value(serie: list):
    if all(map(lambda x: x==0, serie)):
        return 0
    else:
        sub_serie = []
        for i, _ in enumerate(serie):
            if i > 0:
                sub_serie.append(serie[i] - serie[i-1])
        # dprint([serie[0] - get_previous_value(sub_serie)] + serie)
        return serie[0] - get_previous_value(sub_serie)


def ex1(data):
    """Compute ex answer"""
    
    return sum([get_next_value(list(map(int, line.split()))) for line in data.split('\n')])

def ex2(data):
    """Compute ex answer"""
    for line in data.split('\n'):
        serie = list(map(int, line.split()))
        dprint([get_previous_value(serie)] + serie)
    dprint('='*20)
    return sum([get_previous_value(list(map(int, line.split()))) for line in data.split('\n')])


assert ex1(load("sample.txt")) == 114
print(f'ex1 : {ex1(load("input.txt"))}')


assert ex2(load("sample.txt")) == 2
print(f'ex2 : {ex2(load("input.txt"))}')
DEBUG = True
sys.exit()
