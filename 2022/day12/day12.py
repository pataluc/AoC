import re
from os import path
from sys import argv
import numpy as np
from collections import defaultdict

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return [ l.rstrip() for l in open(file, "r").readlines() ]


def get_neighbours(tile, graph):
    height = len(graph)
    width = len(graph[-1])
    x, y = tile
    out = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    # print(graph[y][x])
    return [(a, b) for a, b in out if 0 <= a < width and 0 <= b < height \
        and ((ord(graph[y][x]) - ord(graph[b][a])) <= 1 )]


def _deconstruct_path(tentative_parents, end):
    if end not in tentative_parents:
        return None
    cursor = end
    path = []
    while cursor:
        path.append(cursor)
        cursor = tentative_parents.get(cursor)
    return list(reversed(path))

def dijkstra(graph, start, end):
    """
    Calculate the shortest path for a directed weighted graph.

    Node can be virtually any hashable datatype.

    :param start: starting node
    :param end: ending node
    :param graph: {"node1": {"node2": "weight", ...}, ...}
    :return: ["START", ... nodes between ..., "END"] or None, if there is no
            path
    """

    # We always need to visit the start
    nodes_to_visit = {start}
    visited_nodes = set()
    distance_from_start = defaultdict(lambda: float("inf"))
    # Distance from start to start is 0
    distance_from_start[start] = 0
    tentative_parents = {}

    while nodes_to_visit:
        # The next node should be the one with the smallest weight
        current = min(
            [(distance_from_start[node], node) for node in nodes_to_visit]
        )[1]
        # The end was reached
        if graph[current[1]][current[0]] == end:
            break

        nodes_to_visit.discard(current)
        visited_nodes.add(current)

        
        neighbours = get_neighbours(current, graph)
        # print("neighbours of ", current, ":\n", neighbours)

        for neighbour in neighbours:
            distance = 1 #get_weight(graph, current)
            if neighbour in visited_nodes:
                continue
            neighbour_distance = distance_from_start[current] + distance
            if neighbour_distance < distance_from_start[neighbour]:
                distance_from_start[neighbour] = neighbour_distance
                tentative_parents[neighbour] = current
                nodes_to_visit.add(neighbour)

    path = _deconstruct_path(tentative_parents, current)    
    # for j in range(len(graph)):
    #     for i in range(len(graph[0])):
    #         if (i,j) in path:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print("")

    if not(path):
        return None
    else:
        return len(path) - 1

def ex1(graph):
    # find start and end
    for j in range(len(graph)):
        for i in range(len(graph[0])):
            if graph[j][i] == 'S':
                graph[j] = graph[j].replace('S', '`')
            if graph[j][i] == 'E':
                start = (i,j)
                graph[j] = graph[j].replace('E', 'z')
    return dijkstra(graph, start, '`')


def ex2(graph):

    # find end
    for j in range(len(graph)):
        for i in range(len(graph[0])):
            if graph[j][i] == 'E':
                start = (i,j)
                graph[j] = graph[j].replace('E', 'z')
    return dijkstra(graph, start, 'a')

sample1 = load("sample.txt")
assert ex1(sample1) == 31

data = load("input.txt")
print("ex1 : %s" % ex1(data))

sample1 = load("sample.txt")
data = load("input.txt")
assert ex2(sample1) == 29
print("ex2 : %s" % ex2(data))