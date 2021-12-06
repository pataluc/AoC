import sys
import re
file = "sample.txt" if len(sys.argv) == 2 and sys.argv[1] == "-d" else "input.txt"
lines = open(file, "r").readlines()

vents =  [list(map(int, re.split(r'\D+', line.rstrip()))) for line in lines]

width = max(list(map(max, vents)))

def print_grid(grid):
    for line in grid:
        print("".join(map(lambda x : str(x) if x > 0 else '.', line)))

def improved_range(i, j):
    dir = 1 if j >= i else -1
    return range(i, j + dir, dir)

def get_points(vent):    
    x1, y1, x2, y2 = vent
    return list(zip(
        improved_range(x1, x2) if x1 != x2 else [x1] * (abs(y2 - y1) + 1),
        improved_range(y1, y2) if y1 != y2 else [y1] * (abs(x2 - x1) + 1)
    ))

def count_overlaps(vents):
    occurences = {}
    for p in sum(list(map(get_points, vents)), []):
        occurences[p] = occurences.get(p, 0) + 1
    return len(list(filter(lambda x : x[1] >= 2, occurences.items())))              

def ex1():
    return count_overlaps(list(filter(lambda x : x[0] == x[2] or x[1] == x[3], vents)))

def ex2():
    return count_overlaps(vents)

print("ex1 : %d" % ex1())
print("ex2 : %d" % ex2())



