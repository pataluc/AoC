import re
from os import path
from sys import argv

import numpy as np

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

class Monkey:
    items = None
    divider = None
    operation = None
    test_true = test_false = None
    items_inspected = 0
    
    def __init__(self, items, operation, divider, test_true, test_false):
        self.items = items
        self.operation = operation
        self.divider = divider
        self.test_true, self.test_false = test_true, test_false

    def test(self, value):
        return (value % divider) == 0

    def apply_operation(self, old):
        self.items_inspected += 1
        return eval(self.operation)

    def pop0_and_apply(self):
        return self.apply_operation(self.items.pop())

    def add_item(self, worry_level):
        self.items.append(worry_level)

def load(file):
    monkeys = []
    for m in list(open(file_path(file), "r").read().split("\n\n")):
        m = m.split("\n")
        monkeys.append(Monkey(list(map(int, (m[1][18:]).split(", "))), m[2][19:], int(m[3][21:]), int(m[4][28:]), int(m[5][29:])))
    return monkeys

debug = False
def dprint(s):
    if debug:
        print(s)


def round(monkeys, divides = 3):
    for i, monkey in enumerate(monkeys):
        dprint("Monkey %d:" % i)
        while len(monkey.items):
            item = monkey.items.pop()
            dprint("  Monkey inspects an item with a worry level of %d." % item)
            worry_level = monkey.apply_operation(item)
            dprint("    Worry level is multiplied by %s to %d." % (monkey.operation, worry_level))
            if divides ==3:
                worry_level = worry_level // divides
                dprint("    Monkey gets bored with item. Worry level is divided by %d to %d." % (divides, worry_level))
            else:
                worry_level = worry_level % divides

            if not(worry_level % monkey.divider):
                dprint("    Current worry level is divisible by %d." % monkey.divider)
                dprint("    Item with worry level %d is thrown to monkey %d." % (worry_level, monkey.test_true))
                monkeys[monkey.test_true].add_item(worry_level)
            else:
                dprint("    Current worry level is not divisible by %d." % monkey.divider)
                dprint("    Item with worry level %d is thrown to monkey %d." % (worry_level, monkey.test_false))
                monkeys[monkey.test_false].add_item(worry_level)

def ex1(monkeys):
    for i in range(20):
        round(monkeys)
    inspected = list(map(lambda x: x.items_inspected, monkeys))
    inspected.sort()
    return np.prod(inspected[-2:])

def ex2(monkeys):
    lcm = np.lcm.reduce(list(map(lambda x: x.divider, monkeys)))
    for i in range(10000):
        round(monkeys, lcm)
    inspected = list(map(lambda x: x.items_inspected, monkeys))
    inspected.sort()
    return np.prod(inspected[-2:])

sample1 = load("sample.txt")
# print(sample1)
# ex1(sample1)
# exit()
assert ex1(sample1) == 10605

data = load("input.txt")
print("ex1 : %s" % ex1(data))

sample1 = load("sample.txt")
data = load("input.txt")
assert ex2(sample1) == 2713310158
print("ex2 : %s" % ex2(data))