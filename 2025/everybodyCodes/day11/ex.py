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
    return [int(line) for line in data.split('\n')]

# def shift_cols(cols: list, reverse = False)

def part1(cols: list) -> int:
    rounds = 0

    while cols != sorted(cols):
        for i in range(len(cols) - 1):
            if cols[i] > cols[i+1]:
                cols[i] -= 1
                cols[i+1] += 1
        rounds += 1
        if rounds == 10:
            return sum([(idx+1) * value for idx, value in enumerate(cols)])


    while cols != sorted(cols, reverse = True):
        for i in range(len(cols) - 1):
            if cols[i] < cols[i+1]:
                cols[i] += 1
                cols[i+1] -= 1
        rounds += 1
        if rounds == 10:
            return sum([(idx+1) * value for idx, value in enumerate(cols)])

    return 0

assert part1(load_data(load('sample1'))) == 109
print("Part 1: ", part1(load_data(load('notes1'))))




def part2(cols: list) -> int:
    rounds = 0

    while cols != sorted(cols):
        for i in range(len(cols) - 1):
            if cols[i] > cols[i+1]:
                cols[i] -= 1
                cols[i+1] += 1
        rounds += 1
        # print(cols, sum([(idx+1) * value for idx, value in enumerate(cols)]))

    while cols != sorted(cols, reverse = True):
        for i in range(len(cols) - 1):
            if cols[i] < cols[i+1]:
                cols[i] += 1
                cols[i+1] -= 1
        rounds += 1
        # print(cols, sum([(idx+1) * value for idx, value in enumerate(cols)]))
    return rounds

assert part2(load_data(load('sample1'))) == 11
assert part2(load_data(load('sample2'))) == 1579
print("Part 2: ", part2(load_data(load('notes2'))))


def part3(cols: list) -> int:
    assert cols == sorted(cols)

    target = sum(cols) // len(cols)
    return sum(target - num for num in cols if num < target)

# assert part3(load_data(load('sample3-1'))) == 12
# assert part3(load_data(load('sample3-2'))) == 36
print("Part 3: ", part3(load_data(load('notes3'))))
