

"""Imports"""
from __future__ import annotations
from os import path
import sys
import math
# import regex as re
from z3 import *


def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> list:
    """Loads data as a tuple"""

    return data.splitlines()

def read_machine(machine: str) -> tuple[str, list[set[int]], list[int]]:
    # desired, buttons, joltages = re.findall(r'\[(.+)\] (.*) {(.*)}', machine)[0]
    desired, buttonsjoltages = machine.split('] (')
    buttons, joltages = buttonsjoltages.split(') {')

    r = (
        desired[1:],
        [ {int(button) for button in bg.split(',')} for bg in buttons.split(') (')],
        [ int(joltage) for joltage in joltages[:-1].split(',')]
        )
    return r

def toggle1(current: str, buttons: set[int]) -> str:
    r = ''
    for i in range(len(current)):
        if i in buttons:
            r += '#' if current[i] == '.' else '.'
        else:
            r += current[i]
    return r

def get_neighbours1(current: str, buttons: list[set[int]]):
    return [toggle1(current, bg) for bg in buttons]

def solve_machine1(machine: tuple[str, list[set[int]], list[int]]) -> int:
    desired, buttons, _ = machine
    start = '.' * len(desired)

    #BFS
    queue = []
    queue.append(start)
    visited = {}
    visited[start] = 0

    while len(queue):
        current = queue.pop(0)
        for neighbour in get_neighbours1(current, buttons):
            if neighbour == desired:
                return visited[current] + 1
            elif neighbour not in visited:
                queue.append(neighbour)
                visited[neighbour] = visited[current] + 1

def ex1(data: str) -> int:
    """Solve ex1"""
    machines = load_data(data)
    result = 0

    for machine in machines:
        result += solve_machine1(read_machine(machine))

    return result


def toggle2(current: list[int], buttons: list[int]) -> str:
    return [current[i] + (1 if i in buttons else 0) for i in range(len(current))]

def get_neighbours2(current: str, buttons: list[list[int]], desired: tuple[int]):
    r = []

    for bg in buttons:
        rb = []
        for i in range(len(current)):
            new = current[i] + (1 if i in bg else 0)
            if new > desired[i]:
                break
            rb.append(new)
        else:
            r.append(tuple(rb))

    return r

def solve_machine2(machine: tuple[str, list[set[int]], list[int]]) -> int:
    _, buttons, desired = machine

    s = Optimize()

    ints = []
    for i in range(len(buttons)):
        ivar = Int("i%d" % i)
        ints.append(ivar)
        s.add(ivar>=0)

    for i, goal in enumerate(desired):
        addition = [ints[j] for j, bg in enumerate(buttons) if i in bg]
        s.add(sum(addition) == desired[i])
    s.minimize(sum(ints))
    s.check()
    m = s.model()

    result = sum([m.evaluate(v).as_long() for v in ints])
    return result

def ex2(data: str) -> int:
    """Solve ex2"""
    machines = load_data(data)
    result = 0

    for machine in machines:
        s = solve_machine2(read_machine(machine))
        result += s
    return result

assert ex1(load("sample.txt")) == 7
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2(load("sample.txt")) == 33
print(f'ex2 : {ex2(load("input.txt"))}')
sys.exit()

