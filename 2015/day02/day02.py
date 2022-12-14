from os import path
from sys import argv
import numpy as np

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)


def load(file):
    return [ list(map(int, l.split("x"))) for l in open(file_path(file), "r").read().split("\n") ]

debug = False
def dprint(s):
    if debug:
        print(s)

def paper_size(s):
    l, w, h = s
    return min(l*w, w*h, h*l) + 2 * (l*w + w*h + h*l)

def ribbon_length(s):
    l, w, h = s
    return np.prod(sorted([2*(l+w), 2*(w+h), 2*(h+l)])[:1]) + l*w*h



def ex1(data):
    # print(list(map(lambda gift: (gift, paper_size(gift)), data)))
    return sum(map(paper_size, data))
    

def ex2(data):
    return sum(map(ribbon_length, data))

assert paper_size([2,3,4]) == 58
assert paper_size([1,1,10]) == 43

assert ribbon_length([2,3,4]) == 34
assert ribbon_length([1,1,10]) == 14

data = load("input.txt")
print("ex1 : %s" % ex1(data))
print("ex2 : %s" % ex2(data))