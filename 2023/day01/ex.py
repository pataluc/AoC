from os import path
from sys import argv

import regex as re

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)


def load(file):
    return open(file_path(file), "r").read().rstrip()

debug = False
def dprint(*s):
    if debug:
        print(*s)

def ex1(data):
    result = 0
    for line in data.split('\n'):
        digits = re.findall(r'([0-9])', line)
        result += int(digits[0] + digits[-1])
    return result

def readDigits(d):
    return d.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4")\
        .replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9")

def ex2(data):
    result = 0
    for line in data.split('\n'):
        digits = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
        result += int(readDigits(digits[0]) + readDigits(digits[-1]))

    return result

assert ex1(load("sample.txt")) == 142
print("ex1 : %s" % ex1(load("input.txt")))

assert ex2(load("sample2.txt")) == 281
print("ex2 : %s" % ex2(load("input.txt")))