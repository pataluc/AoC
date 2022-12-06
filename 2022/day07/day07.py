import re
from os import path
from sys import argv

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    raw_stacks, moves = list(map(lambda s: s.split("\n"), open(file_path(file), "r").read().split("\n\n")))

    stacks = [""] * ((len(raw_stacks[0]) + 1) // 4)
    
    for stack_line in raw_stacks[::-1][1::]:
        for i in range(len(stacks)):
            c = stack_line[4*i + 1]
            if c != ' ':
                stacks[i] += c

    moves = [list(map(int, re.search('move ([0-9]+) from ([0-9]+) to ([0-9]+)', move).groups())) for move in moves]
    return stacks, moves


def ex1(stacks, moves):
    for nb_char, stack_from, stack_to in moves:
        stack_to -= 1
        stack_from -= 1
        stacks[stack_to] += stacks[stack_from][-1*nb_char:][::-1]
        stacks[stack_from] = stacks[stack_from][:-1*nb_char]
    return "".join(list(map(lambda s: s[-1], stacks)))

def ex2(stacks, moves):
    for nb_char, stack_from, stack_to in moves:
        stack_to -= 1
        stack_from -= 1
        stacks[stack_to] += stacks[stack_from][-1*nb_char:]
        stacks[stack_from] = stacks[stack_from][:-1*nb_char]
    return "".join(list(map(lambda s: s[-1], stacks)))

sample_stacks, sample_moves = load("sample.txt")
assert ex1(sample_stacks.copy(), sample_moves) == "CMZ"

stacks, moves = load("input.txt")
print("ex1 : %s" % ex1(stacks.copy(), moves))

assert ex2(sample_stacks, sample_moves) == "MCD"
print("ex2 : %s" % ex2(stacks, moves))