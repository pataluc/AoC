"""Imports"""
from __future__ import annotations
from collections import  defaultdict
from colorama import Fore

R = 5
C = 4

def pretty_print(grid):
    """Pretty printing grid"""
    print('#' * C)
    for row, line in enumerate(grid.split('\n')):
        for col, char in enumerate(line):
            if char == 's':
                print(Fore.RED + char, end='')
            elif char in ['V', 'v', 'h']:
                print(Fore.WHITE + char, end='')
            elif char == 'p':
                print(Fore.BLUE + char, end='')
            else:
                print(Fore.WHITE + char, end='')
        print(Fore.WHITE + '')

def board_to_string(b: list):
    return '\n'.join(''.join(line) for line in b)

def string_to_board(s: str):
    return [list(line) for line in s.split('\n')]

def get_neighbours(state: str):
    board = string_to_board(state)
    neighbours = set()

    for r in range(R):
        for c in range(C):
            if board[r][c] == ' ':
                for i, j in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                    # Point vide seul, on tente de bouger un pion simple à côté
                    if 0 <= r + i < R and 0 <= c + j < C and board[r+i][c+j] == 'p':
                        b2 = string_to_board(state)
                        b2[r+i][c+j] = ' '
                        b2[r][c] = 'p'
                        neighbours.add(board_to_string(b2))

                    # Point vide seul, on tente de bouger hh à droite ou gauche
                    if c > 1 and board[r][c-2] == 'h' and board[r][c-1] == 'h':
                        b2 = string_to_board(state)
                        b2[r][c-2] = ' '
                        b2[r][c] = 'h'
                        neighbours.add(board_to_string(b2))
                    if c < C - 2 and board[r][c+1] == 'h' and board[r][c+2] == 'h':
                        b2 = string_to_board(state)
                        b2[r][c] = 'h'
                        b2[r][c+2] = ' '
                        neighbours.add(board_to_string(b2))

                    # Point vide seul, on tente de bouger vv en haut ou en bas
                    if r > 1 and board[r-2][c] == 'V' and board[r-1][c] == 'v':
                        b2 = string_to_board(state)
                        b2[r-2][c] = ' '
                        b2[r-1][c] = 'V'
                        b2[r][c] = 'v'
                        neighbours.add(board_to_string(b2))
                    if r < R - 2 and board[r+1][c] == 'V' and board[r+2][c] == 'v':
                        b2 = string_to_board(state)
                        b2[r][c] = 'V'
                        b2[r+1][c] = 'v'
                        b2[r+2][c] = ' '
                        neighbours.add(board_to_string(b2))
                
                    # 2 points vides contigus horizontaux, on cherche à bouger hh ou ssss
                    if c < C - 1 and board[r][c+1] == ' ':
                        for i in [-1, 1]:
                            if 0 <= r + i < R and board[r+i][c] == 'h' and board[r+i][c+1] == 'h':
                                b2 = string_to_board(state)
                                b2[r][c] = 'h'
                                b2[r][c+1] = 'h'
                                b2[r+i][c] = ' '
                                b2[r+i][c+1] = ' '
                                neighbours.add(board_to_string(b2))
                            if 1 <= r + i < R - 1 and board[r+i][c] == 's' and board[r+i][c+1] == 's':
                                b2 = string_to_board(state)
                                b2[r][c] = 's'
                                b2[r][c+1] = 's'
                                b2[r+2*i][c] = ' '
                                b2[r+2*i][c+1] = ' '
                                neighbours.add(board_to_string(b2))
                
                    # 2 points vides contigus verticaux, on cherche à bouger Vv ou ssss
                    if r < R - 1 and board[r+1][c] == ' ':
                        for j in [-1, 1]:
                            if 0 <= c + j < C and board[r][c+j] == 'V' and board[r+1][c+j] == 'v':
                                b2 = string_to_board(state)
                                b2[r][c] = 'V'
                                b2[r+1][c] = 'v'
                                b2[r][c+j] = ' '
                                b2[r+1][c+j] = ' '
                                neighbours.add(board_to_string(b2))
                            if 1 <= c + j < C - 1 and board[r][c+j] == 's' and board[r+1][c+j] == 's':
                                b2 = string_to_board(state)
                                b2[r][c] = 's'
                                b2[r+1][c] = 's'
                                b2[r][c+2*j] = ' '
                                b2[r+1][c+2*j] = ' '
                                neighbours.add(board_to_string(b2))
    return neighbours
    
init_state = [['V', 's', 's', 'V'],
              ['v', 's', 's', 'v'],
              ['V', 'h', 'h', 'V'],
              ['v', 'p', 'p', 'v'],
              [' ', 'p', 'p', ' ']]

def dfs(start):
    start = board_to_string(start)
    stack = [(start, [start])]  # Utilise une pile pour suivre le chemin
    visited = set()  # Pour suivre les nœuds déjà visités

    while stack:
        current, path = stack.pop()

        if current[17] == current[18] == 's':
            return path  # Retourne le chemin si le sommet recherché est atteint

        if current not in visited:
            visited.add(current)
            for neighbour in get_neighbours(current):
                if neighbour not in visited:
                    stack.append((neighbour, path + [neighbour]))

    return None  # Retourne None si le sommet recherché n'est pas atteint


def _deconstruct_path(tentative_parents, end):
    if end not in tentative_parents:
        return None
    cursor = end
    path = []
    while cursor:
        path.append(cursor)
        cursor = tentative_parents.get(cursor)
    return list(reversed(path))

def dijkstra(start):
    """
    Calculate the shortest path for a directed weighted graph.

    Node can be virtually any hashable datatype.

    :param start: starting node
    :param end: ending node
    :param weighted_graph: {"node1": {"node2": "weight", ...}, ...}
    :return: ["START", ... nodes between ..., "END"] or None, if there is no
            path
    """
    start = board_to_string(start)

    # We always need to visit the start
    nodes_to_visit = {start}
    visited_nodes = set()
    distance_from_start = defaultdict(lambda: float("inf"))
    # Distance from start to start is 0
    distance_from_start[start] = 0
    tentative_parents = {}
    current = None

    while nodes_to_visit:
        # The next node should be the one with the smallest weight
        current = min(
            [(distance_from_start[node], node) for node in nodes_to_visit]
        )[1]
        # The end was reached
        if current[21] == current[22] == 's':
            break

        nodes_to_visit.discard(current)
        visited_nodes.add(current)
        for neighbour in get_neighbours(current):
            if neighbour in visited_nodes:
                continue
            neighbour_distance = distance_from_start[current] + 1
            if neighbour_distance < distance_from_start[neighbour]:
                distance_from_start[neighbour] = neighbour_distance
                tentative_parents[neighbour] = current
                nodes_to_visit.add(neighbour)

    path = _deconstruct_path(tentative_parents, current)
    return path

result = dijkstra(init_state)

if result:
    print(f"Chemin : ")
    for n in result:
        pretty_print(n)
else:
    print(f"Le chemin n'existe pas.")


# queue = deque()
# queue.append(board_to_string(init_state))
# seen = set()

# while queue:
#     current = queue.popleft()
#     if current not in seen:
#         seen.add(current)
#         for neighbour in get_neighbours(current):
#             if neighbour not in seen:
#                 queue.append(neighbour)