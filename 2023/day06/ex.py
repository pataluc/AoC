from os import path
from sys import argv
import math
import regex as re
import numpy as np

def file_path(file):
    return f'{path.dirname(argv[0]) if path.dirname(argv[0]) else "."}/{file}'

def load(file):
    return open(file_path(file), "r").read().rstrip()

DEBUG = False
def dprint(*s):
    if DEBUG:
        print(*s)

def race(t, d):
    discriminant = t*t-4*d
    x1 = math.floor((-1*t + math.sqrt(discriminant)) / -2) + 1
    x2 = math.ceil((-1*t - math.sqrt(discriminant)) / -2) - 1
    diff = x2-x1 + 1

    return diff

def race_brute(t, d):
    ways = 0
    for wait in range(t):
        if wait*(t-wait) > d:
            ways += 1
    return ways

def ex1(data):
    races = [list(map(int, line.split()[1:])) for line in data.split('\n') ]
    results = [race_brute(races[0][i], races[1][i]) for i in range(len(races[0]))]
    dprint(results)

    return np.prod(results)

def ex2(data):
    lines = data.split('\n')
    t = int(lines[0].replace('Time:', '').replace(' ', ''))
    d = int(lines[1].replace('Distance:', '').replace(' ', ''))

    return race_brute(t, d)

assert ex1(load("sample.txt")) == 288
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 71503
print(f'ex2 : {ex2(load("input.txt"))}')
DEBUG = True
