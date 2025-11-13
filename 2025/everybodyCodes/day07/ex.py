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
    names, rules = data.split('\n\n')

    return [names.split(','), {rule.split(' > ')[0]: rule.split(' > ')[1].split(',') for rule in rules.split('\n')}]

def valid_name(name: str, rules: list) -> bool:
    # print(name, rules)
    for i in range(len(name) - 1):
        if name[i] in rules.keys() and name[i + 1] not in rules[name[i]]:
            return False
    return True

def part1(names: list, rules: list) -> str:
    for name in names:
        if valid_name(name, rules):
            # print(name)
            return name

assert part1(*load_data(load('sample1'))) == 'Oroneth'
print("Part 1: ", part1(*load_data(load('notes1'))))




def part2(names: list, rules: list) -> int:
    result = 0
    for i, name in enumerate(names):
        if valid_name(name, rules):
            result += i + 1
    return result

assert part2(*load_data(load('sample2'))) == 23
print("Part 2: ", part2(*load_data(load('notes2'))))

def generate_valid_names(prefix: str, rules: list) -> set:
    valid_names = set()
    to_visit = [prefix]
    while to_visit:
        name = to_visit.pop()
        if 7 <= len(name) <= 11:
            valid_names.add(name)
        if len(name) < 11:
            if name[-1] in rules.keys():
                for next_char in rules[name[-1]]:
                    to_visit.append(name + next_char)
    # print('\n'.join(valid_names))
    return valid_names


def part3(prefixes: list, rules: list) -> int:
    names = set()

    for prefix in prefixes:
        if valid_name(prefix, rules):
            names.update(generate_valid_names(prefix, rules))

    return len(names)


assert part3(*load_data(load('sample3-1'))) == 25
assert part3(*load_data(load('sample3-2'))) == 1154

print("Part 3: ", part3(*load_data(load('notes3'))))

exit()