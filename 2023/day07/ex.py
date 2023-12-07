from os import path
from sys import argv
import math
import regex as re
import numpy as np
from collections import Counter


def file_path(file):
    return f'{path.dirname(argv[0]) if path.dirname(argv[0]) else "."}/{file}'

def load(file):
    return open(file_path(file), "r").read().rstrip()

DEBUG = False
def dprint(*s):
    if DEBUG:
        print(*s)

def hand_type(hand: str):
    c = Counter(hand)
    hand = hand.replace('A', 'E').replace('K', 'D').replace('Q', 'C').replace('J', 'B').replace('T', 'A')
    values = c.values()
    if 5 in values:
        return '50_' + hand
    elif 4 in values:
        return '41_' + hand
    elif 3 in values and 2 in values:
        return '32_' + hand
    elif 3 in values:
        return '31_' + hand
    elif 2 in values and len(list(values)) == 3:
        return '22_' + hand
    elif 2 in values:
        return '21_' + hand
    else:
        return '11_' + hand

def ex1(data):
    data = [ [line.split()[0], int(line.split()[1])] for line in data.split('\n')]
    
    s = sorted(data, key = lambda d: hand_type(d[0]))

    result = 0
    for i in range(len(s)):
        result += (i+1)*s[i][1]

    return result

def ex2(data):

    return 0


assert hand_type('2AAAA') < hand_type('33332')
assert hand_type('31T3K') < hand_type('32T3K')
assert hand_type('77788') < hand_type('77888')
assert ex1(load("sample.txt")) == 6440
DEBUG = True
print(f'ex1 : {ex1(load("input.txt"))}')
exit()

assert ex2(load("sample.txt")) == 71503
print(f'ex2 : {ex2(load("input.txt"))}')
