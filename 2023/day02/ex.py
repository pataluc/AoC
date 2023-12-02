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
    for game in data.split('\n'):
        id, sets = re.match(r'Game (\d*): (.*)', game).groups()
        sets = sets.replace(',', ';').split('; ')
        dprint(sets)

        ok = True
        for set in sets:
            nb, color = set.split(' ')
            nb = int(nb)
            # dprint(nb, color)
            if (color == 'red' and nb > 12) or \
                (color == 'green' and nb > 13) or \
                (color == 'blue' and nb > 14):
                dprint("%s is KO in set %s" % (color, set))
                ok = False
        if ok:
            result += int(id)
    
    return result

def ex2(data):
    result = 0
    for game in data.split('\n'):
        id, sets = re.match(r'Game (\d*): (.*)', game).groups()
        sets = sets.replace(',', ';').split('; ')

        dprint(sets)
        r, g, b = 0, 0, 0

        for set in sets:
            nb, color = set.split(' ')
            nb = int(nb)

            if color == 'red' and nb > r:
                r = nb
            if color == 'green' and nb > g:
                g = nb
            if color == 'blue' and nb > b:
                b = nb
        result += r*g*b
    
    return result

assert ex1(load("sample.txt")) == 8
print("ex1 : %s" % ex1(load("input.txt")))

assert ex2(load("sample.txt")) == 2286
print("ex2 : %s" % ex2(load("input.txt")))