"""Imports"""
from __future__ import annotations
from os import path
import sys
from collections import deque, defaultdict

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> tuple:
    """Loads data as a tuple"""

    codes = [list(line) for line in data.split('\n')]

    return codes

DIRECTIONS = {
    (0, +1): '>',
    (+1, 0): 'v',
    (0, -1): '<',
    (-1, 0): '^'
}

def get_neighbours(graph, pos):
    """Get all neighbours of current in graph"""

    H = len(graph)
    W = len(graph[0])
    h, w = pos

    out = [(h+dh, w+dw) for dh, dw in DIRECTIONS.keys() if 0 <= h+dh < H and 0 <= w+dw<W and graph[h+dh][w+dw] != ' ']
    return out

def bfspaths(graph, start, end):
    """BFS algo which returns every shortest paths from start to end"""
    paths = []

    q = deque()
    visited = {start: 0}

    q.append([start])

    while q:
        current_path = q.popleft()
        node = current_path[-1]

        if node == end:
            paths.append(current_path)

        for n_node in get_neighbours(graph, node):
            if n_node not in visited \
                    or visited[n_node] >= len(current_path) + 1:
                newpath = current_path.copy()
                newpath.append(n_node)
                q.append(newpath)
                visited[n_node] = len(current_path) + 1

    shortest_paths = list(filter(lambda x: x[-1][1] == min(path[-1][1] for path in paths), paths))

    ans = []
    for p in shortest_paths:
        s = ''
        for i in range(len(p) - 1):
            s += DIRECTIONS[(p[i+1][0] - p[i][0], p[i+1][1] - p[i][1])]
        ans.append(s + 'A')

    # print(ans)
    return ans


DEBUG = False

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
numeric_keypad_graph = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [' ', '0', 'A']
]
numeric_memo = defaultdict(list)
for h1 in range(len(numeric_keypad_graph)):
    for w1 in range(len(numeric_keypad_graph[0])):
        for h2 in range(len(numeric_keypad_graph)):
            for w2 in range(len(numeric_keypad_graph[0])):
                if ' ' not in [numeric_keypad_graph[h1][w1], numeric_keypad_graph[h2][w2]]:
                    numeric_memo[(numeric_keypad_graph[h1][w1], numeric_keypad_graph[h2][w2])] = bfspaths(numeric_keypad_graph, (h1, w1), (h2, w2))

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+
directions_keypad_graph = [
    [' ', '^', 'A'],
    ['<', 'v', '>']
]
directions_memo = defaultdict(list)
for h1 in range(len(directions_keypad_graph)):
    for w1 in range(len(directions_keypad_graph[0])):
        for h2 in range(len(directions_keypad_graph)):
            for w2 in range(len(directions_keypad_graph[0])):
                if ' ' not in [directions_keypad_graph[h1][w1], directions_keypad_graph[h2][w2]]:
                    directions_memo[(directions_keypad_graph[h1][w1], directions_keypad_graph[h2][w2])] = bfspaths(directions_keypad_graph, (h1, w1), (h2, w2))

def get_shortest_sequence(code: str):
    """"""
    code = ['A'] + code

    num_ans = ['A']
    for i in range(len(code) - 1):
        new_num_ans = []
        for a in num_ans:
            for d in numeric_memo[(code[i], code[i+1])]:
                new_num_ans.append(a+d)
        num_ans = new_num_ans
    # print('num_ans: ', num_ans)

    best_cost = 2**30
    best = num_ans[0]
    for a in num_ans:
        cost = 0
        for i in range(len(a) - 1):
            cost += len(directions_memo[(a[i], a[i+1])][0])
        # print(f'a: {a}, cost: {cost}')
        if cost < best_cost:
            best = a
            best_cost = cost
    # print(f'best num_ans: {best}, cost: {best_cost}')

    dir_ans1 = ['A']
    for i in range(len(best) - 1):
        new_dir_ans1 = []
        for a in dir_ans1:
            for d in directions_memo[(best[i], best[i+1])]:
                new_dir_ans1.append(a+d)
        dir_ans1 = new_dir_ans1
    # print('dir_ans1: ', dir_ans1)

    best_cost = 2**30
    best = dir_ans1[0]
    for a in dir_ans1:
        cost = 0
        for i in range(len(a) - 1):
            cost += len(directions_memo[(a[i], a[i+1])][0])
        # print(f'a: {a}, cost: {cost}')
        if cost < best_cost:
            best = a
            best_cost = cost
    # print(f'best dir_ans1: {best}, cost: {best_cost}')

    dir_ans2 = ['A']
    for i in range(len(best) - 1):
        new_dir_ans2 = []
        for a in dir_ans2:
            for d in directions_memo[(best[i], best[i+1])]:
                new_dir_ans2.append(a+d)
        dir_ans2 = new_dir_ans2
    # print('dir_ans2: ', dir_ans2)
    # print(dir_ans2)

    best_cost = len(dir_ans2[0])
    best = dir_ans2[0]
    for a in dir_ans2:
        # print(f'a: {a}, cost: {len(a)}')
        if len(a) < best_cost:
            best = a
            best_cost = cost
    # print(f'best dir_ans2: {best}, cost: {best_cost}')

    # print(best)
    return best



def ex1(data: str) -> int:
    """Solve ex1"""

    codes = load_data(data)

    ans = 0
    for code in codes:
        shortest_sequence = get_shortest_sequence(code)[1:]
        print(f"{''.join(code)}: {shortest_sequence} (len: {len(shortest_sequence)})")
        ans += len(shortest_sequence) * int(''.join(code[:3]))
        # exit()

    print(ans)
    return ans

def ex2(data: str) -> int:
    """Solve ex1"""

    return 0

assert ex1(load("sample.txt")) == 126384
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt"), manhattan_max=20, delta=50) == 285
print(f'ex2 : {ex2(load("input.txt"), manhattan_max=20)}')


sys.exit()
