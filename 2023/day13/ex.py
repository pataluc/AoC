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

def ex1(data):
    """Compute ex answer"""
    
    patterns = data.split('\n\n')
    result = 0
    
    for pattern in patterns:
        pattern = pattern.split('\n')
        W = len(pattern[0])
        H = len(pattern)

        # Check vertical
        for i in range(1, W):
            w = min(i, W - i)
            if all(map(lambda line: line[i-w:i] == line[i:i+w][::-1], pattern)):
                result += i
                break

        # Check horizontal
        for i in range(1, H):
            h = min(i, H - i)
            if DEBUG: print(''.join([pattern[j][0] for j in range(i-h, i)]), ''.join([pattern[j][0] for j in range(i, i+h)]))
            if all(map(lambda x: ''.join([pattern[j][x] for j in range(i-h, i)]) == ''.join([pattern[j][x] for j in range(i, i+h)])[::-1], range(W))):
                result += 100*i
                break
        if DEBUG: print(result)
        # exit()
    
    return result

def ex2(data):
    """Compute ex answer"""
    
    patterns = data.split('\n\n')
    result = 0
    
    for pattern in patterns:
        pattern = pattern.split('\n')
        W = len(pattern[0])
        H = len(pattern)
        if DEBUG: print(pattern)

        # Ref
        ref = 0
        # Check vertical
        for i in range(1, W):
            w = min(i, W - i)
            if all(map(lambda line: line[i-w:i] == line[i:i+w][::-1], pattern)):
                ref = i
                break

        # Check horizontal
        for i in range(1, H):
            h = min(i, H - i)
            if DEBUG: print(''.join([pattern[j][0] for j in range(i-h, i)]), ''.join([pattern[j][0] for j in range(i, i+h)]))
            if all(map(lambda x: ''.join([pattern[j][x] for j in range(i-h, i)]) == ''.join([pattern[j][x] for j in range(i, i+h)])[::-1], range(W))):
                ref = 100*i
                break
        if DEBUG: print("ref : ", ref)
        has_result = False
        for u in range(H):
            for v in range(W):
                orig = pattern[u][v]
                if DEBUG: print(u, v, orig)
                if DEBUG: print(pattern[u], pattern[u][:v] + ('.' if orig == '#' else '#') + pattern[u][v+1:])
                pattern[u] = pattern[u][:v] + ('.' if orig == '#' else '#') + pattern[u][v+1:]
                if DEBUG: print(pattern)

                # Check vertical
                for i in range(1, W):
                    w = min(i, W - i)
                    if i != ref and all(map(lambda line: line[i-w:i] == line[i:i+w][::-1], pattern)):
                        if DEBUG: print(u, v, i)
                        result += i
                        has_result = True
                        break

                # Check horizontal
                for i in range(1, H):
                    h = min(i, H - i)
                    if DEBUG: print(''.join([pattern[j][0] for j in range(i-h, i)]), ''.join([pattern[j][0] for j in range(i, i+h)]))
                    if 100 *i != ref and all(map(lambda x: ''.join([pattern[j][x] for j in range(i-h, i)]) == ''.join([pattern[j][x] for j in range(i, i+h)])[::-1], range(W))):
                        if DEBUG: print(u, v, i)
                        result += 100*i
                        has_result = True
                        break
                
                if has_result:
                    break

                pattern[u] = pattern[u][:v] + orig + pattern[u][v+1:]
            if has_result:
                break
    # print(result)
    # exit()
    return result

assert ex1(load("sample.txt")) == 405
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2((load("sample.txt"))) == 400
print(f'ex2 : {ex2((load("input.txt")))}')

DEBUG = True
sys.exit()
