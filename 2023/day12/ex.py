"""Imports"""
from os import path
import sys
# from collections import Counter
import math
import regex as re
# import numpy as np

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False
def dprint(*s, end='\n'):
    """Print function. Prints or not according to DEBUG"""
    if DEBUG:
        print(*s, end)

def generate_lines(line, results = []):
    """Compute ex answer"""
    if '?' in line:
        return results + generate_lines(line.replace('?', '.', 1), results) + generate_lines(line.replace('?', '#', 1), results)
    else:
        return [line]

def nb_arrangements(line: str):
    """Compute ex answer"""
    record, groups = line.split()
    dprint('gruops', groups)
    r = '^\.*%s\.*$' % '\.+'.join(['#' * int(x) for x in groups.split(',')])
    dprint('regex is: ', r)
    # dprint('list generee', generate_lines(record))
    result = 0
    for line in generate_lines(record):
        if re.match(r, line):
            dprint(line, 'matc  hes')
            result +=1
    
    return result

def ex1(data):
    """Compute ex answer"""

    result = 0

    for line in data.split('\n'):
        dprint("line", line)
        nb = nb_arrangements(line)
        dprint("nb", nb)
        result += nb
    return result

    # return sum([nb_arrangements(line) for line in data.split('\n')])

def ex2(data, h, v, times):
    """Compute ex answer"""
    return 0

# assert len(generate_lines('??.###')) == 4

# assert ex1(load("sample.txt")) == 21
# print(f'ex1 : {ex1(load("input.txt"))}')
DEBUG = True

assert ex2((load("sample.txt")), 10) == 1030
assert ex2((load("sample.txt")), 100) == 8410

print(f'ex2 : {ex2((load("input.txt")), 1000000)}')
sys.exit()
