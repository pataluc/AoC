from os import path
from sys import argv
import numpy as np

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return open(file_path(file), "r").read().strip()

debug = True
def dprint(s):
    if debug:
        print(s)

def ex1(data):
    lines = [list(map(int, line.split())) for line in data.split('\n')]
    return sum(map(lambda t : 1 if (t[0] + t[1] > t[2]) and (t[1] + t[2] > t[0]) and (t[0] + t[2] > t[1]) else 0, lines))


def ex2(data):
    lines = [list(map(int, line.split())) for line in data.split('\n')]
    result = 0
    for r in range(len(lines) // 3):
        for c in range(3):
            print(lines[3*r+0][c], lines[3*r+1][c], lines[3*r+2][c])
            if      (lines[3*r+0][c] + lines[3*r+1][c] > lines[3*r+2][c]) \
                and (lines[3*r+1][c] + lines[3*r+2][c] > lines[3*r+0][c]) \
                and (lines[3*r+0][c] + lines[3*r+2][c] > lines[3*r+1][c]):
                result += 1

    return result

print("ex1 : %s" % ex1(load("input.txt")))
print("ex2 : %s" % ex2(load("input.txt")))