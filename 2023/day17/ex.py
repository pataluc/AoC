"""Imports"""
from os import path
import sys
from collections import deque
import math
import regex as re
from colorama import Fore
# import numpy as np
from heapq import *
import cProfile

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False

def g_to_str(grid: list):
    return '\n'.join([''.join(line) for line in grid]) + "\n"

def pretty_print(grid, path):
    print('#' * len(grid[0]))
    for r, line in enumerate(grid):
        for c, char in enumerate(line):
            if (r, c) in path:
                print(Fore.RED + char, end='')
            else:
                print(Fore.WHITE + char, end='')
        print(Fore.WHITE + '')

def get_voisins(G, u, d):
    R = len(G)
    C = len(G[0])
    if DEBUG: print("#"*80 +"\non cherche les voisins de", u, ", chemin actuel", {k: v for k, v in d.items() if isinstance(v, int) or v[0]})
    precedents = []
    precedents_l = 0
    n = u
    for _ in range(4):
        if n in d and d[n][0] != u and d[n][0] not in precedents:
            if DEBUG: print(n, "found in d")
            precedents.append(d[n][0])
            precedents_l += 1
            n = d[n][0]
        else:
            # print(n, "NOT found in d")
            break
    if DEBUG: print('sommets précédents:', precedents)
                                                                                  
    r, c = u
    n = []
    for r2 in [r - 1, r + 1]:
        if 0 < r2 < R and (precedents_l < 4 or not all(map(lambda e: e[0] == r, precedents))):
            if precedents_l == 0 or (r2, c) != precedents[0]:
                n.append(((r2, c), int(G[r2][c])))

    for c2 in [c - 1, c + 1]:
        if 0 < c2 < C and (precedents_l < 4 or not all(map(lambda e: e[1] == c, precedents))):
            if precedents_l == 0 or (r, c2) != precedents[0]:
                n.append(((r, c2), int(G[r][c2])))

    if DEBUG: print('Voisins de', u, 'avec cout:', n)
    return n


def dijkstra(G, entree, sortie, infini=2 ** 30):
    C = len(G[0])
    R = len(G)

    marques = set()  # Contiendra le nom des sommets visités
 
    # Distance minimale trouvée pour chaque valeur dès le départ
    distances = {(i,j): (None, infini) for i in range(R) for j in range(C)}
    #     Sommet d'origine (None par défaut), distance
 
    distances[entree] = ((0,0), 0)  # On initialise la distance du départ
 
    # Nombre de sommets du graphe, longueur du dictionnaire
    taille_graph = R*C
 
    selection = entree
    coefficient = 0

    print(taille_graph)
 
    while len(marques) < taille_graph:
        if len(marques) % 1000 == 0: print(len(marques))
        # if len(marques) > 200: return False
        # On marque la 'selection'
        marques.add(selection)
        if DEBUG: print(f"On marque la sélection {selection} avec poids {coefficient}")
        # On parcours les voisins de 'selection'
        if DEBUG: print(selection)
        for voisin in get_voisins(G, selection, distances):
            # voisin est le couple (sommet, poids de l'arête)
 
            sommet = voisin[0]  # Le sommet qu'on, parcours
            poids = voisin[1]  # Le poids de selection au sommet
            if sommet not in marques:
                # Pour chaque voisin non marqué,
                # on compare coefficient + arête
                # avec la distance du dictionnaire
                d = distances[sommet][1]
                if coefficient + poids < d:
                    # Si c'est plus petit, on remplace
                    if DEBUG: print(f"Pour {sommet}, on remplace {distances[sommet]}", end='')
                    if DEBUG: print(f" par {(selection, coefficient + poids)}")
                    distances[sommet] = (selection, coefficient + poids)
 
        # On recherche le minimum parmi les non marqués
        minimum = (None, infini)
        for i in range(R):
            for j in range(C):
                sommet = (i,j)
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
    if DEBUG: print(parcours, longueur)
    pretty_print(G, parcours)
    return parcours, longueur

def ex1(data):
    """Compute ex answer"""
    G = [[c for c in row] for row in data.split('\n')]
    C = len(G[0])
    R = len(G)

    result = dijkstra(G, (0,0), (R - 1, C- 1))

    # if DEBUG: print(result)

    return result[1]

def ex2(data):
    """Compute ex answer"""
    G = [[c for c in row] for row in data.split('\n')]
    W = len(G[0])
    H = len(G)

    result = 0
    # start horiz
    for i in range(H):
        result = max(result, ex1(data, (i, -1), (0, 1)))
        result = max(result, ex1(data, (i, W), (0, -1)))
        
    # start vert
    for j in range(W):
        result = max(result, ex1(data, (-1, j), (1, 0)))
        result = max(result, ex1(data, (H, j), (-1, 0)))
    
    if DEBUG: print(result)
    return result


assert ex1(load("sample.txt")) == 102
print(f'ex1 : {ex1(load("input.txt"))}')
DEBUG = True

assert ex2(load("sample.txt")) == 51
print(f'ex2 : {ex2((load("input.txt")))}')
sys.exit()

