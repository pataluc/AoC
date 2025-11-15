from os import path
import sys

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

# Custo starts here
def load_data(data: str) -> tuple:
    """Loads data as a tuple"""
    return [line.split(':')[1] for line in data.split('\n')]

def similarity(child: str, parent: str) -> int:
    """Returns similarity score between child and parent strings"""
    score = 0
    for i in range(len(child)):
        if child[i] == parent[i]:
            score += 1
    return score

def is_child(child: str, parent1: str, parent2: str) -> bool:
    """Checks if child string can be formed from parent strings"""
    for i in range(len(child)):
        if child[i] not in [parent1[i], parent2[i]]:
            return False
    return True

def part1(scales: list) -> int:
    # first is child
    if is_child(scales[0], scales[1], scales[2]):
        result = similarity(scales[0], scales[1]) * similarity(scales[0], scales[2])
        return result
    # second is child
    elif is_child(scales[1], scales[0], scales[2]):
        result = similarity(scales[1], scales[0]) * similarity(scales[1], scales[2])
        return result
    # third is child
    elif is_child(scales[2], scales[0], scales[1]):
        result = similarity(scales[2], scales[0]) * similarity(scales[2], scales[1])
        return result

assert part1(load_data(load('sample1'))) == 414
print("Part 1: ", part1(load_data(load('notes1'))))



def part2(scales: list) -> int:
    result = 0
    for child in scales:
        for p1 in range(len(scales) - 1):
            parent1 = scales[p1]
            for p2 in range(p1, len(scales)):
                parent2 = scales[p2]
                if child != parent1 and child != parent2 and parent1 != parent2:
                    if is_child(child, parent1, parent2):
                        result += similarity(child, parent1) * similarity(child, parent2)
    return result

assert part2(load_data(load('sample2'))) == 1245
print("Part 2: ", part2(load_data(load('notes2'))))


import networkx as nx

def part3(scales: list) -> int:
    G = nx.Graph()
    result = 0
    for c in range(len(scales)):
        child = scales[c]
        for p1 in range(len(scales) - 1):
            parent1 = scales[p1]
            for p2 in range(p1, len(scales)):
                parent2 = scales[p2]
                if child != parent1 and child != parent2 and parent1 != parent2:
                    if is_child(child, parent1, parent2):
                        # print(f'{c+1} is child of {p1+1} and {p2+1}')
                        G.add_edge(c + 1, p1 + 1)
                        G.add_edge(c + 1, p2 + 1)

    fam_number = 0
    fam_value = 0
    for component in nx.connected_components(G):
        if len(component) > fam_number:
            fam_number = len(component)
            fam_value = sum(component)

    return fam_value

assert part3(load_data(load('sample3-1'))) == 12
assert part3(load_data(load('sample3-2'))) == 36
print("Part 3: ", part3(load_data(load('notes3'))))
