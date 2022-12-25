import re
from os import path
from sys import argv

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return open(file_path(file), "r").read().split("\n")

debug = False

def to_int(t):
    result = 0
    for i, number in enumerate(t):
        result += number * 5 ** i
    return result

def simplify(t):
    for i in range(len(t)):
        m = t[i] // 5
        t[i] = t[i] % 5
        if t[i] >= 3:
            t[i] = t[i] - 5
            m += 1
        if m:
            t[i + 1] += m
    return t

def to_snafu(t):
    t = simplify(t)
    result = ''
    for i in range(len(t)):
        if t[i] == -2:
            result = '=%s' % result
        elif t[i] == -1:
            result = '-%s' % result
        else:
            result = '%s%s' % (str(t[i]), result)
    result = re.sub(r'^0*', '', result)
    return result
    

def ex1(data):
    number = [0] * 30
    for line in data:
        for i in range(len(line)):
            if line[-1 * i - 1] == '=':
                number[i] += -2
            elif line[-1 * i - 1] == '-':
                number[i] += -1
            else:
                number[i] += int(line[-1 * i - 1])
    number = simplify(number)
    return to_snafu(number)

sample2 = load("sample.txt")
assert ex1(sample2) == '2=-1=0'

data = load("input.txt")
print("ex1 : %s" % ex1(data))