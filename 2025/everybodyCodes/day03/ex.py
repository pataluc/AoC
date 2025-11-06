from os import path
import sys

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

# Custo starts here

def load_data(data: str) -> tuple:
    """Loads data as a tuple"""
    return [int(s) for s in data.split(',')]

def part1(crates: list) -> int:
    return sum(set(crates))

assert part1([10,5,1,10,3,8,5,2,2]) == 29

print("Part 1: ", part1(load_data(load('notes1'))))

def part2(crates: list) -> int:
    mushroom = sorted(list(set(crates)), reverse = True)[-20:]
    return sum(mushroom)

assert part2(load_data(load('sample2'))) == 781

print("Part 2: ", part2(load_data(load('notes2'))))

def part3(crates: list) -> int:
    return max(crates.count(item) for item in set(crates))

assert part3(load_data(load('sample3'))) == 3

print("Part 3: ", part3(load_data(load('notes3'))))
