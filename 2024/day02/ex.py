"""Imports"""
from __future__ import annotations
from os import path
# from copy import deepcopy
import sys
# from collections import deque
# import math
# import regex as re
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

def is_report_safe(report: list) -> bool:
    direction = report[1] - report[0]
    i = 1
    while i < len(report):
        if not(0 < abs(report[i] - report[i-1]) < 4) or ((report[i] - report[i-1]) / direction < 0):
            return False
        i += 1
    return True

def is_report_safe2(report: list) -> bool:
    if DEBUG: print('##################')
    if DEBUG: print(report)

    errors = 0
    direction = report[1] - report[0]
    i = 1
    while i < len(report):
        if not(0 < abs(report[i] - report[i-1]) < 4) or ((report[i] - report[i-1]) / direction < 0):
            if DEBUG: print('Errors: %d, when ommitting %d, checking between %d and %d\nConditions:' % (errors, report[i], report[i-1], (report[i+1] if (i < len(report)) else '')))
            if DEBUG: print('  - (errors == 0): %r' % (errors == 0))
            if DEBUG: print('  - (i < len(report)): %r' % (i < len(report)))
            if DEBUG: print('  - (0 < abs(report[i+1] - report[i-1]) < 4): %r' % (0 < abs(report[i+1] - report[i-1]) < 4))
            if DEBUG: print('  - ((report[i+1] - report[i-1]) / direction < 0): %r' % ((report[i+1] - report[i-1]) / direction < 0))

            if (errors == 0) and (i < len(report)) and (0 < abs(report[i+1] - report[i-1]) < 4) and ((report[i+1] - report[i-1]) / direction < 0):
                if DEBUG: print('Ommitting %d' % report[i])
                i += 1
                errors = 1
            else:
                return False
        i += 1
    return True

def ex1(data: str) -> int:
    """Compute ex answer"""
    
    result = 0
    for line in data.split('\n'):
        if is_report_safe(list(map(int, line.split(' ')))):
            result += 1
    
    return result

DEBUG = True
def ex2(data: str) -> int:
    """Compute ex answer"""
    
    result = 0
    for line in data.split('\n'):
        if DEBUG: print(line)
        report = list(map(int, line.split(' ')))
        if is_report_safe(report):
            if DEBUG: print('True')

            result += 1
        else:
            for i in range(len(report)):
                if is_report_safe(report[:i] + report[(i+1):]):
                    if DEBUG: print('True')
                    result += 1
                    break
            if DEBUG: print('False')
    
    return result


assert ex1(load("sample.txt")) == 2
print(f'ex1 : {ex1(load("input.txt"))}')


# DEBUG = True
assert ex2(load("sample.txt")) == 4
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()

