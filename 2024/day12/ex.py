"""Imports"""
from __future__ import annotations
from os import path
# from copy import deepcopy
import sys
from collections import defaultdict
# import math
# import re
# from colorama import Fore
# import numpy as np
# from heapq import *
# import networkx as nx
import functools

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> tuple:
    """Loads data as a tuple"""

    grid = [list(line) for line in data.split('\n')]
    H = len(grid)
    W = len(grid[0])

    return grid, H, W

DEBUG = False

# def print_grid(H, W, antennas, antinodes):
#     for h in range(H):
#         for w in range(W):
#             if (h, w) in antinodes:
#                 print('#', end='')
#             elif any([(h, w) in antenna_letter for antenna_letter in antennas.values()]):
#                 print('@', end='')
#             else:
#                 print('.', end='')
#         print('')

# def pretty_print(data: list):
#     print(''.join(map(lambda x: str(x) if x >=0 else '.', data)))

def get_regions(grid: list, H: int, W: int) -> list:
    """Search map for regions"""
    already_visited = set()
    regions = list()

    for h in range(H):
        for w in range(W):
            if (h, w) not in already_visited:
                region = {(h, w)}
                still_has_neighbours = True
                while still_has_neighbours:
                    still_has_neighbours = False
                    new_points_of_region = set()
                    for ph, pw in region:
                        for nh, nw in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                            if 0 <= ph + nh < H \
                                and 0 <= pw + nw < W \
                                and grid[ph][pw] == grid[ph + nh][pw + nw] \
                                and (ph + nh, pw + nw) not in already_visited:
                                new_points_of_region.add((ph + nh, pw + nw))
                                already_visited.add((ph + nh, pw + nw))
                                still_has_neighbours = True
                    region = region.union(new_points_of_region)
                    # print("new_points_of_region", new_points_of_region)
                    # print("region", region)
                regions.append(region)

    # print(regions)
    return regions

def ex1(data: str) -> int:
    """Solve ex1"""

    grid, H, W = load_data(data)

    regions = get_regions(grid, H, W)

    ans = 0

    for region in regions:
        area = len(region)
        perimeter = len(region) * 4
        for hi, wi in region:
            for hj, wj in region:
                if abs(hi - hj) + abs(wi - wj) == 1:
                    perimeter -= 1

        # print(region, area, perimeter)
        ans += area * perimeter

    return ans

def ex2(data: str) -> int:
    """Solve ex1"""

    grid, H, W = load_data(data)

    regions = get_regions(grid, H, W)

    ans = 0

    for region in regions:
        area = len(region)

        sides = []
        for (h, w) in region:
            sides.append((h, w, 'n'))
            sides.append((h, w, 'e'))
            sides.append((h, w, 's'))
            sides.append((h, w, 'w'))
        
        # Remove inner edges
        sides_without_contiguous = sides.copy()
        # print(sides_without_contiguous)

        region_list = list(region)
        for i in range(len(region_list)):
            hi, wi = region_list[i]
            for j in range(i+1, len(region_list)):
                hj, wj = region_list[j]
                # i is above j
                if hi == hj + 1 and wi == wj:
                    # print('i', (hi, wi), 'j', (hj, wj))
                    sides_without_contiguous.remove((hi, wi, 's'))
                    sides_without_contiguous.remove((hj, wj, 'n'))
                # i is below j
                if hi + 1 == hj and wi == wj:
                    # print('i', (hi, wi), 'j', (hj, wj))
                    sides_without_contiguous.remove((hi, wi, 'n'))
                    sides_without_contiguous.remove((hj, wj, 's'))
                # i is left of j
                if hi == hj and wi + 1 == wj:
                    # print('i', (hi, wi), 'j', (hj, wj))
                    sides_without_contiguous.remove((hi, wi, 'e'))
                    sides_without_contiguous.remove((hj, wj, 'w'))
                # i is right of j
                if hi == hj and wi == wj + 1:
                    # print('i', (hi, wi), 'j', (hj, wj))
                    sides_without_contiguous.remove((hi, wi, 'w'))
                    sides_without_contiguous.remove((hj, wj, 'e'))
        
        # Remove 
        perimeter = len(sides_without_contiguous)
        for i in range(len(sides_without_contiguous)):
            hi, wi, ci = sides_without_contiguous[i]
            for j in range(i, len(sides_without_contiguous)):
                hj, wj, cj = sides_without_contiguous[j]
                if abs(hi - hj) + abs(wi - wj) == 1 and ci == cj:
                    # print((hi, wi, ci), (hj, wj, cj))
                    perimeter -= 1

        # print(region, area, perimeter)
        ans += area * perimeter

    return ans

assert ex1(load("sample1.txt")) == 140
assert ex1(load("sample2.txt")) == 772
assert ex1(load("sample3.txt")) == 1930
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample1.txt")) == 80
assert ex2(load("sample2.txt")) == 436
assert ex2(load("sample4.txt")) == 236
assert ex2(load("sample5.txt")) == 368
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()
