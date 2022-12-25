import re
from os import path
from sys import argv
import numpy as np

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    lines = open(file_path(file), "r").read().split("\n")
    width = len(lines[0]) - 2
    height = len(lines) - 2

    blizzards_west = [ set(i for i in range(width) if lines[j+1][i+1] == '<') for j in range(height) ]
    blizzards_east = [ set(i for i in range(width) if lines[j+1][i+1] == '>') for j in range(height) ]
    blizzards_north = [ set(j for j in range(height) if lines[j+1][i+1] == '^') for i in range(width) ]
    blizzards_south = [ set(j for j in range(height) if lines[j+1][i+1] == 'v') for i in range(width) ]

    return width, height, [blizzards_west, blizzards_east, blizzards_north, blizzards_south]

def bfs(data, start, end, time_initial = 0):
    width, height, blizzards = data
    # print("going from", start, "to", end, "time =", time_initial)

    queue  = [(start[0], start[1], time_initial)]
    visited = set([start[0], start[1], time_initial % (width * height)])

    while queue:
        i, j, time = queue.pop(0)
        if (i, j) == end:
            return time
        
        # parcours des voisins
        for m, n in ((i-1, j), (i, j-1), (i,j), (i, j+1), (i+1, j)):
            if (m, n) not in [start, end] and (not 0 <= m < width or not 0 <= n < height) :
                continue
            if 0 <= m < width and 0 <= n < height and (m + time + 1) % width  in blizzards[0][n]:
                continue
            if 0 <= m < width and 0 <= n < height and (m - time - 1) % width  in blizzards[1][n]:
                continue
            if 0 <= m < width and 0 <= n < height and (n + time + 1) % height in blizzards[2][m]:
                continue
            if 0 <= m < width and 0 <= n < height and (n - time - 1) % height in blizzards[3][m]:
                continue
            if (m, n, time + 1) not in visited:
                queue.append((m, n, time + 1))
                visited.add((m, n, (time + 1) % (width * height)))

def ex1(data):
    width, height, _ = data
    return bfs(data, (0, -1), (width - 1, height))

def ex2(data):
    width, height, _ = data
    aller = bfs(data, (0, -1), (width - 1, height))
    retour = bfs(data, (width - 1, height), (0, -1), aller)
    return bfs(data, (0, -1), (width - 1, height), retour)


sample2 = load("sample2.txt")

assert ex1(sample2) == 18
data = load("input.txt")
print("ex1 : %s" % ex1(data))

assert ex2(sample2) == 54
print("ex2 : %s" % ex2(data))
