from os import path
from sys import argv
import re
from collections import Counter

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return open(file_path(file), "r").read().strip()

debug = False
def dprint(*s):
    if debug:
        print(*s)

def check(room):
    name, sector, checksum = re.match(r'(.*)-([0-9]*)\[(.*)\]', room).groups()

    keys = list(map(lambda x: x[0], sorted(Counter(name.replace('-', '')).most_common(), key= lambda x: str(100-int(x[1])) + x[0])))[:5]
    return int(sector) if checksum == ''.join(keys) else 0

def ex1(data):
    for room in data.split('\n'):
        name, sector, checksum = re.match(r'(.*)-([0-9]*)\[(.*)\]', room).groups()

        r = check(room)
        # if r > 0:
        # dprint(name, sector, checksum)
        dprint(room)
        for c in checksum:
            dprint("%s: %d" % (c, name.count(c)))
        dprint(r)
        # print(name, sector)
    return sum([check(room) for room in data.split('\n')])

def rot(char, n):
    if char == '-':
        return ' '
    else:
        return chr((ord(char) - 97 + n) % 26 + 97)

def ex2(data):
    for room in data.split('\n'):
        name, sector, checksum = re.match(r'(.*)-([0-9]*)\[(.*)\]', room).groups()
        if check(room):
            print(sector, ''.join(map(lambda x: rot(x, int(sector)), name)))
    return 0

assert check("aaaaa-bbb-z-y-x-123[abxyz]") == 123
assert check("a-b-c-d-e-f-g-h-987[abcde]") == 987
assert check("not-a-real-room-404[oarel]") == 404
assert check("totally-real-room-200[decoy]") == 0
assert ex1(load("sample.txt")) == 1514
# debug=True

print("ex1 : %s" % ex1(load("input.txt")))
print("ex2 : %s" % ex2(load("input.txt")))