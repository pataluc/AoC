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

def ex1(data):
    result = 0
    lines = data.split('\n')
    I = len(lines)
    J = len(lines[0])

    for i, line in enumerate(lines):
        numbers = re.findall(r'(\d+)', line)
        j = -1
        for number in numbers:
            j = line.find(number, j + 1)
            l = len(number)
            L = l + (1 if j > 0 else 0) + (1 if j < J else 0)

            previous_line = lines[i-1][max(0, j-1):min(J, j+l+1)] if i > 0 else '.'*L
            number_line = line[max(0, j-1):min(J, j+l+1)]
            next_line = lines[i+1][max(0, j-1):min(J, j+l+1)] if i < J-1 else '.'*L
            dprint(number, i, j, L, previous_line+number_line+next_line)

            if not re.match(r'^[\d|\.]*$', previous_line+number_line+next_line):
                dprint('valid part: %s' % number)
                result += int(number)
            else:
                dprint('invalid part: %s' % number)

    return result

def ex2(data):
    lines = data.split('\n')
    I = len(lines)
    J = len(lines[0])
    gears = dict()
    
    for i in range(I):
        for j in range(J):
            if lines[i][j] == '*':
                gears[(i, j)] = (0, 1)

    for i, line in enumerate(lines):
        numbers = re.findall(r'(\d+)', line)
        j = -1
        for number in numbers:
            j = line.find(number, j + 1)
            l = len(number)
            L = l + (1 if j > 0 else 0) + (1 if j < J else 0)

            rx = range(max(0, i - 1), min(I, i + 2))
            ry = range(max(0, j - 1), min(J, j + l + 1))
            dprint(number, list(rx), list(ry))

            for x in rx:
                for y in ry:
                    if (x,y) in gears:
                        n, v = gears[(x,y)]
                        gears[(x,y)] = (n+1, v*int(number))
                        dprint((x,y), 'in gears: ', gears[(x,y)], number)

    result = 0
    for n, v in gears.values():
        result += v if n == 2 else 0
    return result

assert ex1(load("sample.txt")) == 4361
print("ex1 : %s" % ex1(load("input.txt")))

assert ex2(load("sample.txt")) == 467835
print("ex2 : %s" % ex2(load("input.txt")))