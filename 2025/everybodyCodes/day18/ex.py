from os import path
import sys
import re
from collections import deque

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

# Custo starts here
def load_data(data: str) -> tuple:
    """Loads data as a tuple"""

    plants = {}
    branches = {}
    for block in data.split('\n\n'):
        lines = block.splitlines()
        plant_n, plant_thickness = [int(s) for s in re.findall(r'\d+', lines[0])]
        plants[plant_n] = plant_thickness

        for line in lines[1:]:
            if 'free' not in line:
                branched_plant_n, branch_thickness = [int(s) for s in re.findall(r'\d+', line)]
                branches[plant_n] = (branched_plant_n, branch_thickness)

    return [plants, branches]

def part1(plants: dict, branches: dict) -> int:
    energy = {}

    while True:
        for plant in plants.keys():
            if plant not in energy:


        exit()


    return result

def part2(values: list) -> int:
    previously = 0
    maxd = 0
    id = 0
    for i in range(1, 100):
        destroyed = part1(values, i)
        if destroyed-previously > maxd:
            maxd = destroyed-previously
            id = i
        previously = destroyed

    return id * maxd


assert part1(*load_data(load('sample1'))) == 774
print("Part 1: ", part1(*load_data(load('notes1'))))

assert part2(load_data(load('sample2'))) == 1090
print("Part 2: ", part2(load_data(load('notes2'))))

exit()
print("Part 3: ", part2(load_data2(load('notes3')), 202520252025))
