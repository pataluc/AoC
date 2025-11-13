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
    return list(map(int, data.split(',')))

def part1(nails: list, nail_numbers: int) -> int:
    result = 0
    for i in range(len(nails)):
        if 2*abs(nails[i-1]-nails[i]) == nail_numbers:
            result += 1
    return result

assert part1([1,5,2,6,8,4,1,7,3], 8) == 4
print("Part 1: ", part1(load_data(load('notes1')), 32))

def part2(nails: list, nail_numbers: int) -> int:
    result = 0
    for i in range(3, len(nails)):
        for j in range(1, i - 1):
            if 2*abs(nails[i-1]-nails[i]) == nail_numbers:
                result += 1
    return result

assert part2([1,5,2,6,8,4,1,7,3,5,7,8,2], 8) == 21

print("Part 2: ", part2(load_data(load('notes2'))))

def part3(crates: list) -> int:
    return max(crates.count(item) for item in set(crates))

assert part3(load_data(load('sample3'))) == 3

print("Part 3: ", part3(load_data(load('notes3'))))
