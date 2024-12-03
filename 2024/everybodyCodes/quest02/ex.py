"""Imports"""
from os import path
# from copy import deepcopy
import sys
from collections import deque
# import math
import re
from colorama import Fore
# import numpy as np
# from heapq import *

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False

def part1(data):
    """Compute ex answer"""
    words, sentence = data.split('\n\n')
    words = (words.split(':')[1]).split(',')

    result = sum(map(lambda x: sentence.count(x), words))
    # print(result)
    return result

def sentence_indexes(sentence, word):
    indexes = set()
    for match in re.finditer(r'(?=(%s))' % word, sentence):
        # print(match)
        indexes.update(list(range(match.start(1), match.end(1))))
    return indexes

def part2(data):
    """Compute ex answer"""
    words, sentence = data.split('\n\n')
    words = (words.split(':')[1]).split(',')

    # for line in sentence.split('\n'):
    runes = set()
    for word in words:
        runes.update(sentence_indexes(sentence, word))
        runes.update(sentence_indexes(sentence, word[::-1]))

    # print(len(runes))
    return len(runes)

def part3(data):
    """Compute ex answer"""
    # print(' '.join(re.findall('...', data)))
    # print(' '.join(map(str, map(potions_for_brelan, re.findall('...', data)))))
    return sum(map(potions_for_brelan, re.findall('...', data)))

assert part1("""WORDS:THE,OWE,MES,ROD,HER

AWAKEN THE POWER ADORNED WITH THE FLAMES BRIGHT IRE""") == 4
print(f'Result Part I: {part1(load("input1.txt"))}')

assert part2("""WORDS:THE,OWE,MES,ROD,HER

AWAKEN THE POWE ADORNED WITH THE FLAMES BRIGHT IRE
THE FLAME SHIELDED THE HEART OF THE KINGS
POWE PO WER P OWE R
THERE IS THE END""") == 37
print(f'Result Part II: {part2(load("input2.txt"))}')
sys.exit(0)

assert part3("xBxAAABCDxCC") == 30
print(f'Result Part III: {part3(load("input3.txt"))}')


