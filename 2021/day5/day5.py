import sys
import re
file = "sample.txt" if len(sys.argv) == 2 and sys.argv[1] == "-d" else "input.txt"
lines = open(file, "r").readlines()

vents =  [list(map(int, re.split(r'\D+', line.rstrip()))) for line in lines]

width = max(list(map(max, vents)))

def print_grid(grid):
    for line in grid:
        print("".join(map(lambda x : str(x) if x > 0 else '.', line)))

def apply_vent(grid, vent):
    y1, x1, y2, x2 = vent
    dir_x = 1 if x2 >= x1 else -1
    dir_y = 1 if y2 >= y1 else -1

    if x1 == x2: #horiz
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[x1][y] += 1 
    elif y1 == y2: #vertical
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[x][y1] += 1         
    else: #diag
        for i, j in list(zip(range(0, dir_x + x2 - x1, dir_x), range(0, dir_y + y2 - y1, dir_y))):
            grid[x1 + i][y1 + j] += 1               

def ex1():
    grid = [[0 for i in range(width + 1)] for j in range(width + 1)]
    for vent in list(filter(lambda x : x[0] == x[2] or x[1] == x[3], vents)):
        apply_vent(grid, vent)
    return sum(map(lambda line: len(list(filter(lambda x: x >= 2, line))), grid))

def ex2():
    grid = [[0 for i in range(width + 1)] for j in range(width + 1)]
    for vent in list(filter(lambda x : x[0] == x[2] or x[1] == x[3] or abs(x[0] - x[3]) == abs(x[1] - x[2]) or abs(x[0] - x[2]) == abs(x[1] - x[3]), vents)):
        apply_vent(grid, vent)
    return sum(map(lambda line: len(list(filter(lambda x: x >= 2, line))), grid))

print("ex1 : %d" % ex1())
print("ex2 : %d" % ex2())



