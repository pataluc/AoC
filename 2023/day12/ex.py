"""Imports"""
from os import path
import sys
# from collections import Counter
# import math
import re
# import numpy as np

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False

def generate_lines(line, results = []):
    """Compute ex answer"""
    if '?' in line:
        return results + generate_lines(line.replace('?', '.', 1), results) + generate_lines(line.replace('?', '#', 1), results)
    else:
        return [line]

def nb_arrangements(record: str, groups):
    """Compute ex answer"""

    if DEBUG: print('groups', groups)
    r = '^\.*%s\.*$' % '\.+'.join(['#' * int(x) for x in groups.split(',')])
    if DEBUG: print('regex is: ', r)
    # if DEBUG: print('list generee', generate_lines(record))
    result = 0
    for line in generate_lines(record):
        if re.match(r, line):
            if DEBUG: print(line, 'matches')
            result +=1

    return result

def ex1(data):
    """Compute ex answer"""
    result = 0

    for record, group in [line.split() for line in data.split('\n')]:
        if DEBUG: print("line", record, group)
        nb = nb_arrangements(record, group)
        if DEBUG: print("nb", nb)
        result += nb
    return result

    # return sum([nb_arrangements(line) for line in data.split('\n')])

def ex2(data):
    """Compute ex answer"""
    result = 0
    for record, group in [line.split() for line in data.split('\n')]:
        record2, group2 = '?'.join([record]*5), ','.join([group]*5)
        if DEBUG: print("line", record, group)
        
        nb1 = nb_arrangements(record, group)
        nb2 = nb_arrangements(record2, group2)
        nb = pow(nb1/nb2, 3) * nb2

        print("nb", nb)
        result += nb
        if result > 1 : exit()
    return result

assert len(generate_lines('??.###')) == 4

assert ex1(load("sample.txt")) == 21
print(f'ex1 : {ex1(load("input.txt"))}')

sys.exit()
assert ex2((load("sample.txt"))) == 525152
print(f'ex2 : {ex2((load("input.txt")), 1000000)}')

DEBUG = True
