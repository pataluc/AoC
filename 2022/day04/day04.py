from os import path
from sys import argv

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    data = list(open(file_path(file), "r").read().split("\n"))
    #[tuple(int(x) for assignment in row.split(',')
    #          for x in assignment.split('-')) for row in f.readlines()]
    return data

def range_in_range(r, s):
    return all(map(lambda x: x in s, r))

def range_in_part_of_range(r, s):
    return any(map(lambda x: x in s, r))

def ex1(data):
    answer = 0
    for l in data:
        elf1, elf2 = l.split(",")
        elf1min, elf1max = map(int, elf1.split("-"))
        r1 = range(elf1min, elf1max + 1)
        elf2min, elf2max = map(int, elf2.split("-"))
        r2 = range(elf2min, elf2max + 1)
        if range_in_range(r1, r2) or range_in_range(r2, r1):
            answer += 1
    return answer

def ex2(data):
    answer = 0
    for l in data:
        elf1, elf2 = l.split(",")
        elf1min, elf1max = map(int, elf1.split("-"))
        r1 = range(elf1min, elf1max + 1)
        elf2min, elf2max = map(int, elf2.split("-"))
        r2 = range(elf2min, elf2max + 1)
        if range_in_part_of_range(r1, r2):
            answer += 1
    return answer

data = load("sample.txt")
assert ex1(data) == 2
assert ex2(data) == 4

data = load("input.txt")
print("ex1 : %d" % ex1(data))
print("ex2 : %d" % ex2(data))