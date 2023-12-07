"""Imports"""
from os import path
import sys
from collections import Counter
# import math
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

def hand_type(hand: str):
    """Compute hand type (5 of kind, 4 of kind, full, pairs, etc)"""
    counter = Counter(hand)
    values = ''.join(list(map(lambda x: str(x[1]), counter.most_common(2))))
    if len(values) == 1:
        return '51'
    return values

def hand_score(hand: str):
    """Compute hand score in camel game"""
    return hand_type(hand) + '_' \
        + hand.replace('A', 'E').replace('K', 'D').replace('Q', 'C') \
        .replace('J', 'B').replace('T', 'A')

def hand_score2(hand: str):
    """Compute hand score in camel game ex2"""
    return (max(hand_type(hand.replace('J', j)) for j in 'AKQT98765432') if 'J' in hand else hand_type(hand)) + '_' \
        + hand.replace('A', 'E').replace('K', 'D').replace('Q', 'C') \
        .replace('J', '0').replace('T', 'A')

def ex(data, function):
    """Compute ex answer"""
    data = [ [line.split()[0], int(line.split()[1])] for line in data.split('\n') ]
    sorted_data = sorted(data, key = lambda d: function(d[0]))

    result = 0
    for i, line in enumerate(sorted_data):
        result += (i+1)*line[1]

    return result

assert hand_score('2AAAA') < hand_score('33332')
assert hand_score('31T3K') < hand_score('32T3K')
assert hand_score('77788') < hand_score('77888')
assert ex(load("sample.txt"), hand_score) == 6440
print(f'ex1 : {ex(load("input.txt"), hand_score)}')

assert max(sorted([hand_score("QJJQ2".replace('J', j)) for j in 'AKQT98765432'])) == "41_CCCC2"
assert hand_score2('T55J5') < hand_score2('QQQJA') < hand_score2('KTJJT')
assert ex(load("sample.txt"), hand_score2) == 5905

print(f'ex2 : {ex(load("input.txt"), hand_score2)}')
DEBUG = True
sys.exit()
