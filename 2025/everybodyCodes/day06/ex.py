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
    id, segments = data.split(':')

    return [int(id), list(map(int, segments.split(',')))]

def part1(professions: str) -> int:
    mentor_count = 0
    result = 0
    for i in list(professions):
        if i == 'A':
            mentor_count += 1
        elif i == 'a':
            result += mentor_count
    return result

assert part1(load('sample1')) == 5

print("Part 1: ", part1(load('notes1')))






def part2(professions: str) -> int:
    mentor_count = {}
    result = 0
    for i in list(professions):
        if i.isupper():
            if i not in mentor_count:
                mentor_count[i] = 1
            else:
                mentor_count[i] += 1
        elif i.islower() and i.upper() in mentor_count:
            result += mentor_count[i.upper()]
    return result

assert part2(load('sample2')) == 11

print("Part 2: ", part2(load('notes2')))


def part3(segment: str, times: int, distance: int) -> int:

    arrangement = segment * times

    result = 0
    for i in range(len(arrangement)):
        if arrangement[i].islower():
            result += arrangement[max(0, i - distance): min(len(arrangement), i + distance + 1)].count(arrangement[i].upper())
    return result



assert part3('AABCBABCABCabcabcABCCBAACBCa', 1, 10) == 34
assert part3('AABCBABCABCabcabcABCCBAACBCa', 2, 10) == 72
assert part3('AABCBABCABCabcabcABCCBAACBCa', 1000, 1000) == 3442321

print("Part 3: ", part3(load('notes3'), 1000, 1000))
