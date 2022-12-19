from collections import deque
import re
from os import path
from sys import argv

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return [ tuple(map(int, line.split(','))) for line in open(file_path(file), "r").read().split("\n") ]

def manhattan2(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + abs(p1[2]-p2[2])

debug = True
def ex1(data):
    score = len(data) * 6
    for cube1 in data:
        for cube2 in data:
            if cube1 != cube2 and manhattan2(cube1, cube2) == 1:
                score -= 1

    return score

def flood_fill(start_c: tuple, air_c: dict):
    # Goes thru all cubes in air_c connected to start_c and "fills" them
    # Unfilled cubes are False, filled cubes are True

    queue = deque()
    # initialize queue with start coordinate
    queue.append(start_c)

    while queue:
        # Pull from the front of the queue
        coord = queue.popleft()
        # Set it to filled
        air_c[coord] = True
        # Find all its unfilled, non-lava neighbors and add to queue
        cx, cy, cz = coord
        directions = [(cx - 1, cy, cz), (cx + 1, cy, cz), (cx, cy + 1, cz),
                      (cx, cy - 1, cz), (cx, cy, cz + 1), (cx, cy, cz - 1)]

        for d in directions:
            if d in air_c and not air_c[d] and d not in queue:
                queue.append(d)
    return air_c


def ex2(data):
    score = len(data) * 6
    minx = maxx = 0
    miny = maxy = 0
    minz = maxz = 0
    for cube1 in data:
        minx = min(minx, cube1[0])
        miny = min(miny, cube1[1])
        minz = min(minz, cube1[2])
        maxx = max(maxx, cube1[0])
        maxy = max(maxy, cube1[1])
        maxz = max(maxz, cube1[2])
        for cube2 in data:
            if cube1 != cube2 and manhattan2(cube1, cube2) == 1:
                score -= 1
    air_cubes = {}

    for x in range(minx - 1, maxx + 2):
        for y in range(miny - 1, maxy + 2):
            for z in range(minz - 1, maxz + 2):
                if (x, y, z) not in data :
                    air_cubes[(x,y,z)] = False

    air_cubes = flood_fill((-1,-1,-1), air_cubes)
    # print(air_cubes)


                    # and (x + 1, y, z) in data \
                    # and (x - 1, y, z) in data \
                    # and (x, y + 1, z) in data \
                    # and (x, y - 1, z) in data \
                    # and (x, y, z + 1) in data \
                    # and (x, y, z - 1) in data:
                    # score -= 6
    return score - ex1([cube for cube in air_cubes if air_cubes[cube] is False])

sample = load("sample.txt")
# print(sample)
assert ex1([(1,1,1), (2,1,1)]) == 10
assert ex1(sample) == 64

data = load("input.txt")
print("ex1 : %s" % ex1(data))


assert ex2(sample) == 58
print("ex2 : %s" % ex2(data))
