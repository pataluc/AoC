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
        for j in range(1, i):
            x1, x2 = nails[i-1], nails[i]
            y1, y2 = nails[j-1], nails[j]
            if (x1 not in [y1, y2] and x2 not in [y1, y2]) and ((y1 < x1 < y2 or y2 < x1 < y1) ^ (y1 < x2 < y2 or y2 < x2 < y1)):
                result += 1
    return result

assert part2([1,5,2,6,8,4,1,7,3,5,7,8,2], 8) == 21
print("Part 2: ", part2(load_data(load('notes2')), 256))



def part3(nails: list, nail_numbers: int) -> int:
    result = 0
    for x1 in range(1, nail_numbers):
        for x2 in range(x1 + 1, nail_numbers + 1):
            temp = 0
            for j in range(1, len(nails)):
                y1, y2 = nails[j-1], nails[j]
                if (x1 not in [y1, y2] and x2 not in [y1, y2]) and ((y1 < x1 < y2 or y2 < x1 < y1) ^ (y1 < x2 < y2 or y2 < x2 < y1)):
                    temp += 1
                if (x1 in [y1, y2] and x2 in [y1, y2]):
                    temp += 1
            result = max(result, temp)
    print(result)
    return result

assert part3([1,5,2,6,8,4,1,7,3,6], 8) == 7
print("Part 3: ", part3(load_data(load('notes3')), 256))
