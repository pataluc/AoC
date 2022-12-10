import re
from os import path
from sys import argv
import numpy as np
from yachalk import chalk

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return [list(map(int, list(l))) for l in open(file_path(file), "r").read().split("\n")]

def ex1(data):
    visible = len(data[0]) * 2 + (len(data)-2)*2
    for j in range(1, len(data) - 1):
        for i in range(1, len(data[0]) - 1):
            if all(map(lambda x: x < data[j][i], data[j][0:i])) or \
                all(map(lambda x: x < data[j][i], data[j][i+1:len(data[0])])) \
                or all(map(lambda x: x < data[j][i], list(map(lambda x: x[i], data[:j])))) \
                or all(map(lambda x: x < data[j][i], list(map(lambda x: x[i], data[j+1:])))):
                visible += 1
    return visible

def cprint(lines, m, n):
    for j in range(len(lines)):
        for i in range(len(lines[0])):
            if m == i and n == j:
                print(chalk.red(lines[j][i]), end="")
            else:
                print(lines[j][i], end="")
        print("")


def view(data, current_tree, direction):
    trees_viewed = 0
    i, j = current_tree
    tree_height = data[j][i]
    
    while True:
        i += direction[0]
        j += direction[1]
        if not(0 <= i < len(data[0])) or not(0 <= j < len(data)) :
            break
        trees_viewed += 1

        if data[j][i] >= tree_height:
            break
    return trees_viewed


def ex2(data):
    highscore = 0
    for j in range(0, len(data)):
        for i in range(0, len(data[0])):
            score = view(data, (i, j), (0, -1))*view(data, (i, j), (-1, 0))*view(data, (i, j), (1, 0))*view(data, (i, j), (0, 1))
            if score > highscore:
                highscore = score
    return highscore

sample_data = load("sample.txt")
assert ex1(sample_data) == 21

data = load("input.txt")
print("ex1 : %s" % ex1(data))

assert ex2(sample_data) == 8
print("ex2 : %s" % ex2(data))