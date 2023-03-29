import re
from os import path
from sys import argv
import numpy as np

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    points = set()
    for j, line in enumerate(open(file_path(file), "r").read().split("\n")):
        for i, c in enumerate(line):
            if c == '#':
                points.add((i,j))
                
    return points

debug = False

directions = {
    'N': [(-1,-1), (0,-1), (1,-1)],
    'S': [(-1,1), (0,1), (1,1)],
    'W': [(-1,-1), (-1,0), (-1,1)],
    'E': [(1,-1), (1,0), (1,1)]
}

all_adjacents = [
    (-1,-1), (0,-1), (1,-1),
    (-1,0), (1,0),
    (-1,1), (0,1), (1,1),
]

def print_points(points):
    minx = miny = maxx = maxy = 0
    for point in points:
        minx = min(minx, point[0])
        miny = min(miny, point[1])
        maxx = max(maxx, point[0])
        maxy = max(maxy, point[1])

    minx, maxx, miny, maxy = -3,10, -2,9
    for j in range(miny, maxy + 1):
        print("".join([ '#' if (i, j) in points else '.' for i in range(minx, maxx + 1) ]))

def compute_score(points):
    minx = miny = maxx = maxy = 0
    for point in points:
        minx = min(minx, point[0])
        miny = min(miny, point[1])
        maxx = max(maxx, point[0])
        maxy = max(maxy, point[1])
    return (maxx - minx + 1) * (maxy - miny + 1) - len(points)

def ex1(data: set):
    print("== Initial State ==") if debug else None
    print_points(data) if debug else None

    directions_order = ['N', 'S', 'W', 'E']

    for i in range(10):
        movements = dict()
        # print("directions order: %s" % " ".join(directions_order))
        for point in data:
            # si tous les points autour ne sont pas vides
            # print(point, all([ tuple(np.array(point) + d) not in data for d in all_adjacents ]))
            if any([ tuple(np.array(point) + d) in data for d in all_adjacents ]):
                for dir in directions_order:
                    if all([ tuple(np.array(point) + d) not in data for d in directions[dir] ]):
                        # movement to target already there:
                        target = tuple(np.array(point) + directions[dir][1])
                        if target in movements:
                            movements.pop(target)
                        else:
                            movements[tuple(np.array(point) + directions[dir][1])] = point
                        break
        
        for target, source in movements.items():
            data.remove(source)
            data.add(target)

        print("\n== End of Round %d ==" % (i + 1)) if debug else None
        print_points(data) if debug else None
    
        # rotate default directions
        directions_order = directions_order[1:] + [directions_order[0]]
    
    score = compute_score(data)
    print(score) if debug else None
    return score

def ex2(data: dict):
    print("== Initial State ==") if debug else None
    print_points(data) if debug else None

    directions_order = ['N', 'S', 'W', 'E']
    
    i = 1
    while True:
        movements = dict()
        # print("directions order: %s" % " ".join(directions_order))
        for point in data:
            # si tous les points autour ne sont pas vides
            # print(point, all([ tuple(np.array(point) + d) not in data for d in all_adjacents ]))
            if any([ tuple(np.array(point) + d) in data for d in all_adjacents ]):
                for dir in directions_order:
                    if all([ tuple(np.array(point) + d) not in data for d in directions[dir] ]):
                        # movement to target already there:
                        target = tuple(np.array(point) + directions[dir][1])
                        if target in movements:
                            movements.pop(target)
                        else:
                            movements[tuple(np.array(point) + directions[dir][1])] = point
                        break
        
        print("tour %d, %d mouvements" % (i, len(movements)))
        if not movements:
            return i
        for target, source in movements.items():
            data.remove(source)
            data.add(target)

        print("\n== End of Round %d ==" % (i + 1)) if debug else None
        print_points(data) if debug else None
    
        # rotate default directions
        directions_order = directions_order[1:] + [directions_order[0]]
        i += 1

sample = load("sample.txt")
# print(sample)
assert ex1(sample.copy()) == 110
data = load("input.txt")
print("ex1 : %s" % ex1(data.copy()))

assert ex2(sample) == 20
print("ex2 : %s" % ex2(data))
