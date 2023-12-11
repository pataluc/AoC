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
def dprint(*s, end='\n'):
    """Print function. Prints or not according to DEBUG"""
    if DEBUG:
        print(*s, end)

def expand_universe(data):
    """Compute ex answer"""
    universe = []

    # expand vertically
    lines = data.split('\n')
    dprint("Before\n" + "\n".join(lines))
    for i, line in enumerate(lines):
        if line == '.' * (len(line)):
            dprint(i, "expands vert")
            universe.append(line)
            universe.append(line)
        else:
            universe.append(line)
    dprint("After vertically\n" + "\n".join(universe))
    
    # expand horizontally
    for i in range(len(universe[0]) -1 , -1, -1):
        if all(map(lambda line: line[i] == '.', universe)):
            dprint(i, "expands horiz")
            for j, line in enumerate(universe):
                universe[j] = line[:i] + '..' + line[i+1:]
    
    dprint("After horizontally\n" + "\n".join(universe))
    return universe

def get_expansion(data: list):
    """Compute ex answer"""
    vert = []

    # expand vertically
    lines = data.split('\n')
    for i, line in enumerate(lines):
        if line == '.' * (len(line)):
            # dprint(i, "expands vert")
            vert.append(i)
    
    horiz = []
    # expand horizontally
    for i in range(len(lines[0])):
        if all(map(lambda line: line[i] == '.', lines)):
            # dprint(i, "expands horiz")
            horiz.append(i)
    
    # dprint("Expands on ", vert, "vertically and on ", horiz, "horizontally")
    return lines, vert, horiz

def find_galaxies(data: list):
    galaxies = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '#':
                galaxies.append((i, j))
    return galaxies

def ex1(data):
    """Compute ex answer"""
    galaxies = find_galaxies(data)

    result = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            d = abs(galaxies[j][0] - galaxies[i][0]) + abs(galaxies[j][1] - galaxies[i][1])
            dprint("Distance between gal ", i, galaxies[i], "and gal ", j, galaxies[j], "=", d)
            result += d

    dprint(galaxies)

    return result

def ex2(data, h, v, times):
    """Compute ex answer"""
    galaxies = find_galaxies(data)
    dprint(data, h, v, times, galaxies)

    result = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            dprint("Distance between gal ", i, galaxies[i], "and gal ", j, galaxies[j])
            expanded_h = len(list(filter(lambda x: (galaxies[j][0] < x < galaxies[i][0]) or (galaxies[j][0] > x > galaxies[i][0]), h)))
            expanded_v = len(list(filter(lambda x: (galaxies[j][1] < x < galaxies[i][1]) or (galaxies[j][1] > x > galaxies[i][1]), v)))

            d = abs(galaxies[j][0] - galaxies[i][0]) + abs(galaxies[j][1] - galaxies[i][1]) + (expanded_h + expanded_v) * (times - 1)
            result += d

    dprint(galaxies)

    return result

sample = expand_universe(load("sample.txt"))
assert sample == ['....#........', '.........#...', '#............', '.............', '.............', '........#....', '.#...........', '............#', '.............', '.............', '.........#...', '#....#.......']
assert ex1(sample) == 374

print(f'ex1 : {ex1(expand_universe(load("input.txt")))}')

assert ex2(*get_expansion(load("sample.txt")), 10) == 1030
assert ex2(*get_expansion(load("sample.txt")), 100) == 8410

print(f'ex2 : {ex2(*get_expansion(load("input.txt")), 1000000)}')
DEBUG = True
sys.exit()
