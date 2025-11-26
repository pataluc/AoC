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
    return [list(line) for line in data.split('\n')]


def part1(values: list, rr: int = 10) -> int:
    R = len(values)
    C = len(values[0])

    vr = R // 2
    vc = C // 2

    result = 0
    for r in range(R):
        for c in range(C):
            if ((vr-r)**2 + (vc-c)**2) <= rr ** 2 and (r, c) != (vr, vc):
                result += int(values[r][c])
    #             print('X', end='')
    #         elif (r, c) == (vr,vc):
    #             print('@', end='')
    #         else:
    #             print('.', end='')
    #     print()


    # print(result)

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


# assert part1(load_data(load('sample1'))) == 1573
# print("Part 1: ", part1(load_data(load('notes1'))))

assert part2(load_data(load('sample2'))) == 1090
print("Part 2: ", part2(load_data(load('notes2'))))

exit()
print("Part 3: ", part2(load_data2(load('notes3')), 202520252025))
