

"""Imports"""
from __future__ import annotations
from os import path
import sys
import math
import networkx as nx

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> list:
    """Loads data as a tuple"""

    return [tuple(map(int, line.split(','))) for line in data.split('\n')]

def distance(box1: tuple, box2: tuple) -> float:
    x1, y1, z1 = box1
    x2, y2, z2 = box2

    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

def ex1(data: str, times: int) -> int:
    """Solve ex1"""
    boxes = load_data(data)

    G = nx.Graph()
    for box in boxes:
        G.add_node(box)


    # #######
    # d = set()
    # for i, box1 in enumerate(boxes):
    #     for j in range(i+1, len(boxes)):
    #         box2 = boxes[j]
    #         d.add(distance(box1, box2))
    # print(sorted(list(d))[:11])
    # #######


    connections = set()

    for _ in range(times):

        md = distance(boxes[0], boxes[1])
        mb1, mb2 = boxes[:2]
        for i, box1 in enumerate(boxes):
            for j in range(i+1, len(boxes)):
                box2 = boxes[j]
                d = distance(box1, box2)
                if d < md and (box1, box2) not in connections:
                    md = d
                    mb1 = box1
                    mb2 = box2
        connections.add((mb1, mb2))
        G.add_edge(mb1, mb2)
    sizes = [len(c) for c in nx.connected_components(G)]
    result = 1
    for s in sorted(sizes, reverse = True)[:3]:
        result *= s
    return result


def ex2(data: str) -> int:
    """Solve ex2"""
    boxes = load_data(data)

    G = nx.Graph()
    for box in boxes:
        G.add_node(box)

    connections = set()

    while nx.number_connected_components(G) > 1:
        md = distance(boxes[0], boxes[1])
        mb1, mb2 = boxes[:2]
        for i, box1 in enumerate(boxes):
            for j in range(i+1, len(boxes)):
                box2 = boxes[j]
                d = distance(box1, box2)
                if d < md and (box1, box2) not in connections:
                    md = d
                    mb1 = box1
                    mb2 = box2
        connections.add((mb1, mb2))
        G.add_edge(mb1, mb2)

    return mb1[0] * mb2[0]


assert ex1(load("sample.txt"), 10) == 40
print(f'ex1 : {ex1(load("input.txt"), 1000)}')

sys.exit()
assert ex2(load("sample.txt")) == 25272
print(f'ex2 : {ex2(load("input.txt"))}')

