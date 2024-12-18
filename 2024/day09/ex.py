"""Imports"""
from __future__ import annotations
from os import path
# from copy import deepcopy
import sys
# from collections import defaultdict
# import math
# import re
# from colorama import Fore
# import numpy as np
# from heapq import *
# import networkx as nx

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False

def get_disk(data: str) -> list:
    """get disk content from disk map"""
    result = []
    for i in range(len(data) // 2):
        result.extend([i] * int(data[2*i]))
        result.extend([-1] * int(data[2*i+1]))
    result.extend([len(data)//2]*int(data[-1]))

    return result

def ex1(data: str) -> int:
    """Solve ex1"""

    disk_data = get_disk(data)

    while -1 in disk_data:
        i = disk_data.index(-1)
        disk_data[i] = disk_data[-1]
        disk_data.pop()
        while disk_data[-1] == -1:
            disk_data.pop()

        # pretty_print(disk_data)
    result = 0
    for i, v in enumerate(disk_data):
        result += i*v
    return result

def get_disk2(data: str) -> list:
    """get disk content from disk map"""
    result = []
    for i in range(len(data) // 2):
        result.append((i, int(data[2*i])))
        result.append((-1, int(data[2*i+1])))
    result.append((len(data) //2, int(data[-1])))

    return result

def ex2(data: str) -> int:
    """Solve ex2"""

    disk_data = get_disk2(data)
    max_id = len(disk_data) // 2

    for file_to_move_id in range(max_id, 0, -1):
        # Finding file to move pos
        index = -1
        for i in range(len(disk_data) - 1, 0, -1):
            if disk_data[i][0] == file_to_move_id:
                index = i
                break
        _, file_to_move_size = disk_data[index]
        for i, (file_id, file_size) in enumerate(disk_data):
            if file_id == -1 and i < index:
                if file_to_move_size == file_size:
                    disk_data[i] = (file_to_move_id, file_to_move_size)
                    disk_data[index] = (-1, file_to_move_size)
                    break
                if file_to_move_size < file_size:
                    disk_data[index] = (-1, file_to_move_size)
                    disk_data = disk_data[:i] + \
                        [(file_to_move_id, file_to_move_size), \
                            (-1, file_size - file_to_move_size)] + \
                        disk_data[i+1:-1]
                    break

    disk_data_array = []
    for i, l in disk_data:
        disk_data_array += [max(0, i)] * l

    result = 0
    for i, v in enumerate(disk_data_array):
        result += i * v
    return result


assert ''.join(map(lambda x: str(x) if x >=0 else '.', \
            get_disk(load("sample.txt")))) == '00...111...2...333.44.5555.6666.777.888899'
assert ex1(load("sample.txt")) == 1928
print(f'ex1 : {ex1(load("input.txt"))}')


# DEBUG = True
assert ex2(load("sample.txt")) == 2858
print(f'ex2 : {ex2(load("input.txt"))}')

sys.exit()
