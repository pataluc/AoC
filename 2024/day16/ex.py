"""Imports"""
from __future__ import annotations
from os import path
import sys
from collections import deque

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

DEBUG = False

def get_neighbours(graph, current):
    """Get all neighbours of current in graph"""
    directions = {
        'E': (0, 1),
        'S': (1, 0),
        'W': (0, -1),
        'N': (-1, 0)
    } if not reversed else {
        'E': (0, -1),
        'S': (-1, 0),
        'W': (0, 1),
        'N': (1, 0)
    }
    left = {
        'E': 'N',
        'S': 'E',
        'W': 'S',
        'N': 'W'
    }
    right = {
        'E': 'S',
        'S': 'W',
        'W': 'N',
        'N': 'E'
    }

    H = len(graph)
    W = len(graph[0])
    pos, direction = current
    h, w = pos

    out = [(pos, left[direction], 1000), (pos, right[direction], 1000)]
    dh, dw = directions[direction]
    if 0 <= h + dh < H and 0 <= w + dw < W and graph[h+dh][w+dw] != '#':
        out.append(((h + dh, w + dw), direction, 1))

    return out

def bfspaths(graph, start, end):
    """BFS algo which returns every shortest paths from start to end"""
    paths = []

    q = deque()
    visited = {start: 0}

    q.append([(start, 0)])

    while q:
        current_path = q.popleft()
        (node, direction), cost = current_path[-1]

        if node == end:
            paths.append(current_path)

        for n_node, n_direction, n_cost in get_neighbours(graph, (node, direction)):
            if (n_node, n_direction) not in visited \
                    or visited[(n_node, n_direction)] >= cost + n_cost:
                newpath = current_path.copy()
                newpath.append(((n_node, n_direction), cost + n_cost))
                q.append(newpath)
                visited[(n_node, n_direction)] = cost + n_cost

    return list(filter(lambda x: x[-1][1] == min(path[-1][1] for path in paths), paths))

def ex1(data: str) -> int:
    """Solve ex1"""

    maze, H, W = load_data(data)
    start = end = None

    for h in range(H):
        for w in range(W):
            if maze[h][w] == 'S':
                start = (h, w)
            if maze[h][w] == 'E':
                end = (h, w)

    ans = bfspaths(maze, (start, 'E'), end)[0][-1][1]
    if DEBUG:
        print(ans)
    return ans


def ex2(data: str):
    """Solve ex1"""

    maze, H, W = load_data(data)
    start = end = None

    for h in range(H):
        for w in range(W):
            if maze[h][w] == 'S':
                start = (h, w)
            if maze[h][w] == 'E':
                end = (h, w)

    shortest_paths = bfspaths(maze, (start, 'E'), end)
    v_nodes = set()
    for current_path in shortest_paths:
        for (node, _), _ in current_path:
            v_nodes.add(node)

    if DEBUG:
        for h in range(H):
            for w in range(W):
                print('O' if (h, w) in v_nodes else maze[h][w], end='')
            print()
    return len(v_nodes)

assert ex1(load("sample1.txt")) == 7036
assert ex1(load("sample2.txt")) == 11048
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample1.txt")) == 45
assert ex2(load("sample2.txt")) == 64
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()
