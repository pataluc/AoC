"""Imports"""
from __future__ import annotations
from os import path
import sys
from collections import deque, defaultdict

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> tuple:
    """Loads data as a tuple"""

    maze = [list(line) for line in data.split('\n')]

    return maze, len(maze), len(maze[0])


def get_neighbours(graph, pos):
    """Get all neighbours of current in graph"""
    directions = {
        'E': (0, 1),
        'S': (1, 0),
        'W': (0, -1),
        'N': (-1, 0)
    }

    H = len(graph)
    W = len(graph[0])
    h, w = pos

    out = [(h+dh, w+dw) for dh, dw in directions.values() if graph[h+dh][w+dw] != '#' and 0 <= h+dh < H and 0 <= w+dw<W ]

    return out

def bfspath(graph, start, end):
    """BFS algo which returns every shortest paths from start to end"""
    q = deque()
    visited = {start}

    q.append([start])

    while q:
        current_path = q.popleft()
        node = current_path[-1]

        if node == end:
            return current_path

        for n_node in get_neighbours(graph, node):
            if n_node not in visited:
                newpath = current_path.copy()
                newpath.append(n_node)
                q.append(newpath)
                visited.add(node)

DEBUG = False

def ex(data: str, delta = 100, manhattan_max = 2) -> int:
    """Solve ex1"""

    maze, H, W = load_data(data)
    start = end = None

    for h in range(H):
        for w in range(W):
            if maze[h][w] == 'S':
                start = (h, w)
            if maze[h][w] == 'E':
                end = (h, w)

    shortest_path = bfspath(maze, start, end)
    ans = 0
    cheats = defaultdict(int)
    for i, (h1, w1) in enumerate(shortest_path):
        for j, (h2, w2) in enumerate(shortest_path):
            # Manhattan distance
            distance = abs(h2-h1) + abs(w2-w1)
            if distance <= manhattan_max \
                and j-i -distance >= delta:
                cheats[j-i - distance] += 1
                ans += 1

    return ans

assert ex(load("sample.txt"), delta=1) == 44
print(f'ex1 : {ex(load("input.txt"))}')

assert ex(load("sample.txt"), manhattan_max=20, delta=50) == 285
print(f'ex2 : {ex(load("input.txt"), manhattan_max=20)}')


sys.exit()
