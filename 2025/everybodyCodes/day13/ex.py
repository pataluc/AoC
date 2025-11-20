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
    return [int(line) for line in data.split('\n')]

def part1(numbers: list) -> int:
    wheel = deque([1])
    for i, number in enumerate(numbers):
        if i % 2 == 0:
            wheel.append(number)
        else:
            wheel.appendleft(number)

    while wheel[0] != 1:
        number = wheel.popleft()
        wheel.append(number)

    result = wheel[2025 % len(wheel)]
    return result

assert part1(load_data(load('sample1'))) == 67
print("Part 1: ", part1(load_data(load('notes1'))))


def load_data2(data: str) -> tuple:
    """Loads data as a tuple"""
    lines = [list(map(int, line.split('-'))) for line in data.split('\n')]
    assert all([x < y for x, y in lines])

    return lines

def part2(numbers: list, times : int = 20252025) -> int:
    clockwise = [1]
    counterclockwise = []
    for i, (m, M) in enumerate(numbers):
        if i % 2 == 0:
            clockwise += list(range(m, M+1))
        else:
            counterclockwise += list(range(m, M+1))
    wheel = clockwise + counterclockwise[::-1]

    while wheel[0] != 1:
        number = wheel.popleft()
        wheel.append(number)

    result = wheel[times % len(wheel)]
    return result

assert part2(load_data2(load('sample2'))) == 30
print("Part 2: ", part2(load_data2(load('notes2'))))

print("Part 3: ", part2(load_data2(load('notes3')), 202520252025))
