"""Imports"""
from __future__ import annotations
from os import path
# from copy import deepcopy
import sys
from collections import defaultdict
# import math
import re
# from colorama import Fore
# import numpy as np
# from heapq import *
# import networkx as nx
# import functools
# from sympy import solve, symbols, Eq

from PIL import Image

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()


class Robot:
    """Robot object"""

    def __init__(self, id: int, init_pos: tuple, velocity: tuple, grid_size: tuple):
        """Constructor"""
        self.id = id
        self.w, self.h = init_pos
        self.vw, self.vh = velocity
        self.H, self.W = grid_size
    
    def __str__(self) -> str:
        return "Robot %d with v = (%d, %d) is on point (%d, %d)\n" % (self.id, self.vh, self.vw, self.h, self.w)

    def move(self) -> None:
        """Move for 1 second"""
        self.h = (self.h + self.vh) % self.H
        self.w = (self.w + self.vw) % self.W
    

def load_data(data: str) -> tuple:
    """Loads data as a tuple"""
    
    robots = []
    H = 7 if len(data.split('\n')) == 12 else 103
    W = 11 if len(data.split('\n')) == 12 else 101
    for i, robot in enumerate(data.split('\n')):
        line = robot.split()

        robots.append(Robot(i, tuple(map(int, line[0].replace('p=', '').split(','))), tuple(map(int, line[1].replace('v=', '').split(','))), (H, W)))

    return robots, H, W

DEBUG = False

def ex1(data: str) -> int:
    """Solve ex1"""

    robots, H, W = load_data(data)

    for i in range(100):
        for robot in robots:
            robot.move()

    q1 = sum([1 if robot.h < (H / 2) - 1 and robot.w < (W / 2) - 1 else 0 for robot in robots])
    q2 = sum([1 if robot.h < (H / 2) - 1 and robot.w > (W / 2) else 0 for robot in robots])
    q3 = sum([1 if robot.h > (H / 2) and robot.w < (W / 2) - 1 else 0 for robot in robots])
    q4 = sum([1 if robot.h > (H / 2) and robot.w > (W / 2) else 0 for robot in robots])
    
    
    return q1*q2*q3*q4

def save_picture(seconds: int, robots: list, H: int, W: int) -> str:
    
    img = Image.new('RGB', (W, H), "white")

    for h in range(H):
        for w in range(W):
            if sum([(robot.h, robot.w) == (h, w) for robot in robots]) > 0:
                img.putpixel((w, h), (0,0,0))
    img.save('output/image%d.png' % seconds)

def whole_picture(robots: list, H: int, W: int) -> str:
    res = ''
    points = {(r.h, r.w) for r in robots}
    for h in range(H):
        for w in range(W):
            res += '#' if (h, w) in points else ' '
        res += '\n'
    return res


def ex2(data: str):

    robots, H, W = load_data(data)

    i = 0
    while i < 10000:
        for robot in robots:
            robot.move()
        i += 1
        pic = whole_picture(robots, H, W)
        if '######################' in pic:
            print(i)
            print(pic)
            exit()


assert ex1(load("sample.txt")) == 12
print(f'ex1 : {ex1(load("input.txt"))}')

print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()
