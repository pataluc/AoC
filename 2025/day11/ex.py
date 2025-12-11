

"""Imports"""
from __future__ import annotations
from os import path
from functools import cache
import sys
from collections import deque

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> list:
    """Loads data as a tuple"""

    return {line.split(':')[0]: (line.split(':')[1]).split() for line in data.split('\n')}

def bfs(devices: set[str: list[str]], start: str, end: str) -> list[list[str]]:
    Q = deque([[start]])
    visited = set()
    paths = []

    while Q:
        current = Q.popleft()
        last = current[-1]
        # print(current, len(visited))
        if last == end:
            paths.append(current)
        elif last in devices:
            for n in devices[last]:
                if n not in visited:
                    Q.append(current + [n])
                    visited.add(last)

    return paths

def ex1(data: str) -> int:
    """Solve ex1"""
    devices = load_data(data)

    @cache
    def walk(start: str, end: str, avoid: str = '') -> int:
        if start == end:
            return 1
        elif start != avoid:
            return sum(walk(n, end, avoid) for n in devices[start]) if start in devices else 0
        else:
            return 0

    paths = bfs(devices, 'you', 'out')
    # print('\n'.join([','.join(path) for path in paths]))

    return len(paths)


def ex2(data: str) -> int:
    """Solve ex2"""
    devices = load_data(data)

    @cache
    def walk(start: str, end: str, avoid: str = '') -> int:
        if start == end:
            return 1
        elif start != avoid:
            return sum(walk(n, end, avoid) for n in devices[start]) if start in devices else 0
        else:
            return 0

    dacfft = walk('dac', 'fft')
    dacout = walk('dac', 'out', 'fft')
    svrdac = walk('svr', 'dac', 'fft')

    fftout = walk('fft', 'out', 'dac')
    svrfft = walk('svr', 'fft', 'dac')
    fftdac = walk('fft', 'dac')

    result = svrdac * dacfft * fftout + svrfft * fftdac * dacout
    return result



assert ex1(load("sample.txt")) == 5
print(f'ex1 : {ex1(load("input.txt"))}')

# assert ex2(load("sample2.txt")) == 2
print(f'ex2 : {ex2(load("input.txt"))}')
sys.exit()

