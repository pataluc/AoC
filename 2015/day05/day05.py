import re
from os import path
from sys import argv
import numpy as np
from collections import defaultdict
import functools

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return open(file_path(file), "r").read().split("\n")

def is_nice(string):
    return len(list(filter(lambda x: x in ['a', 'e', 'i', 'o', 'u'], string))) >= 3 \
        and any([ string[x] == string[x+1] for x in range(len(string) - 1) ]) \
        and "ab" not in string \
        and "cd" not in string \
        and "pq" not in string \
        and "xy" not in string

def is_nice2(string):
    regex1 = r'([a-z][a-z]).*\1'
    regex2 = r'([a-z]).\1'
    return bool(re.search(regex1, string) and re.search(regex2, string))

def ex1(data):
    return len(list(filter(is_nice, data)))

def ex2(data):
    return len(list(filter(is_nice2, data)))

assert is_nice("ugknbfddgicrmopn") == True
assert is_nice("aaa") == True
assert is_nice("aei") == False
assert is_nice("jchzalrnumimnmhp") == False
assert is_nice("haegwjzuvuyypxyu") == False
assert is_nice("dvszwmarrgswjxmb") == False

data = load("input.txt")
print("ex1 : %s" % ex1(data))


assert is_nice2("qjhvhtzxzqqjkmpb") == True
assert is_nice2("xxyxx") == True
assert is_nice2("uurcxstgmygtbstg") == False
assert is_nice2("ieodomkazucvgmuy") == False

print("ex2 : %s" % ex2(data))