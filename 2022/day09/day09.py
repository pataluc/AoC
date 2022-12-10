import re
from os import path
from sys import argv

import numpy as np

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)


def load(file):
    moves = [tuple(x.split(" ")) for x in open(file_path(file), "r").read().split("\n")]
    return moves

directions = {'U': np.array([0, 1]),
              'L': np.array([-1, 0]),
              'D': np.array([0, -1]),
              'R': np.array([1, 0])}

def ex1(moves):
    visited = set()
    h = np.array([0, 0])
    t = np.array([0, 0])
    for direction, times in moves:
        for i in range(int(times)):
            h += directions[direction]
            v = h - t
            if abs(v[0]) == 2:
                t += np.array([v[0] // 2, v[1]])
            elif abs(v[1]) == 2:
                t += np.array([v[0], v[1] // 2])
            visited.add(str(t))
    return len(visited)

def ex2(moves):
    visited = set()
    knots = []
    for i in range(10):
        knots.append(np.array([0, 0]))
    
    for direction, times in moves:
        #print("move %s %s times" % (direction, times))
        for i in range(int(times)):
            knots[0] += directions[direction]
        
            for i in range(1, 10):
                v = knots[i - 1] - knots[i]
                if abs(v[0]) == 2 and abs(v[1]) == 2:
                    knots[i] += np.array([v[0] // 2, v[1] // 2])
                elif abs(v[0]) == 2:
                    knots[i] += np.array([v[0] // 2, v[1]])
                elif abs(v[1]) == 2:
                    knots[i] += np.array([v[0], v[1] // 2])
            visited.add(str(knots[-1]))
            #print(knots)
    return len(visited)

sample_moves = load("sample.txt")
# print(sample_moves)
assert ex1(sample_moves) == 13

moves = load("input.txt")
print("ex1 : %s" % ex1(moves))

assert ex2(sample_moves) == 1
sample_moves = load("sample2.txt")
assert ex2(sample_moves) == 36
print("ex2 : %s" % ex2(moves))