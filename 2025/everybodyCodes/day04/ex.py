from os import path
import sys
from math import ceil

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

# Custo starts here

def load_data(data: str) -> tuple:
    """Loads data as a tuple"""
    return list(map(int, data.split('\n')))
def load_data2(data: str) -> tuple:
    """Loads data as a tuple"""
    return data.split('\n')

def part1(gears: list) -> int:
    return 2025 * gears[0] // gears[-1]

assert part1(load_data(load('sample1-1'))) == 32400
assert part1(load_data(load('sample1-2'))) == 15888

print("Part 1: ", part1(load_data(load('notes1'))))

def part2(gears: list) -> int:
    value = ceil(10000000000000 * gears[-1] / gears[0])
    return value

assert part2(load_data(load('sample1-1'))) == 625000000000
assert part2(load_data(load('sample1-2'))) == 1274509803922

print("Part 2: ", part2(load_data(load('notes2'))))

def part3(gears: list) -> int:
    v = 100 * int(gears[0])
    for gear_couple in gears[1:-1]:
        g1, g2 = map(int, gear_couple.split('|'))
        v = v * g2 // g1
    v = v // int(gears[-1])
    return v

assert part3(load_data2(load('sample3-1'))) == 400
assert part3(load_data2(load('sample3-2'))) == 6818

print("Part 3: ", part3(load_data2(load('notes3'))))
