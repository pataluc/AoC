import re
from os import path
from sys import argv
from collections import deque

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    board_map, path = open(file_path(file), "r").read().split("\n\n")
    path = list(map(lambda x: int(x) if x not in "RL" else x, filter(lambda x: x != '', path)))

    print(path)
    return (board_map, path)

debug = False

def solve(data, term):
    if term not in data:
        return term
    elif isinstance(data[term], int):
        return data[term]
    else:
        m, op, n = data[term].split(' ')
        return "(%s %s %s)" % (solve(data, m), op, solve(data, n))

def ex1(data):
    return

def ex2(data: dict):
    return

sample = load("sample.txt")
# print(sample)
assert ex1(sample.copy()) == 152
data = load("input.txt")
print("ex1 : %s" % ex1(data.copy()))

assert ex2(sample) == 301
print("ex2 : %s" % ex2(data))
