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

def ex1(data):
    lines = data.split('\n')

    return ''.join([Counter(list(map(lambda x: x[i], lines))).most_common(1)[0][0] for i in range(len(lines[0]))])


def ex2(data):
    lines = data.split('\n')

    return ''.join([Counter(list(map(lambda x: x[i], lines))).most_common()[-1][0] for i in range(len(lines[0]))])

assert ex1(load("sample.txt")) == 'easter'
# debug=True

print("ex1 : %s" % ex1(load("input.txt")))
assert ex2(load("sample.txt")) == 'advent'
print("ex2 : %s" % ex2(load("input.txt")))