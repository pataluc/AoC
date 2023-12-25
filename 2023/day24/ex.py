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
from sympy import Symbol
from sympy import solve_poly_system

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

def ex1(data: str, bottom = 200000000000000, top = 400000000000000) -> int:
    """Compute ex answer"""
    data_lines = data.split('\n')

    lines = []
    for line in data_lines:
        pos, speed = line.split('@')
        p1, p2, _ = tuple(int(x) for x in pos.split(', '))
        s1, s2, _ = tuple(int(x) for x in speed.split(', '))
        
        a = s2/s1
        b = p2-a*p1
        lines.append((a, b, p2, s2))

    result = 0
    for i in range(len(lines) - 1):
        for j in range(i +1, len(lines)):
            a1, b1, p1, s1 = lines[i]
            a2, b2, p2, s2 = lines[j]
            if DEBUG: print(f'\nHailstone A: {data_lines[i]}')
            if DEBUG: print(f'Hailstone B: {data_lines[j]}')
            if a1 != a2:
                x=(b2-b1)/(a1-a2)
                # assert abs((a1*x + b1) - (a2*x + b2)) < 0.000001
                y = a1*x + b1
                t1 = (y-p1)/s1
                t2 = (y-p2)/s2
                if DEBUG: print(t1, t2)
                
                if bottom <= x <= top and bottom <= y <= top and t1 > 0 and t2 > 0:
                    if DEBUG: print(f"Hailstones' paths will cross at x={x:.3f}, y={y:.3f}")
                    result += 1

    return result

def ex2(data: str) -> int:
    """Compute ex answer"""
    px = Symbol('px')
    py = Symbol('py')
    pz = Symbol('pz')
    vx = Symbol('vx')
    vy = Symbol('vy')
    vz = Symbol('vz')

    data_lines = data.split('\n')

    lines = []
    for line in data_lines[:3]:
        pos, speed = line.split('@')
        px, py, pz = tuple(int(c) for c in pos.split(', '))
        dx, dy, dz = tuple(int(c) for c in speed.split(', '))
        lines.append((px, py, pz, dx, dy, dz))

    print(lines)

    equations = []
    t_syms = []
    
    for i,line in enumerate(lines):
        #vx is the velocity of our throw, xv is the velocity of the shard we're trying to hit. Yes, this is a confusing naming convention.
        x0,y0,z0,xv,yv,zv = line
        t = Symbol('t'+str(i)) #remember that each intersection will have a different time, so it needs its own variable

        #(x + vx*t) is the x-coordinate of our throw, (x0 + xv*t) is the x-coordinate of the shard we're trying to hit.
        #set these equal, and subtract to get x + vx*t - x0 - xv*t = 0
        #similarly for y and z
        eqx = x + vx*t - x0 - xv*t
        eqy = y + vy*t - y0 - yv*t
        eqz = z + vz*t - z0 - zv*t

        equations.append(eqx)
        equations.append(eqy)
        equations.append(eqz)
        t_syms.append(t)

    #To my great shame, I don't really know how this works under the hood.
    result = solve_poly_system(equations,*([x,y,z,vx,vy,vz]+t_syms))
    print(result)
    print(result[0][0]+result[0][1]+result[0][2]) #part 2 answer

    return result[0][0]+result[0][1]+result[0][2]

assert ex1(load("sample.txt"), 7, 27) == 2
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 47
print(f'ex2 : {ex2((load("input.txt")))}')
sys.exit()
DEBUG = True
