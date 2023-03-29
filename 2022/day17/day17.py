from os import path
from sys import argv, stderr
import numpy as np

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return open(file_path(file), "r").read().strip()

def print_chamber(points, height, current_rock = set()):
    maxy = height
    for r in current_rock:
        maxy = max(maxy, r[1])
    for h in range(maxy, -1, -1):
        print("|%s|" % ''.join([ '@' if (x, h) in current_rock else '#' if (x, h) in points else '.' for x in range(7) ]))
    print("+-------+\n")


rocks = [
    [(0,0),(1,0),(2,0),(3,0)],
    [(1,0),(0,1),(1,1),(2,1),(1,2)],
    [(0,0),(1,0),(2,0),(2,1),(2,2)],
    [(0,0),(0,1),(0,2),(0,3)],
    [(0,0),(1,0),(0,1),(1,1)],
    ]

def ex1(data):
    max_height = 0
    chamber = set()
    counter = 0

    for i in range(2022):
        # adding current rock:
        current_rock = [tuple(r + np.array((2, max_height + 4))) for r in rocks[i % 5] ]

        # apply gravity and winds
        while True:
            # Apply gravity:
            if all([tuple(r + np.array((0,-1))) not in chamber and r[1] > 0 for r in set(current_rock)]):
                current_rock = [ tuple(r + np.array((0, -1))) for r in current_rock ]
                # print("Rock falls 1 unit:")
                # print_chamber(chamber, max_height, current_rock)
            else:
                for p in current_rock:
                    chamber.add(p)
                    max_height = max(max_height, p[1] + 1)
                # print("Rock falls 1 unit, causing it to come to rest:")
                # print_chamber(chamber, max_height)
                break
            
            # Apply gas
            gas = np.array((-1 if data[counter % len(data)] == '<' else 1, 0))

            if all([tuple(r + gas) not in chamber and ((data[counter % len(data)] == '<' and 0 < r[0]) or (data[counter % len(data)] == '>' and r[0] < 6)) for r in set(current_rock)]):
                current_rock = [ tuple(r + gas) for r in current_rock ]
                # print("Jet of gas pushes rock %s:" % ("left" if data[counter % len(data)] == '<' else "right"))
            else:
                None
                # print("Jet of gas pushes rock %s, but nothing happens:" % ("left" if data[counter % len(data)] == '<' else "right"))

            counter += 1
            # print_chamber(chamber, max_height, current_rock)
    
    # print_chamber(chamber, max_height)
    maxy = 0
    for r in chamber:
        maxy = max(maxy, r[1])
    # print(maxy + 1)
    return maxy + 1

def ex2(data):
    max_height = 0
    chamber = set()
    counter = 0

    pattern = set()

    for i in range(2022):
        # adding current rock:
        current_rock = [tuple(r + np.array((2, max_height + 4))) for r in rocks[i % 5] ]

        # apply gravity and winds
        while True:
            # Apply gravity:
            if all([tuple(r + np.array((0,-1))) not in chamber and r[1] > 0 for r in set(current_rock)]):
                current_rock = [ tuple(r + np.array((0, -1))) for r in current_rock ]
                # print("Rock falls 1 unit:")
                # print_chamber(chamber, max_height, current_rock)
            else:
                for p in current_rock:
                    chamber.add(p)
                    max_height = max(max_height, p[1] + 1)
                # print("Rock falls 1 unit, causing it to come to rest:")
                # print_chamber(chamber, max_height)
                break
            
            # Apply gas
            gas = np.array((-1 if data[counter % len(data)] == '<' else 1, 0))

            if all([tuple(r + gas) not in chamber and ((data[counter % len(data)] == '<' and 0 < r[0]) or (data[counter % len(data)] == '>' and r[0] < 6)) for r in set(current_rock)]):
                current_rock = [ tuple(r + gas) for r in current_rock ]
                # print("Jet of gas pushes rock %s:" % ("left" if data[counter % len(data)] == '<' else "right"))
            else:
                None
                # print("Jet of gas pushes rock %s, but nothing happens:" % ("left" if data[counter % len(data)] == '<' else "right"))

            counter += 1
            # print_chamber(chamber, max_height, current_rock)
    
    # print_chamber(chamber, max_height)
    maxy = 0
    for r in chamber:
        maxy = max(maxy, r[1])
    # print(maxy + 1)
    return maxy + 1

sample = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

# print(sample)
assert ex1(sample) == 3068

data = load("input.txt")
print("ex1 : %s" % ex1(data))


assert ex2(sample) == 1514285714288
print("ex2 : %s" % ex2(data))
