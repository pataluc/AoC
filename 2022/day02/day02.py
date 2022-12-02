from os import path
from sys import argv

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    data = list(map(lambda x: x.split(" "), open(file_path(file), "r").read().split("\n")))
    return data

orderABC = ['A', 'B', 'C']
orderXYZ = ['X', 'Y', 'Z']

def score_round(roundd, order1, order2):
    elf, me = roundd
    # score my play
    score = order2.index(me) + 1
    # draw
    if order1.index(elf) == order2.index(me):
        score += 3
    # win
    elif ((order1.index(elf) + 1) % 3) == order2.index(me):
        score += 6
    return score

def ex1(data):
    return sum([score_round(r, orderABC, orderXYZ) for r in data])

def ex2(data):
    my_plays = [[elf, orderABC[(orderABC.index(elf) + orderXYZ.index(result) - 1) % 3]] for [elf, result] in data]
    return sum([score_round(r, orderABC, orderABC) for r in my_plays])


data = load("sample.txt")
assert ex1(data) == 15
assert ex2(data) == 12

data = load("input.txt")
print("ex1 : %d" % ex1(data))

print("ex2 : %d" % ex2(data))