"""Imports"""
from __future__ import annotations
from os import path
import sys
from collections import deque, defaultdict
from itertools import combinations

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> defaultdict[str, list[str]]:
    """Loads data as a tuple"""

    graph = defaultdict(list)

    for line in data.split('\n'):
        n1, n2 = line.split('-')
        graph[n1].append(n2)
        graph[n2].append(n1)

    return graph


def ex1(data: str) -> int:
    """Solve ex1"""

    graph = load_data(data)

    ans = set()

    for node, neighbours in graph.items():
        if node.startswith('t'):
            # print(f'Checking {node} with neighbours {neighbours}')
            for n1, n2 in combinations(neighbours, 2):
                # print(f'Checking {n1} and {n2}')
                if n1 in graph[n2]:
                    ans.add(tuple(sorted([node, n1, n2])))
                    # break

    # print(ans)
    return len(ans)


def ex2(data: str) -> int:
    """Solve ex1"""
    graph = load_data(data)

    groups_of_3 = set()

    for node, neighbours in graph.items():
        if node.startswith('t'):
            # print(f'Checking {node} with neighbours {neighbours}')
            for n1, n2 in combinations(neighbours, 2):
                # print(f'Checking {n1} and {n2}')
                if n1 in graph[n2]:
                    groups_of_3.add(tuple(sorted([node, n1, n2])))
                    # break

    group_of_n = set(groups_of_3)

    found_new_connections = True
    while found_new_connections:
        found_new_connections = False
        new_groups = set()
        for group in group_of_n:
            for node in graph.keys():
                if all(map(lambda neighbour: neighbour in graph[node], group)):
                    found_new_connections = True
                    new_groups.add(tuple(sorted(list(group) + [node])))
        if found_new_connections:
            group_of_n = new_groups

    ans = ','.join(sorted(list(group_of_n.pop())))
    # print(ans)
    return ans

assert ex1(load("sample.txt")) == 7
print(f'ex1 : {ex1(load("input.txt"))}')

# ex2('123')
# exit()
assert ex2(load("sample.txt")) == 'co,de,ka,ta'
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()
