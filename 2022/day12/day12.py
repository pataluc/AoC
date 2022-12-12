import re
from os import path
from sys import argv
import numpy as np
from collections import defaultdict

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return [ l.rstrip() for l in open(file, "r").readlines() ]

def get_neighbours(tile, graph):
    height = len(graph)
    width = len(graph[-1])
    x, y = tile
    out = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(a, b) for a, b in out if 0 <= a < width and 0 <= b < height \
        and ((ord(graph[y][x]) - ord(graph[b][a])) <= 1 )]

def bfs(graph, start, endvalue):
    queue  = []
    queue.append(start)
    visited = {}
    visited[start] = 0

    while len(queue):
        current = queue.pop(0)
        for neighbour in get_neighbours(current, graph):
            if graph[neighbour[1]][neighbour[0]] == endvalue:
                return visited[current] + 1
            elif neighbour not in visited:
                queue.append(neighbour)
                visited[neighbour] = visited[current] + 1

def ex1(graph):
    # find start and end
    for j in range(len(graph)):
        for i in range(len(graph[0])):
            if graph[j][i] == 'S':
                graph[j] = graph[j].replace('S', '`')
            if graph[j][i] == 'E':
                start = (i,j)
                graph[j] = graph[j].replace('E', 'z')
    return bfs(graph, start, '`')


def ex2(graph):
    # find end
    for j in range(len(graph)):
        for i in range(len(graph[0])):
            if graph[j][i] == 'E':
                start = (i,j)
                graph[j] = graph[j].replace('E', 'z')
    return bfs(graph, start, 'a')

sample1 = load("sample.txt")
assert ex1(sample1) == 31

data = load("input.txt")
print("ex1 : %s" % ex1(data))

sample1 = load("sample.txt")
data = load("input.txt")
assert ex2(sample1) == 29
print("ex2 : %s" % ex2(data))