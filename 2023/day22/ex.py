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

class Brick:
    """Brick object"""
    def __init__(self, id: int, points: ((int, int, int), (int, int, int))):
        """Constructor"""
        self.name = chr(ord('A') + id)
        self.point_a, self.point_b = points
        self.supported_by = set()
        self.supporting = set()
        # self.descendants = set()

    def get_points(self) -> ((int, int, int), (int, int, int)):
        """Get brick"s points"""
        return (self.point_a, self.point_b)

    def set_points(self, points: ((int, int, int), (int, int, int))) -> None:
        """Set brick"s points"""
        self.point_a, self.point_b = points

    def get_lower_z(self) -> int:
        """Get brick's lower z"""
        return self.point_a[2]

    def supports(self, b: Brick) -> None:
        """Adds support dependency"""
        self.supporting.add(b)
        b.supported_by.add(self)

    def supported_by_to_str(self) -> str:
        """Returns list of bricks supporting this one"""
        return " ".join(b.name for b in self.supported_by)
    def supporting_to_str(self) -> str:
        """Returns list of bricks supported by this one"""
        return " ".join(b.name for b in self.supporting)
    # def descendants_to_str(self) -> str:
    #     return " ".join(b.name for b in self.descendants)

def overlapping(r1, r2):
    """Check if 2 rectangles overlaps"""
    ((x1, y1), (x2, y2)) = r1
    ((X1, Y1), (X2, Y2)) = r2

    if x2 < X1 or X2 < x1:
        return False
    if y2 < Y1 or Y2 < y1:
        return False

    return True

def bricks_from_data(data: str) -> list[Brick]:
    bricks = [tuple(line.split('~')) for line in data.split('\n')]

    brick_set = []
    for i, (brick_p1, brick_p2) in enumerate(bricks):
        brick_p1 = tuple(map(int, brick_p1.split(',')))
        brick_p2 = tuple(map(int, brick_p2.split(',')))
        brick_set.append(Brick(i, (brick_p1, brick_p2)))
        for i in range(3):
            assert brick_p1[i] <= brick_p2[i]

    brick_set.sort(key=lambda b: b.get_lower_z())

    return brick_set

def fall_brick(fallen_bricks: list[Brick], to_fall: Brick) -> (((int, int, int), (int, int, int)), bool):
    ((x1, y1, z1), (x2, y2, z2)) = to_fall.get_points()
    z_orig = z1
    keep_going = True
    while keep_going and z1 >= 1:
        z1 -= 1
        z2 -= 1
        if DEBUG: print(z2)
        for fallen_brick in fallen_bricks:
            ((X1, Y1, Z1), (X2, Y2, Z2)) = fallen_brick.get_points()
            if DEBUG: print("  brick already there: ", ((X1, Y1, Z1), (X2, Y2, Z2)))
            if z1 <= Z2 and overlapping(((x1, y1), (x2, y2)), ((X1, Y1), (X2, Y2))):
                keep_going = False
                if DEBUG: print(f"  break! because z1 == 0 is {z1 == 0} or z2 <= Z1 is {z2 <= Z1} or overlaps is {overlapping(((x1, y1), (x2, y2)), ((X1, Y1), (X2, Y2)))}" )
                break

    to_fall.set_points(((x1, y1, z1 + 1), (x2, y2, z2 + 1)))
    return to_fall, not z1 + 1 == z_orig

def fall_bricks(brick_set: list[Brick]) -> (list[Brick], int):
    to_fall = deque(brick_set)
    moved = 0

    fallen_bricks: list[Brick] = []

    while to_fall:
        # fall bricks
        brick, has_moved = fall_brick(fallen_bricks, to_fall.popleft())
        fallen_bricks.append(brick)
        if has_moved:
            moved += 1

    for i, fallen_brick1 in enumerate(fallen_bricks[:-1]):
        ((x1, y1, z1), (x2, y2, z2)) = fallen_brick1.get_points()
        for j, fallen_brick2 in enumerate(fallen_bricks[i + 1:]):
            ((X1, Y1, Z1), (X2, Y2, Z2)) = fallen_brick2.get_points()
            if DEBUG: print(((x1, y1, z1), (x2, y2, z2)), ((X1, Y1, Z1), (X2, Y2, Z2)), z2 + 1 == Z1, overlapping(((x1, y1), (x2, y2)), ((X1, Y1), (X2, Y2))))
            if z2 + 1 == Z1 and overlapping(((x1, y1), (x2, y2)), ((X1, Y1), (X2, Y2))):
                if DEBUG: print(f"Brick {chr(ord('A') + i)} is supporting brick {chr(ord('A') + i + j + 1)}")
                fallen_bricks[i].supports(fallen_bricks[i+j+1])
            else:
                if DEBUG: print(f"Brick {chr(ord('A') + i)} does not supports brick {chr(ord('A') + i + j + 1)}")

    return fallen_bricks, moved

def ex1(data: str) -> int:
    """Compute ex answer"""

    bricks : list[Brick] = bricks_from_data(data)
    bricks = fall_bricks(bricks)[0]
    result = 0
    for b in bricks:
        if DEBUG: print(f'Brick {b.name}', 'supports', b.supporting_to_str(), 'and is supported by', b.supported_by_to_str())
        if len(b.supporting) == 0 or all([len(c.supported_by) > 1 for c in b.supporting]):
            result += 1

    if DEBUG: print(result)
    return result

def ex2(data: str) -> int:
    """Compute ex answer"""

    bricks : list[Brick] = fall_bricks(bricks_from_data(data))[0]

    result = 0
    L = len(bricks)
    for i in range(L):
        _, moved = fall_bricks(bricks[:i] + bricks[i+1:])
        print(f'{i}/{L}')
        if DEBUG: print(f'  Disintegrating brick {bricks[i].name} would move {moved} other bricks.')
        result += moved

    return result

    # no_childrens_bricks = [b for b in bricks_obj if len(b.supporting) == 0]

    # to_visit = deque(no_childrens_bricks)

    # while to_visit:
    #     b = to_visit.pop()
    #     for d in b.supporting:
    #         b.descendants = b.descendants.union(b.supporting, d.descendants)
    #     print(f'{b.name} has {b.descendants_to_str()} descendants and {b.supported_by_to_str()} parents')

    #     for parent in b.supported_by:
    #         to_visit.append(parent)
    # no_parents = [b for b in bricks_obj if len(b.supported_by) == 0]

    # to_visit = deque(no_parents)

    # while to_visit:
    #     b = to_visit.pop()
    #     for d in b.supporting:
    #         b.descendants = b.descendants.union(b.supporting, d.descendants)
    #     print(f'{b.name} has {b.descendants_to_str()} descendants and {b.supported_by_to_str()} parents')

    #     for parent in b.supported_by:
    #         to_visit.append(parent)


assert ex1(load("sample.txt")) == 5
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 7
print(f'ex2 : {ex2((load("input.txt")))}')
DEBUG = True
sys.exit()
