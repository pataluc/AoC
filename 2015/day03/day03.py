from os import path
from sys import argv
import numpy as np

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)


def load(file):
    return open(file_path(file), "r").read().rstrip()

debug = False
def dprint(s):
    if debug:
        print(s)

directions = {
    ">": np.array(( 1,  0)),
    "<": np.array((-1,  0)),
    "^": np.array(( 0,  1)),
    "v": np.array(( 0, -1)),
}

def ex1(data):
    visited = set()
    santa = np.array((0, 0))
    visited.add(tuple(santa))
    for c in data:
        santa += directions[c]
        visited.add(tuple(santa))

    return len(visited)
    

def ex2(data):
    visited = set()
    santa = np.array((0, 0))
    robot_santa = np.array((0, 0))
    visited.add(tuple(santa))
    for i, c in enumerate(data):
        if i % 2:
            robot_santa += directions[c]
            visited.add(tuple(robot_santa))
        else:
            santa += directions[c]
            visited.add(tuple(santa))

    return len(visited)

assert ex1(">") == 2
assert ex1("^>v<") == 4
assert ex1("^v^v^v^v^v") == 2

assert ex2("^v") == 3
assert ex2("^>v<") == 3
assert ex2("^v^v^v^v^v") == 11

data = load("input.txt")
print("ex1 : %s" % ex1(data))
print("ex2 : %s" % ex2(data))