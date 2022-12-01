from os import path
from sys import argv

def load(file):
    input = list(map(lambda x: [int(n) for n in x.split("\n")], open(file, "r").read().split("\n\n")))

    return input

def ex1(calories):
    return max(map(sum, calories))

def ex2(calories):
    return sum(sorted(map(sum, calories))[-3:])


calories = load("%s/sample.txt" % (path.dirname(argv[0]) if path.dirname(argv[0]) else "."))
r = ex1(calories)
assert r == 24000
r = ex2(calories)
assert r == 45000

calories = load("%s/input.txt" % (path.dirname(argv[0]) if path.dirname(argv[0]) else "."))
r = ex1(calories)
print("ex1 : %d" % r)
r = ex2(calories)
print("ex2 : %d" % r)