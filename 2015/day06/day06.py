from os import path
from sys import argv
import re


def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return [ re.match(r'(.*) ([0-9]{1,3},[0-9]{1,3}) through ([0-9]{1,3},[0-9]{1,3})', line) for line in open(file_path(file), "r").read().split("\n") ]

def ex1(data):
    on = set()
    for instruction in data:
        verb, p1, p2 = instruction[1], eval(instruction[2]), eval(instruction[3])
        for i in range(p1[0], p2[0] + 1):
            for j in range(p1[1], p2[1] + 1):
                if verb == 'turn on':
                    on.add((i, j))
                elif verb == 'turn off' and (i, j) in on:
                    on.remove((i, j))
                elif verb == 'toggle':
                    if (i, j) in on:
                        on.remove((i, j))
                    else:
                        on.add((i, j))
        # print("%s for " % verb, p1, "to", p2, " -> on: %d" % len(on))

    return len(on)

def ex2(data):
    on = dict()
    for instruction in data:
        verb, p1, p2 = instruction[1], eval(instruction[2]), eval(instruction[3])
        for i in range(p1[0], p2[0] + 1):
            for j in range(p1[1], p2[1] + 1):
                if verb == 'turn on':
                    if (i, j) not in on:
                        on[(i, j)] = 1
                    else:
                        on[(i, j)] += 1
                elif verb == 'turn off' and (i, j) in on:
                    if on[(i, j)] == 1:
                        on.pop((i, j))
                    else:
                        on[(i, j)] -= 1
                elif verb == 'toggle':
                    if (i, j) not in on:
                        on[(i, j)] = 2
                    else:
                        on[(i, j)] += 2
        # print("%s for " % verb, p1, "to", p2, " -> on: %d" % len(on))

    return sum(on.values())

sample = load("sample.txt")
assert ex1(sample) == 1000000 - 1000 - 4

data = load("input.txt")
print("ex1 : %s" % ex1(data))

print("ex2 : %s" % ex2(data))