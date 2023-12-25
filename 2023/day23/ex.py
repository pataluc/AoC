"""Imports"""
from __future__ import annotations
from os import path
from copy import deepcopy
import sys
from collections import deque
# import math
# import regex as re
from colorama import Fore
# import numpy as np
# from heapq import *

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False

def g_to_str(grid: list):
    """Printing grid"""
    return '\n'.join([''.join(line) for line in grid]) + "\n"

def pretty_print(grid, points):
    """Pretty printing grid"""
    print('#' * len(grid[0]))
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if (row, col) in points:
                print(Fore.RED + 'O', end='')
            else:
                print(Fore.WHITE + char, end='')
        print(Fore.WHITE + '')

def get_neighbours_part1(G, R, C, point):
    r, c = point
    n = []
    if r - 1 > 0 and G[r-1][c] in ['.', '^']:
        n.append((r-1, c))
    if c - 1 > 0 and G[r][c-1] in ['.', '<']:
        n.append((r, c-1))
    if c + 1 < C and G[r][c+1] in ['.', '>']:
        n.append((r, c+1))
    if r + 1 < R and G[r+1][c] in ['.', 'v']:
        n.append((r+1, c))
    return n

def get_neighbours_part2(G, R, C, point):
    r, c = point
    n = []
    for i, j in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        if 0 < r + i < R and 0 < c + j < C and G[r+i][c+j] != '#':
            n.append((r+i, c+j))
    return n


def find_longest_path_part1(G: list[list], R: int, C: int, orig: (int, int), target: (int, int), get_neighbours: get_neighbours_part1):
    queue = deque([[orig]])
    if DEBUG: print(queue)
    
    max_path = []

    while queue:
        current_path = queue.popleft()
        pos = current_path[-1]

        if pos == target:
            if len(current_path) > len(max_path):
                max_path = current_path
        else:            
            for neighbour in get_neighbours(G, R, C, pos):
                if neighbour not in current_path:
                    new_path = deepcopy(current_path)
                    new_path.append(neighbour)
                    queue.append(new_path)
            
    if DEBUG: pretty_print(G, max_path)
    if DEBUG: print(max_path, len(max_path))

    return max_path[1:]

def find_longest_path_part2(G: list[Node], orig: Node, target: Node):
    queue = deque([[(orig, 0)]])
    if DEBUG: print(queue)
    
    max_path = []

    while queue:
        # print(queue)
        current_path = queue.popleft()
        pos, _ = current_path[-1]

        if pos == target:
            print(''.join(f'{n.point}, {dist}' for n, dist in current_path))
            if sum(p[1] for p in current_path) > sum(p[1] for p in max_path):
                max_path = current_path
        else:            
            for neighbour, dist in pos.childrens.items():
                # print(neighbour.point, [p[0].point for p in current_path])
                if not any(p[0].point == neighbour.point for p in current_path):
                    new_path = deepcopy(current_path)
                    new_path.append((neighbour, dist))
                    queue.append(new_path)
            
    if DEBUG: pretty_print(G, max_path)
    if DEBUG: print(max_path, len(max_path))

    return sum(p[1] for p in max_path)

class Node:
    def __init__(self, point):
        self.point = point
        self.childrens: dict[Node: int] = {}

    def add_child(self, other, dist = 1):
        self.childrens[other] = dist

def ex1(data: str) -> int:
    """Compute ex answer"""

    G = [list(line) for line in data.split('\n')]
    R = len(G)
    C = len(G[0])

    orig = (0, G[0].index('.'))
    target = (R-1, G[R-1].index('.'))

    return len(find_longest_path_part1(G, R, C, orig, target))

def longest_path(g, cur, dst, distance=0, seen=set()):
	if cur == dst:
		return distance

	best = 0
	seen.add(cur)

	for neighbor, weight in cur.childrens.items():
		if neighbor in seen:
			continue

		best = max(best, longest_path(g, neighbor, dst, distance + weight))

	seen.remove(cur)
	return best

def ex2(data: str) -> int:
    """Compute ex answer"""

    G = [list(line) for line in data.split('\n')]
    R = len(G)
    C = len(G[0])
    
    nodes = {}
    for r in range(R):
        for c in range(C):
            if G[r][c] != '#':
                nodes[(r,c)] = Node((r,c))
    
    for node in nodes.values():
        # print(node)
        # print('#'*20)
        for rr, cc in get_neighbours_part2(G, R, C, node.point):
            # print(rr, cc)
            node.add_child(nodes[(rr, cc)])
    # print(nodes)

    for node in nodes.values():
        if len(node.childrens) == 2:
            a: Node
            b: Node
            a, b = node.childrens
            
            dista = a.childrens.pop(node)
            distb = b.childrens.pop(node)
            a.add_child(b, dista + distb)
            b.add_child(a, distb + dista)
            node.childrens = []

    orig = nodes[(0, G[0].index('.'))]
    target = nodes[(R-1, G[R-1].index('.'))]
    # print(nodes)
    nodes = [n for n in nodes.values() if len(n.childrens) > 0]
    # print('#'*30)
    
    # for node in nodes:
    #     print('-'*15)
    #     print(f'Node {node.point} goes to:')
    #     for c, d in node.childrens.items():
    #         print(f'{c.point} in {d}')

    # print(len(nodes))    
    # result = find_longest_path_part2(nodes, orig, target)
    result = longest_path(nodes, orig, target) 
    # exit()

    print(result)
    return result

# assert ex1(load("sample.txt")) == 94
# print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 154
print(f'ex2 : {ex2((load("input.txt")))}')
sys.exit()
DEBUG = True
