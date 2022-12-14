import re
from os import path
from sys import argv
import numpy as np
from collections import defaultdict
import functools

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def myrange(x, y):
    if x <= y:
        return range(x, y + 1)
    else:
        return range(y, x + 1)

def load(file):
    lines = [ list(map(eval, l.split(" -> "))) for l in open(file_path(file), "r").read().split("\n") ]
    minx = lines[0][0][0]
    maxx = lines[0][0][0]
    maxy = lines[0][0][1]
    rocks = set()
    for line in lines:
        for point in line:
            if point[0] < minx:
                minx = point[0]
            if point[0] > maxx:
                maxx = point[0]
            if point[1] > maxy:
                maxy = point[1]
        for i, point in enumerate(line[:-1]):
            for x in myrange(point[0], line[i+1][0]):
                for y in myrange(point[1], line[i+1][1]):
                    rocks.add((x, y))
    return (rocks, minx, maxx, maxy)

debug = False
def dprint(s):
    if debug:
        print(s)

def display(data, sand, current_sand, has_floor = False):
    if not debug:
        return
    rocks, minx, maxx, maxy = data
    if has_floor:
        minx = min(map(lambda p: p[0], rocks.union(sand)))
        maxx = max(map(lambda p: p[0], rocks.union(sand)))
    print("   %d%s%d" % (minx, " " * (maxx-minx-4), maxx))
    for y in range(maxy + 2):
        print("%3d %s" % (y, "".join([ 'o' if (x, y) in sand or (x, y) == current_sand else "#" if (x, y) in rocks else '+' if (x, y) == (500,0) else "." for x in range(minx, maxx + 1) ])))
    if has_floor:
        print("%3d %s" % (y + 1, "".join([ "#" * (maxx - minx + 1) ])))

def can_flow(sand_position, rocks, sand):
    return ((sand_position[0], sand_position[1] + 1) not in rocks and (sand_position[0], sand_position[1] + 1) not in sand) \
        or ((sand_position[0] - 1, sand_position[1] + 1) not in rocks and (sand_position[0] - 1, sand_position[1] + 1) not in sand) \
        or ((sand_position[0] + 1, sand_position[1] + 1) not in rocks and (sand_position[0] + 1, sand_position[1] + 1) not in sand)

source = (500, 0)
def ex1(data):
    sand = set()
    rocks, maxy = [data[i] for i in (0, -1)]
    # display(data, sand) 

    keep_producing = True
    while keep_producing:
        sand_position = source

        while can_flow(sand_position, rocks, sand) and (sand_position[1] < maxy):
            if ((sand_position[0], sand_position[1] + 1) not in rocks and (sand_position[0], sand_position[1] + 1) not in sand):
                sand_position = (sand_position[0], sand_position[1] + 1)
            elif ((sand_position[0] - 1, sand_position[1] + 1) not in rocks and (sand_position[0] - 1, sand_position[1] + 1) not in sand):
                sand_position = (sand_position[0] - 1, sand_position[1] + 1)
            else:
                sand_position = (sand_position[0] + 1, sand_position[1] + 1)

        if (sand_position[1] < maxy):
            sand.add(sand_position)
        # display(data, sand)

        keep_producing = (sand_position[1] < maxy)

    # display(data, sand)
    return len(sand)

def ex2(data):
    sand = set()
    rocks, maxy = [data[i] for i in (0, -1)]
    display(data, sand, None, True) 

    keep_producing = True
    while keep_producing:
        # dprint("production sand particle number %d" % (len(sand) + 1))
        sand_position = source

        while can_flow(sand_position, rocks, sand) and (sand_position[1] < maxy + 1):
            if ((sand_position[0], sand_position[1] + 1) not in rocks and (sand_position[0], sand_position[1] + 1) not in sand):
                sand_position = (sand_position[0], sand_position[1] + 1)
            elif ((sand_position[0] - 1, sand_position[1] + 1) not in rocks and (sand_position[0] - 1, sand_position[1] + 1) not in sand):
                sand_position = (sand_position[0] - 1, sand_position[1] + 1)
            else:
                sand_position = (sand_position[0] + 1, sand_position[1] + 1)
            # display(data, sand, sand_position, True)
        
        if (sand_position[1] < maxy + 2):
            sand.add(sand_position)
        display(data, sand, None, True)

        keep_producing = (sand_position != source)

    return len(sand)

sample1 = load("sample.txt")

assert ex1(sample1) == 24

data = load("input.txt")
print("ex1 : %s" % ex1(data))


assert ex2(sample1) == 93
print("ex2 : %s" % ex2(data))