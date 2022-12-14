import re
from os import path
from sys import argv
import numpy as np
from collections import defaultdict
import functools

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return [ list(map(eval, l.split("\n"))) for l in open(file_path(file), "r").read().split("\n\n") ]

def load2(file):
    return [ eval(l) for l in open(file_path(file), "r").read().split("\n") if l != '' ] + [[[2]]] + [[[6]]]

debug = False

def compare(l, m, prefix = ""):
    # listes non vide
    if len(l) and len(m):
        i = 0
        while i < min(len(l), len(m)):
            n, o = l[i], m[i]
            print("  %s- Compare" % prefix, n, "vs", o) if debug else None
            if isinstance(n, int) and isinstance(o, int):
                if n < o:
                    print("    %s- Left side is smaller, so inputs are in the right order" % prefix) if debug else None
                    return -1
                elif n > o:
                    print("    %s- Right side is smaller, so inputs are not in the right order" % prefix) if debug else None
                    return 1
            elif isinstance(n, list) and isinstance(o, list):
                if len(n) and len(o):
                    r = compare(n, o, prefix + "  ")
                    if r != 0:
                        return r
                elif len(o):
                    print("    %s- Left side ran out of items, so inputs are in the right order" % prefix) if debug else None
                    return -1
                elif len(n):
                    print("    %s- Right side ran out of items, so inputs are not in the right order" % prefix) if debug else None
                    return 1
            elif isinstance(n, list):
                print("    %s- Mixed types; convert right to [%d] and retry comparison" % (prefix, o)) if debug else None
                print("    %s- Compare" % prefix, n, "vs", [o]) if debug else None
                r = compare(n, [o], prefix + "    ")
                if r != 0:
                    return r
            elif isinstance(o, list):
                print("    %s- Mixed types; convert left to [%d] and retry comparison" % (prefix, n)) if debug else None
                print("    %s- Compare" % prefix, [n], "vs", o) if debug else None
                r = compare([n], o, prefix + "    ")
                if r != 0:
                    return r
            i += 1

        if i == len(l) and i < len(m):
            print("  %s- Left side ran out of items, so inputs are in the right order" % prefix) if debug else None
            return -1
        elif i < len(l) and i == len(m):
            print("  %s- Right side ran out of items, so inputs are not in the right order" % prefix) if debug else None
            return 1

    elif len(m):
        print("  %s- Left side ran out of items, so inputs are in the right order" % prefix) if debug else None
        return -1
    elif len(l):
        print("  %s- Right side ran out of items, so inputs are not in the right order" % prefix) if debug else None
        return 1
    return 0

def ex1(pairs):
    score = 0
    ok_pairs = []
    for i, [l, m] in enumerate(pairs):
        print("== Pair %d ==" % (i + 1)) if debug else None
        print("- Compare", l, "vs", m) if debug else None

        if compare(l, m) < 0:
            print("Pair %d is OK") if debug else None
            score += (i + 1)
            ok_pairs.append(i + 1)
        print("") if debug else None
    return score



def ex2(pairs):
    pairs = sorted(pairs, key=functools.cmp_to_key(compare))

    return (pairs.index([[2]]) + 1) * (pairs.index([[6]]) + 1)

sample1 = load("sample.txt")

# print(compare([1,1,3,1,1], [1,1,5,1,1]))
# exit()
# print(sample1)
assert ex1(sample1) == 13

data = load("input.txt")
print("ex1 : %s" % ex1(data))


sample1 = load2("sample.txt")
data = load2("input.txt")

assert ex2(sample1) == 140
print("ex2 : %s" % ex2(data))