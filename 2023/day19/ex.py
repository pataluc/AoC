"""Imports"""
from os import path
import sys
from collections import deque
import math
import regex as re
from colorama import Fore
import numpy as np
from heapq import *
from copy import deepcopy

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False

def g_to_str(grid: list):
    return '\n'.join([''.join(line) for line in grid]) + "\n"

def pretty_print(grid, path):
    print('#' * len(grid[0]))
    for r, line in enumerate(grid):
        for c, char in enumerate(line):
            if (r, c) in path:
                print(Fore.RED + char, end='')
            else:
                print(Fore.WHITE + char, end='')
        print(Fore.WHITE + '')

def process_part(workflows: list, part: dict, workflow='in'):
    if workflow == 'A':
        return sum(part.values())
    if workflow == 'R':
        return 0

    rules = workflows[workflow]
    x, m, a, s = part.values()

    for rule in rules:
        if ':' not in rule:
            return process_part(workflows, part, rule)
        r, n = rule.split(':')
        if eval(r):
            return process_part(workflows, part, n)



def ex1(data):
    """Compute ex answer"""
    workflows, parts = data.split('\n\n')

    workflows = [re.match(r'(?P<name>\w+){(?P<rules>.*)}', line).groupdict() for line in workflows.split('\n')]
    workflows = {w['name']: w['rules'].split(',') for w in workflows}
    if DEBUG: print(workflows)

    parts = [re.match(r'{x=(?P<x>\d+),m=(?P<m>\d+),a=(?P<a>\d+),s=(?P<s>\d+)}', line).groupdict() for line in parts.split('\n')]
    parts = [{k: int(v) for k, v in part.items()} for part in parts]
    if DEBUG: print(parts)

    return sum(process_part(workflows, part) for part in parts)

def process2(workflows: list, path: list, indent=0, result = 0):
    last_w, limits = path[-1]

    if last_w == 'A':
        if DEBUG: print('  ' * indent, Fore.GREEN, "Accepted:", # limits, 
              "nb:", np.prod([1 + limit[1] - limit[0] for limit in limits.values()]), Fore.LIGHTMAGENTA_EX,
              "result: ", result + np.prod([1 + limit[1] - limit[0] for limit in limits.values()]), Fore.WHITE)
        return result + np.prod([1 + limit[1] - limit[0] for limit in limits.values()])
    if last_w == 'R':
        return result

    rules = workflows[last_w]
    if DEBUG: print('  ' * indent,'Workflow', Fore.BLUE, last_w, Fore.WHITE, limits)

    for rule in rules:
        if DEBUG: print('  ' * indent, 'Evaluating', rule)
        if ':' not in rule:
            if DEBUG: print('  ' * indent, 'Going straight to', rule)
            return process2(workflows, path + [(rule, deepcopy(limits))], indent+1, result)

        r, n = rule.split(':')
        if r[1] == '<':
            v = int(r[2:])
            tmp = limits[r[0]][1]
            limits[r[0]][1] = v - 1

            if limits[r[0]][0] < limits[r[0]][1]:
                result = process2(workflows, path + [(n, deepcopy(limits))], indent+1, result)
            else:
                break
            limits[r[0]][1] = tmp
            limits[r[0]][0] = v
        if r[1] == '>':
            v = int(r[2:])
            tmp = limits[r[0]][0]
            limits[r[0]][0] = v + 1
            if  limits[r[0]][0] < limits[r[0]][1]:
                result = process2(workflows, path + [(n, deepcopy(limits))], indent+1, result)
            else:
                break
            limits[r[0]][0] = tmp
            limits[r[0]][1] = v
    if DEBUG: print("sortie")
    return result



def ex2(data):
    """Compute ex answer"""
    workflows = data.split('\n\n')[0]

    workflows = [re.match(r'(?P<name>\w+){(?P<rules>.*)}', line).groupdict() for line in workflows.split('\n')]
    workflows = {w['name']: w['rules'].split(',') for w in workflows}

    path = [('in', {'x': [1,4000], 'm': [1,4000], 'a': [1,4000], 's': [1,4000]})]

    return process2(workflows, path)

assert ex1(load("sample.txt")) == 19114
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 167409079868000
print(f'ex2 : {ex2((load("input.txt")))}')

DEBUG = True
sys.exit()
