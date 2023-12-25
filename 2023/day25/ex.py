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
import networkx as nx

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

def ex1(data: str) -> int:
    """Compute ex answer"""
    data_lines = data.split('\n')

    wires_graph = nx.DiGraph()
    for line in data_lines:
        n1, nodes= line.split(': ')
        for n2 in nodes.split():
            wires_graph.add_edge(n1, n2, capacity=1)
            wires_graph.add_edge(n2, n1, capacity=1)
    
    m = list(wires_graph.nodes)[0]
    
    for n in wires_graph.nodes:
        if m != n:
            cut_num, (group1, group2) = nx.minimum_cut(wires_graph, m, n)
            if cut_num == 3:
                return len(group1) * len(group2)


# assert ex1(load("sample.txt")) == 54
print(f'Final ex : {ex1(load("input.txt"))}')
DEBUG = True

sys.exit()
