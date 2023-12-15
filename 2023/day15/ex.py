"""Imports"""
from os import path
import sys
from collections import OrderedDict
# import math
import regex as re
# import numpy as np

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False

def hash_algorithm(string: str):
    """Compute HASH algorithm for string"""
    value = 0
    for character in string:
        value = ((value + ord(character)) * 17) % 256
    return value

def ex1(data):
    """Compute ex answer"""
    sequences = data.split('\n')[0].split(',')

    return sum(hash_algorithm(sequence) for sequence in sequences)

def ex2(data):
    """Compute ex answer"""
    boxes = [ OrderedDict() for _ in range(256)]
    sequences = data.split('\n')[0].split(',')

    for sequence in sequences:
        parsing = re.match(r'(\w+)(.)(\d)*', sequence).groups()
        label, sign = parsing[:2]
        box_nb = hash_algorithm(label)
        if sign == '-':
            if label in boxes[box_nb]:
                boxes[box_nb].move_to_end(label)
                boxes[box_nb].popitem()
        else:
            focal = parsing[-1]
            boxes[box_nb][label] = focal

        if DEBUG:
            print(f'\nAfter "{sequence}":')
            for i, box in enumerate(boxes):
                if len(box) > 0:
                    boxes_list = "] [".join([label + ' ' + focal for label, focal in box.items() ])
                    print(f'Box {i}: [{boxes_list}]')

    result = 0
    for i, box in enumerate(boxes):
        for j, focal in enumerate(box.values()):
            result += (i+1)*(j+1)*int(focal)
    return result

assert hash_algorithm('HASH') == 52
assert ex1(load("sample.txt")) == 1320
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 145
print(f'ex2 : {ex2((load("input.txt")))}')

DEBUG = True
sys.exit()
