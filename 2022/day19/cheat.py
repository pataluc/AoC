from itertools import islice
from collections import deque
from utils import *

from typing import (
    Callable,
    Collection,
    Iterable,
    Iterator,
)

NAMES = {
    'ore': 0,
    'clay': 1,
    'obsidian': 2,
    'geode': 3,
}

def lmap(func: Callable, sequence: Iterable) -> list:
    """
    >>> lmap(int, "12345")
    [1, 2, 3, 4, 5]
    """
    return list(map(func, sequence))

inf = float('inf')
GEODE = NAMES['geode']

def iter_chunks(s: Collection, n: int) -> Iterator:
    """
    >>> list(iter_chunks("123456789", 3))
    ['123', '456', '789']
    >>> list(iter_chunks([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))
    [[1, 2], [3, 4], [5, 6], [7, 8]]
    """
    for i in range(0, len(s) - n + 1, n):
        yield s[i: i + n]

def tuple_from_dict(d):
    return tuple(d.get(k, 0) for k in NAMES)


def read_data(filename):
    with open(filename, 'r') as f:
        data = f.read()

    parts = data.strip().split('.')
    for chunk in iter_chunks(parts, 4):
        chunk = lmap(str.strip, '.'.join(chunk).split(':')[1].split('.'))
        rules = [None, None, None, None]
        limits = [0, 0, 0, inf]
        for rule in chunk:
            _, robot_name, _, *parts = rule.split(' ')

            parts = {
                part_name: int(amount)
                for _, amount, part_name in iter_chunks(parts, 3)
            }

            for part_name, amount in parts.items():
                robot_num = NAMES[part_name]
                limits[robot_num] = max(limits[robot_num], amount)

            robot_num = NAMES[robot_name]
            rules[robot_num] = tuple_from_dict(parts)

        yield rules, limits


def can_build(parts, rule):
    return all(have >= need for have, need in zip(parts, rule))


def spend(parts, rule):
    return tuple(
        have - need
        for have, need in zip(parts, rule)
    )


def build(robots, num):
    return tuple(
        have + (i == num)
        for i, have in enumerate(robots)
    )


def gather(parts, robots):
    return tuple(
        have + robot
        for have, robot in zip(parts, robots)
    )


def waste(parts, limits):
    return tuple(
        min(part, 2 * cap)
        for part, cap in zip(parts, limits)
    )


def process_blueprint(rules, limits, turns):
    queue = deque()
    initial = ((1, 0, 0, 0), (0, 0, 0, 0))
    queue.append(initial)
    time = 0
    visited = set()
    while queue and time < turns:
        for _ in range(len(queue)):
            state = queue.popleft()
            if state in visited:
                continue
            visited.add(state)
            robots, parts = state
            # Assumption 1: if we can build a geode, we do
            if can_build(parts, rules[GEODE]):
                new_parts = waste(gather(spend(parts, rules[GEODE]), robots), limits)
                new_robots = build(robots, GEODE)
                queue.append((new_robots, new_parts))
            else:
                for robot_num, rule in enumerate(rules):
                    # Assumption 2: if we produce enough of a resource, we don't build more robots of that kind
                    if robots[robot_num] >= limits[robot_num]:
                        continue
                    if can_build(parts, rule):
                        new_parts = waste(gather(spend(parts, rule), robots), limits)
                        new_robots = build(robots, robot_num)
                        queue.append((new_robots, new_parts))
                # Assumption 3: if we have too much of resource, we just waste it
                new_parts = waste(gather(parts, robots), limits)
                queue.append((robots, new_parts))
        time += 1

    res = 0
    for state in queue:
        robots, parts = state
        res = max(res, parts[GEODE])
    return res


def task1(filename, turns):
    result = 0
    for num, (rules, limits) in enumerate(read_data(filename), 1):
        # print(num, limits, rules)
        result += num * process_blueprint(rules, limits, turns)
    return result


def task2(filename, turns):
    result = 1
    for rules, limits in islice(read_data(filename), 3):
        result *= process_blueprint(rules, limits, turns)
    return result


assert task1('sample.txt', 24) == 33
print(task1('input.txt', 24))
assert task2('sample.txt', 32) == 3472
print(task2('input.txt', 32))
