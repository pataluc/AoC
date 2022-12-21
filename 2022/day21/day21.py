import re
from os import path
from sys import argv
from collections import deque

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    data = dict()
    for line in open(file_path(file), "r").read().split("\n"):
        i, j = line.split(': ')
        data[i] = j if ' ' in j else int(j)
    return data

debug = False

def solve(data, term):
    if term not in data:
        return term
    elif isinstance(data[term], int):
        return data[term]
    else:
        m, op, n = data[term].split(' ')
        return "(%s %s %s)" % (solve(data, m), op, solve(data, n))

def ex1(data):
    op = solve(data, 'root')
    # print(op)
    return int(eval(op))

def ex2(data: dict):

    data.pop('humn')

    m, _, n = data['root'].split(' ')
    eq1, eq2 = solve(data, m), solve(data, n)
    to_solve = value = None
    if 'humn' in eq1:
        to_solve, value = eq1, int(eval(eq2))
    else:
        to_solve, value = eq2, int(eval(eq1))
    
    while True:
        groups = re.findall(r'\(\d+ . \d+\)', to_solve)
        if groups:
            for g in groups:
                to_solve = to_solve.replace(g, str(int(eval(g))))
        else:
            break
    
    while True:
        # print(to_solve, ' = ', value)
        searchleft = re.search(r'^\((.*) (.) (\d+)\)$', to_solve)
        searchright = re.search(r'^\((\d+) (.) (.*)\)$', to_solve)
        if searchleft:
            left, op, right = searchleft.groups()
            if op == '+':
                value -= int(right)
            elif op == '/':
                value *= int(right)
            elif op == '*':
                value = value // int(right)
            elif op == '-':
                value += int(right)
            to_solve = left
        elif searchright:
            left, op, right = searchright.groups()
            if op == '+':
                value -= int(left)
            elif op == '/':
                value *= int(left)
            elif op == '*':
                value = value // int(left)
            elif op == '-':
                value = -1 * (value - int(left))
            to_solve = right
        else:
            return value

sample = load("sample.txt")
# print(sample)
assert ex1(sample.copy()) == 152
data = load("input.txt")
print("ex1 : %s" % ex1(data.copy()))

assert ex2(sample) == 301
print("ex2 : %s" % ex2(data))
