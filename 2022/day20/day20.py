import re
from os import path
from sys import argv
from collections import deque

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return list(map(int, open(file_path(file), "r").read().split("\n")))

def myrange(x, y):
    if x <= y:
        return range(x, y + 1)
    else:
        return range(y, x + 1)

debug = False

class chain_link:
    value = None
    ofset = None
    previous = None
    next = None

    def __init__(self, value, chain_length):
        self.value = value
        self.ofset = value if abs(value) < chain_length else (value // abs(value)) * (abs(value) % (chain_length - 1))
    
    def __repr__(self):
        return "%d (previous: %d, next: %d)" % (self.value, self.previous.value, self.next.value)

    def get_ofseted_link(self):
        current = self
        if self.value > 0:
            for _ in range(abs(self.ofset)):
                current = current.next
        elif self.value < 0:
            for _ in range(abs(self.ofset)):
                current = current.previous
            current = current.previous
        return current

    def print(self):
        current = self
        r = ""
        while current.next != self:
            r += "%d, " % current.value
            current = current.next
        print("%s%d" % (r, current.value))

    def dprint(self):
        current = self
        r = ""
        while current.next != self:
            r += "%d, " % current
            current = current.next
        print("%s%d" % (r, current))

def ex1(data):
    l = len(data)
    links = [ chain_link(v, l) for v in data ]
    
    for i, link in enumerate(links):
        link.previous = links[(i - 1) % l]
        link.next = links[(i + 1) % l]
    
    first = links[0]
    print("Initial arrangement:") if debug else None
    first.print() if debug else None
    # first.dprint()
    print("") if debug else None

    for link in links:
        if link.value != 0:
            # décalage du premier si nécessaire
            if first == link:
                first = link.next
            
            # on déchaine
            link.previous.next = link.next
            link.next.previous = link.previous

            target = link.get_ofseted_link()
            print("%d moves between %d and %d:" % (link.value, target.value, target.next.value)) if debug else None

            # on insère
            link.next = target.next
            link.previous = target
            target.next = link
            link.next.previous = link
            # first.dprint()
        else:
            print("0 does not move:") if debug else None
        first.print() if debug else None
        print("") if debug else None

    score = 0
    current = first
    # searching 0
    while current.value != 0:
        current = current.next
    # current.print()


    for i in range(1000):
        current = current.next
    score += current.value
    # print(current)
    for i in range(1000):
        current = current.next
    score += current.value
    # print(current)
    for i in range(1000):
        current = current.next
    score += current.value
    # print(current)


    return score

key=811589153

def ex2(data):
    l = len(data)
    links = [ chain_link(v * key, l) for v in data ]
    
    for i, link in enumerate(links):
        link.previous = links[(i - 1) % l]
        link.next = links[(i + 1) % l]
    first = links[0]
    print("Initial arrangement:") if debug else None
    first.print() if debug else None
    # first.dprint()
    print("") if debug else None

    for i in range(10):
        for link in links:
            if link.value != 0:
                # décalage du premier si nécessaire
                if first == link:
                    first = link.next
                
                # on déchaine
                link.previous.next = link.next
                link.next.previous = link.previous

                target = link.get_ofseted_link()
                print("%d moves between %d and %d: (%d)" % (link.value, target.value, target.next.value, link.value % len(links))) if debug else None

                # on insère
                link.next = target.next
                link.previous = target
                target.next = link
                link.next.previous = link
                # first.dprint()
            else:
                print("0 does not move:") if debug else None
            first.print() if debug else None
            print("") if debug else None

    score = 0
    current = first
    # searching 0
    while current.value != 0:
        current = current.next
    # current.print()


    for i in range(1000):
        current = current.next
    score += current.value
    # print(current)
    for i in range(1000):
        current = current.next
    score += current.value
    # print(current)
    for i in range(1000):
        current = current.next
    score += current.value
    # print(current)


    return score

sample = [1, 2, -3, 3, -2, 0, 4]
# print(sample)
assert ex1(sample) == 3
data = load("input.txt")
print("ex1 : %s" % ex1(data))

assert ex2(sample) == 1623178306
print("ex2 : %s" % ex2(data))
