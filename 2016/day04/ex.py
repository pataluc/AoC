from os import path
from sys import argv
import re
import numpy as np

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return open(file_path(file), "r").read().strip()

debug = True
def dprint(s):
    if debug:
        print(s)

def check(room):
    name, sector, checksum = re.match(r'(.*)-([0-9]*)\[(.*)\]', room).groups()

    for i in range(len(checksum) - 1):
        if name.count(checksum[i]) < name.count(checksum[i + 1]) \
            or (name.count(checksum[i]) == name.count(checksum[i + 1]) and checksum[i] > checksum[i + 1]):
            return 0
    return int(sector)

def ex1(data):
    for room in data.split('\n'):
        name, sector, checksum = re.match(r'(.*)-([0-9]*)\[(.*)\]', room).groups()

        r = check(room)
        if r > 0:
            print(name, sector, checksum)
            for c in checksum:
                print("%s: %d" % (c, name.count(c)))
            print(r)
    return sum([check(room) for room in data.split('\n')])


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

# assert check("aaaaa-bbb-z-y-x-123[abxyz]") == 123
# assert check("a-b-c-d-e-f-g-h-987[abcde]") == 987
# assert check("not-a-real-room-404[oarel]") == 404
# assert check("totally-real-room-200[decoy]") == 0
# assert ex1(load("sample.txt")) == 1514

print("ex1 : %s" % ex1(load("input.txt")))
# print("ex2 : %s" % ex2(load("input.txt")))