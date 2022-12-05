from os import path
from sys import argv

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    data = list(map(list, open(file_path(file), "r").read().split("\n")))
    return data

def my_ord(letter):
    if ord(letter) > 96:
        return ord(letter) - 96
    else:
        return ord(letter) - 38

def ex1(data):
    score = 0
    for line in data:
        firstpart, secondpart = set(line[:len(line)//2]), set(line[len(line)//2:])
        
        score += my_ord(set.intersection(firstpart, secondpart[0])
    return score

def ex2(data):
    score = 0
    for i in range(len(data) // 3):
        intersection = [l for l in data[3*i] if l in data[3*i + 1] and l in data[3*i + 2]]
        score += my_ord(intersection[0])
    return score

data = load("sample.txt")
assert ex1(data) == 157
assert ex2(data) == 70

data = load("input.txt")
print("ex1 : %d" % ex1(data))
print("ex2 : %d" % ex2(data))