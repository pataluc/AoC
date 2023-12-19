"""Imports"""
from os import path
import sys
# from collections import deque
# import math
# import regex as re
from colorama import Fore
# import numpy as np
# import cProfile

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False

def g_to_str(grid: list):
    """Printing grid"""
    return '\n'.join([''.join(line) for line in grid]) + "\n"

def pretty_print(grid, path):
    """Pretty printing grid"""
    print('#' * len(grid[0]))
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if (row, col) in path:
                print(Fore.RED + char, end='')
            else:
                print(Fore.WHITE + char, end='')
        print(Fore.WHITE + '')

def get_voisins(grid, node, distances):
    """Get node neighbours"""
    ROWS = len(grid)
    COLS = len(grid[0])
    if DEBUG:
        print("#"*80 +"\non cherche les voisins de", node, ", chemin actuel",\
              {k: v for k, v in distances.items() if isinstance(v, int) or v[0]})
    precedents = []
    precedents_l = 0
    current_node = node
    for _ in range(4):
        if current_node in distances and \
            distances[current_node][0] != node \
                and distances[current_node][0] not in precedents:
            if DEBUG:
                print(current_node, "found in d")
            precedents.append(distances[current_node][0])
            precedents_l += 1
            current_node = distances[current_node][0]
        else:
            # print(n, "NOT found in d")
            break
    if DEBUG: print('sommets précédents:', precedents)

    row, col = node
    current_node = []
    for row2 in [row - 1, row + 1]:
        if 0 < row2 < ROWS \
            and (precedents_l < 4 \
                 or not all(map(lambda element: element[0] == row, precedents))):
            if precedents_l == 0 or (row2, col) != precedents[0]:
                current_node.append(((row2, col), int(grid[row2][col])))

    for col2 in [col - 1, col + 1]:
        if 0 < col2 < COLS \
            and (precedents_l < 4 \
                 or not all(map(lambda e: e[1] == col, precedents))):
            if precedents_l == 0 or (row, col2) != precedents[0]:
                current_node.append(((row, col2), int(grid[row][col2])))

    if DEBUG:
        print('Voisins de', node, 'avec cout:', current_node)
    return current_node


def dijkstra(grid, entree, sortie, infini=2 ** 30):
    """Dijkstra"""
    ROWS = len(grid)
    COLS = len(grid[0])

    marques = set()  # Contiendra le nom des sommets visités

    # Distance minimale trouvée pour chaque valeur dès le départ
    distances = {(row,col): (None, infini) for row in range(ROWS) for col in range(COLS)}
    # Sommet d'origine (None par défaut), distance

    distances[entree] = ((0, 0), 0)  # On initialise la distance du départ

    # Nombre de sommets du graphe, longueur du dictionnaire
    taille_graph = ROWS*COLS

    selection = entree
    coefficient = 0

    print(taille_graph)

    while len(marques) < taille_graph:
        if len(marques) % 1000 == 0: print(len(marques))
        # if len(marques) > 200: return False
        # On marque la 'selection'
        marques.add(selection)
        if DEBUG:
            print(f"On marque la sélection {selection} avec poids {coefficient}")
        # On parcours les voisins de 'selection'
        if DEBUG:
            print(selection)
        for voisin in get_voisins(grid, selection, distances):
            # voisin est le couple (sommet, poids de l'arête)

            sommet = voisin[0]  # Le sommet qu'on, parcours
            poids = voisin[1]  # Le poids de selection au sommet
            if sommet not in marques:
                # Pour chaque voisin non marqué,
                # on compare coefficient + arête
                # avec la distance du dictionnaire
                distance = distances[sommet][1]
                if coefficient + poids < distance:
                    # Si c'est plus petit, on remplace
                    if DEBUG:
                        print(f"Pour {sommet}, on remplace {distances[sommet]}", end='')
                    if DEBUG:
                        print(f" par {(selection, coefficient + poids)}")
                    distances[sommet] = (selection, coefficient + poids)

        # On recherche le minimum parmi les non marqués
        minimum = (None, infini)
        for row in range(ROWS):
            for col in range(COLS):
                sommet = (row,col)
                if sommet not in marques and distances[sommet][1] < minimum[1]:
                    minimum = (sommet, distances[sommet][1])

        # puis il devient notre nouvelle 'selection'
        selection, coefficient = minimum

    sommet = sortie
    parcours = [sortie]
    longueur = distances[sortie][1]
    # On parcours le graphe à l'envers pour obtenir le chemin
    while sommet != entree:
        sommet = distances[sommet][0]
        parcours.append(sommet)
    parcours.reverse()

    # On renvoie le chemin le plus court et la longueur
    if DEBUG:
        print(parcours, longueur)
    pretty_print(grid, parcours)
    return parcours, longueur

def ex1(data):
    """Compute ex answer"""
    grid = [[col for col in row] for row in data.split('\n')]
    ROWS = len(grid)
    COLS = len(grid[0])

    result = dijkstra(grid, (0,0), (ROWS - 1, COLS- 1))

    # if DEBUG: print(result)

    return result[1]

def ex2(data):
    """Compute ex answer"""
    grid = [[c for c in row] for row in data.split('\n')]
    ROWS = len(grid)
    COLS = len(grid[0])

    result = 0
    # start horiz
    for i in range(ROWS):
        result = max(result, ex1(data, (i, -1), (0, 1)))
        result = max(result, ex1(data, (i, COLS), (0, -1)))

    # start vert
    for j in range(COLS):
        result = max(result, ex1(data, (-1, j), (1, 0)))
        result = max(result, ex1(data, (ROWS, j), (-1, 0)))

    if DEBUG: print(result)
    return result


assert ex1(load("sample.txt")) == 102
print(f'ex1 : {ex1(load("input.txt"))}')
DEBUG = True

assert ex2(load("sample.txt")) == 51
print(f'ex2 : {ex2((load("input.txt")))}')
sys.exit()
