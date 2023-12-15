"""Imports"""
from os import path
import sys
# from collections import Counter
import math
import regex as re
# import numpy as np

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False

def g_to_str(grid: list):
    return '\n'.join([''.join(line) for line in grid]) + "\n"

def ex1(data):
    """Compute ex answer"""
    
    P = [[c for c in row] for row in data.split('\n')]
    W = len(P[0])
    H = len(P)
    if DEBUG: print(g_to_str(P), W, H)

    for c in range(H):
        for r in range(W):
            if P[r][c] == 'O':
                dr = r
                while dr > 0 and P[dr - 1][c] == '.':
                    dr -= 1
                if dr != r:
                    P[dr][c] = 'O'
                    P[r][c] = '.'
    
    if DEBUG: print(g_to_str(P))

    result = sum([line.count('O') * (H - i) for i, line in enumerate(P)])

    if DEBUG: print(result)
    return result

def ex2(data, cycles = 1000000000):
    """Compute ex answer"""
    
    P = [[c for c in row] for row in data.split('\n')]
    W = len(P[0])
    H = len(P)
    if DEBUG: print(g_to_str(P))

    previous = {}

    i = 0
    while i < cycles:
        i += 1
        if i % 10000 == 0: print(i)

        # Tilt North
        for c in range(H):
            for r in range(W):
                if P[r][c] == 'O':
                    dr = r
                    while dr > 0 and P[dr - 1][c] == '.':
                        dr -= 1
                    if dr != r:
                        P[dr][c] = 'O'
                        P[r][c] = '.'
        
        # if DEBUG: print(g_to_str(P))

        # Tilt West
        for r in range(H):
            for c in range(W):
                if P[r][c] == 'O':
                    dc = c
                    while dc > 0 and P[r][dc - 1] == '.':
                        dc -= 1
                    if dc != c:
                        P[r][dc] = 'O'
                        P[r][c] = '.'
        
        # if DEBUG: print(g_to_str(P))

        # Tilt South
        for c in range(W):
            for r in range(H - 1, -1, -1):
                if P[r][c] == 'O':
                    dr = r
                    while dr < H - 1 and P[dr + 1][c] == '.':
                        dr += 1
                    if dr != r:
                        P[dr][c] = 'O'
                        P[r][c] = '.'
        
        # if DEBUG: print(g_to_str(P))

        # Tilt East
        for r in range(W):
            for c in range(H - 1, -1, -1):
                if P[r][c] == 'O':
                    dc = c
                    while dc < W - 1 and P[r][dc + 1] == '.':
                        dc += 1
                    if dc != c:
                        P[r][dc] = 'O'
                        P[r][c] = '.'
        
        s = g_to_str(P)
        if s not in previous:
            previous[s] = i
        else:
            delta = i - previous[s]
            if DEBUG: print("delta", delta)
            if i < cycles - delta:
                if DEBUG: print("Jumping from", i)
                while i < cycles - delta:
                    i += delta
                if DEBUG: print("... to", i)
    
    if DEBUG: print(g_to_str(P))

    result = sum([line.count('O') * (H - i) for i, line in enumerate(P)])
    
    return result

assert ex1(load("sample.txt")) == 136
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 64
print(f'ex2 : {ex2((load("input.txt")))}')

DEBUG = True
sys.exit()
