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

def part1(segments: list) -> int:
    spine = {0: segments[0]}
    lefts = {}
    rights = {}

    for segment in segments[1:]:
        exited = False
        for i in sorted(spine.keys()):
            if segment < spine[i] and i not in lefts:
                lefts[i] = segment
                exited = True
                break
            elif segment > spine[i] and i not in rights:
                rights[i] = segment
                exited = True
                break
        if exited:
            continue

        spine[max(spine.keys()) + 1] = segment
    result = ''.join(map(str, spine.values()))
    return result

assert part1(load_data(load('sample1'))[1]) == '581078'

print("Part 1: ", part1(load_data(load('notes1'))[1]))






def part2(data: str) -> int:
    swords = [load_data(line) for line in data.splitlines()]

    min = max = int(part1(swords[0][1]))
    for _, segments in swords[1:]:
        r = int(part1(segments))
        if r < min:
            min = r
        elif r > max:
            max = r

    # print(min, max, max - min)
    return max - min

assert part2(load('sample2')) == 77053

print("Part 2: ", part2(load('notes2')))





def sword_value3(segments: list) -> int:
    spine = {0: segments[0]}
    lefts = {}
    rights = {}

    for segment in segments[1:]:
        exited = False
        for i in sorted(spine.keys()):
            if segment < spine[i] and i not in lefts:
                lefts[i] = segment
                exited = True
                break
            elif segment > spine[i] and i not in rights:
                rights[i] = segment
                exited = True
                break
        if exited:
            continue

        spine[max(spine.keys()) + 1] = segment

    result = [int(''.join(map(str, spine.values())))]
    for i in sorted(spine.keys()):
        l = str(lefts[i]) if i in lefts else ''
        l += str(spine[i])
        l += str(rights[i]) if i in rights else ''
        result.append(int(l))
    return result



def part3(data: str) -> int:
    swords = [load_data(line) for line in data.splitlines()]

    swords = sorted([sword_value3(sword[1]) + [sword[0]] for sword in swords], reverse=True)

    # print(swords)
    result = 0
    for i in range(len(swords)):
        result += (i+1) * swords[i][-1]
    return result



assert part3(load('sample3-1')) == 260
assert part3(load('sample3-2')) == 4

print("Part 3: ", part3(load('notes3')))
