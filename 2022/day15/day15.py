import re
from os import path
from sys import argv

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return [ list(map(int, re.match(r'Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)', line).groups())) for line in open(file_path(file), "r").read().split("\n") ]

def ex1(data, y):
    no_beacon = set()
    for sx, sy, bx, by in data:
        distance = abs(bx-sx) + abs(by-sy)
        n = max(0, 2 * (distance - abs(y-sy)) + 1)
        if n:
            # print("%d pos without beacon at line %d for sensor (%d, %d)" % (n, y, sx, sy))
            for x in range(sx - n//2, sx + n//2 + 1):
                if x not in no_beacon:
                    no_beacon.add(x)

    for sx, sy, bx, by in data:
        if by == y and bx in no_beacon:
            no_beacon.remove(bx)
    # print(no_beacon, len(no_beacon))
    return len(no_beacon)

def matrix_print(m):
    for row in m:
        print("".join(map(str, row)))

debug = False

def manhattan(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

def get_neighbours(line, size):
    sx, sy, bx, by = line
    neighbours = set()
    distance = manhattan(sx, sy, bx, by) + 1
    diffs = [ (x, distance - x) for x in range(1, distance + 1) ]
    
    for x, y in diffs:
        neighbours.add((sx + x, sy + y)) if 0 <= sx + x <= size and 0 <= sy + y <= size else None
        neighbours.add((sx + x, sy - y)) if 0 <= sx + x <= size and 0 <= sy - y <= size else None
        neighbours.add((sx - x, sy + y)) if 0 <= sx - x <= size and 0 <= sy + y <= size else None
        neighbours.add((sx - x, sy - y)) if 0 <= sx - x <= size and 0 <= sy - y <= size else None
    return neighbours

def ex2(data, size):
    for line in data:
        neighbours = get_neighbours(line, size)

        for x, y in neighbours:
            if 0 <= x <= size and 0 <= y <= size:
                for sx, sy, bx, by in data:
                    if manhattan(sx, sy, bx, by) >= manhattan(sx, sy, x, y):
                        break
                else:
                    return 4000000 * x + y

sample = load("sample.txt")
# print(sample)
assert ex1(sample, 10) == 26

data = load("input.txt")
print("ex1 : %s" % ex1(data, 2000000))


assert ex2(sample, 20) == 56000011
print("ex2 : %s" % ex2(data, 4000000))
