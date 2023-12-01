from os import path
from sys import argv
import numpy as np
from collections import deque

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)


def load(file):
    return open(file_path(file), "r").read().rstrip()

debug = False
def dprint(s):
    if debug:
        print(s)

def ex1(data):
    north = np.array((0, 1))
    east = np.array((1, 0))
    south = np.array((0, -1))
    west = np.array((-1, 0))

    dirs = deque([north, east, south, west])

    pos = np.array((0, 0))
    for instruction in data.split(', '):
        direction, value = instruction[0], int(instruction[1:])

        dirs.rotate(-1 if direction == 'R' else 1)
        pos = pos + value*dirs[0]

    return abs(pos[0]) + abs(pos[1])


def ex2(data):
    visited = set()
    north = np.array((0, 1))
    east = np.array((1, 0))
    south = np.array((0, -1))
    west = np.array((-1, 0))

    dirs = deque([north, east, south, west])

    pos = np.array((0, 0))
    for instruction in data.split(', '):
        direction, value = instruction[0], int(instruction[1:])

        dirs.rotate(-1 if direction == 'R' else 1)
        for _ in range(value):
            pos = pos + dirs[0]
            if tuple(pos) in visited:
                return abs(pos[0]) + abs(pos[1])
            else:
                visited.add(tuple(pos))

assert ex1("R2, L3") == 5
assert ex1("R2, R2, R2") == 2
assert ex1("R5, L5, R5, R3") == 12

data = "R4, R1, L2, R1, L1, L1, R1, L5, R1, R5, L2, R3, L3, L4, R4, R4, R3, L5, L1, R5, R3, L4, R1, R5, L1, R3, L2, R3, R1, L4, L1, R1, L1, L5, R1, L2, R2, L3, L5, R1, R5, L1, R188, L3, R2, R52, R5, L3, R79, L1, R5, R186, R2, R1, L3, L5, L2, R2, R4, R5, R5, L5, L4, R5, R3, L4, R4, L4, L4, R5, L4, L3, L1, L4, R1, R2, L5, R3, L4, R3, L3, L5, R1, R1, L3, R2, R1, R2, R2, L4, R5, R1, R3, R2, L2, L2, L1, R2, L1, L3, R5, R1, R4, R5, R2, R2, R4, R4, R1, L3, R4, L2, R2, R1, R3, L5, R5, R2, R5, L1, R2, R4, L1, R5, L3, L3, R1, L4, R2, L2, R1, L1, R4, R3, L2, L3, R3, L2, R1, L4, R5, L1, R5, L2, L1, L5, L2, L5, L2, L4, L2, R3"
print("ex1 : %s" % ex1(data))

assert ex2("R8, R4, R4, R8, R8, R4, R4, R8, R8, R4, R4, R8, R8, R4, R4, R8") == 4
print("ex2 : %s" % ex2(data))