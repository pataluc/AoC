from os import path
from sys import argv

import regex as re

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)


def load(file):
    return open(file_path(file), "r").read().rstrip()

debug = False
def dprint(*s):
    if debug:
        print(*s)

def card_score1(line):
    _, winning, have = re.match(r'Card +(\d+): (.*) \| (.*)', line).groups()
    winning = winning.split()
    have = have.split()

    result = 0
    for card in winning:
        if card in have:
            result = 1 if result == 0 else 2*result

    return result

def card_score2(line):
    _, winning, have = re.match(r'Card +(\d+): (.*) \| (.*)', line).groups()
    winning = winning.split()
    have = have.split()

    result = 0
    for card in winning:
        if card in have:
            result =+1
    return result

def ex1(data):
    return sum([card_score1(line) for line in data.split('\n')])

def ex2(data):
    lines = data.split('\n')
    copies = [1]* len(lines)

    for line in lines:
        card_id, winning, have = re.match(r'Card +(\d+): (.*) \| (.*)', line).groups()
        winning = winning.split()
        have = have.split()

        score = 0
        for card in winning:
            if card in have:
                score += 1

        for i in range(score):
            if i < len(copies):
                copies[int(card_id) + i] += copies[int(card_id) - 1]

    return sum(copies)

assert ex1(load("sample.txt")) == 13
print("ex1 : %s" % ex1(load("input.txt")))
debug = False

assert ex2(load("sample.txt")) == 30
print("ex2 : %s" % ex2(load("input.txt")))