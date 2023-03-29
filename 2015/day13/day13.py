import re
from os import path
from sys import argv
import numpy as np

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    groups = re.findall(r'(.*) would (.*) happiness units by sitting next to (.*)\.', open(file_path(file), "r").read(), flags=re.M)
    matrix = dict()
    for person in {group[0] for group in groups}:
        matrix[person] = dict()
    for p1, gain, p2 in groups:
        matrix[p1][p2] = int(gain.replace("gain ", "").replace("lose ", "-"))

    return matrix

debug = False

def happiness(data, order):
    splitted_order = order.split("-")
    return sum([data[person][splitted_order[(i+1) % len(splitted_order)]] + data[splitted_order[(i+1) % len(splitted_order)]][person] for i, person in enumerate(splitted_order)])


def solve(data):
    orders = set()
    persons = list(data.keys())
    first = persons[0]
    
    result = 0
    
    while len(orders) < np.math.factorial(len(persons) - 1):
        np.random.shuffle(persons)
        order = '-'.join(persons)
        if order not in orders and order.split("-")[0] == first:
            orders.add(order)
            result = max(result, happiness(data, order))
    return result

sample = load("sample.txt")
# print(sample)
assert solve(sample) == 330

data = load("input.txt")
print("ex1 : %s" % solve(data))

data['me'] = dict()
for person in list(data.keys()):
    data[person]['me'] = 0
    data['me'][person] = 0

print("ex2 : %s" % solve(data))