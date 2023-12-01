from os import path
from sys import argv
import numpy as np

dirs = {
    'U': np.array((-1, 0)),
    'L': np.array((0, -1)),
    'D': np.array((1, 0)),
    'R': np.array((0, 1))
}

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return open(file_path(file), "r").read().strip()

debug = False
def dprint(s):
    if debug:
        print(s)

def ex1(data):
    keypad = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9']
    ]
    result = ''
    pos = np.array((1, 1))
    for line in data.split('\n'):
        dprint(line)
        for c in line:
            pos += dirs[c]
            pos[0] = max(0, min(2, pos[0]))
            pos[1] = max(0, min(2, pos[1]))
            dprint(keypad[pos[0]][pos[1]])

        result += keypad[pos[0]][pos[1]]

    return int(result)


def ex2(data):
    keypad = [
        [' ', ' ', '1', ' ', ' '],
        [' ', '2', '3', '4', ' '],
        ['5', '6', '7', '8', '9'],
        [' ', 'A', 'B', 'C', ' '],
        [' ', ' ', 'D', ' ', ' ']
    ]

    result = ''
    pos = np.array((2, 0))
    for line in data.split('\n'):
        dprint(line)
        for c in line:
            temppos = pos + dirs[c]
            temppos[0] = max(0, min(4, temppos[0]))
            temppos[1] = max(0, min(4, temppos[1]))
            if keypad[temppos[0]][temppos[1]] != ' ':
                pos = temppos
                dprint(pos)
            dprint(keypad[pos[0]][pos[1]])

        result += keypad[pos[0]][pos[1]]

    return result

assert ex1(load("sample.txt")) == 1985
print("ex1 : %s" % ex1(load("input.txt")))

assert ex2(load("sample.txt")) == '5DB3'
print("ex2 : %s" % ex2(load("input.txt")))