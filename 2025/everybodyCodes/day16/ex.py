from os import path
import sys
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
    return [int(v) for v in data.split(',')]


def part1(values: list) -> int:
    result = 0
    for i in range(90):
        result += sum([1 for v in values if (i+1) % v == 0])

    return result

def part2(values: list) -> int:
    # soluce = [1, 2, 4, 9, 13]
    # for i in range(len(values)):
    #     print(values[i], end=',')
    # print()
    # for i in range(len(values)):
    #     print(values[i] - sum([1 for v in soluce if (i+1) % v == 0]), end=',')

    soluce = []
    while sum(values) > 0:
        new_soluce = values.index(1) + 1

        for i in range(len(values)):
            if (i + 1) % new_soluce == 0:
                values[i] = values[i] - 1


        soluce.append(new_soluce)

    result = 1
    for v in soluce:
        result *= v
    return result

assert part1(load_data(load('sample1'))) == 193
print("Part 1: ", part1(load_data(load('notes1'))))

assert part2(load_data(load('sample2'))) == 270
print("Part 2: ", part2(load_data(load('notes2'))))

exit()
print("Part 3: ", part2(load_data2(load('notes3')), 202520252025))
