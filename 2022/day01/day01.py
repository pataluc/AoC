from os import path
from sys import argv

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    input = list(map(lambda x: [int(n) for n in x.split("\n")], open(file_path(file), "r").read().split("\n\n")))

    return input

def solve(calories, count):
    return sum(sorted(map(sum, calories), reverse=True)[:count])

def ex1(calories):
    return solve(calories, 1)

def ex2(calories):
    return solve(calories, 3)


calories = load("sample.txt")
assert ex1(calories) == 24000
assert ex2(calories) == 45000

calories = load("input.txt")
print("ex1 : %d" % ex1(calories))
print("ex2 : %d" % ex2(calories))