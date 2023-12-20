"""Imports"""
from os import path
# from copy import deepcopy
import sys
from collections import deque
# import math
# import regex as re
from colorama import Fore
# import numpy as np
# from heapq import *

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

DEBUG = False

def g_to_str(grid: list):
    """Printing grid"""
    return '\n'.join([''.join(line) for line in grid]) + "\n"

def pretty_print(grid, path_):
    """Pretty printing grid"""
    print('#' * len(grid[0]))
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if (row, col) in path_:
                print(Fore.RED + char, end='')
            else:
                print(Fore.WHITE + char, end='')
        print(Fore.WHITE + '')

LOW = 0
HIGH = 1

class Module():
    def __init__(self, children = []) -> None:
        self.children = children
        self.last_pulse_send = LOW
        self.highs = 0

    def set_last_pulse_send(self, pulse):
        self.last_pulse_send = pulse

    def inc_highs(self):
        self.highs += 1

    def __str__(self) -> str:
        return f"Childrens: {', '.join(self.children)}"

class Flipflop(Module):
    def __init__(self, children) -> None:
        super().__init__(children)
        self.state = False

    def flip(self) -> None:
        self.state = not self.state

class Conjunction(Module):
    def __init__(self, children) -> None:
        super().__init__(children)
        self.parents = []

    def add_parent(self, parent) -> None:
        self.parents.append(parent)

    def all_parents_high(self, modules) -> bool:
        return all([modules[parent].last_pulse_send == HIGH for parent in self.parents])

    def __str__(self) -> str:
        return f"Childrens: {', '.join(self.children)} Parents: {', '.join(self.parents)}"

def init_modules(data):
    """Reads data and return state"""
    modules_lines = [line.split(' -> ') for line in data.split('\n')]

    modules = {}
    for module_line in modules_lines:
        if module_line[0][0] == 'b':
            modules['broadcaster'] = Module(module_line[1].split(', '))
        elif module_line[0][0] == '%':
            modules[module_line[0][1:]] = Flipflop(module_line[1].split(', '))
        elif module_line[0][0] == '&':
            modules[module_line[0][1:]] = Conjunction(module_line[1].split(', '))

    for module_name, module_line in modules.items():
        for child in module_line.children:
            if DEBUG: print({name: str(module) for name, module in modules.items()})
            if DEBUG: print(child)
            if child in modules and isinstance(modules[child], Conjunction):
                modules[child].add_parent(module_name)
    return modules

def push_button(modules: dict, nb_pulses = [0,0]):
    pulses = deque()

    for module in modules:
        modules[module].highs = 0

    if DEBUG: print('button -low-> broadcaster')
    pulses.append(('broadcaster', LOW))
    nb_pulses[LOW] += 1

    while pulses:
        # print(Fore.GREEN, pulses)
        module, pulse = pulses.popleft()
        # print(Fore.BLUE, module, modules[module], Fore.WHITE)
        if module == 'broadcaster':
            for child in modules[module].children:
                if DEBUG: print(f'{module} -{"high" if pulse == HIGH else "low"}-> {child}')
                pulses.append((child, pulse))
                nb_pulses[pulse] += 1
        elif module in modules:
            modules[module]
            if isinstance(modules[module], Flipflop) and pulse == LOW:
                modules[module].flip()
                new_pulse = HIGH if modules[module].state else LOW
            elif isinstance(modules[module], Conjunction):
                new_pulse = LOW if modules[module].all_parents_high(modules) else HIGH
            elif isinstance(modules[module], Flipflop) and pulse == HIGH:
                continue

            if new_pulse == HIGH:
                modules[module].inc_highs()

            for child in modules[module].children:
                if DEBUG: print(f'{module} -{"high" if new_pulse else "low"}-> {child}')
                pulses.append((child, new_pulse))
                modules[module].set_last_pulse_send(new_pulse)

                nb_pulses[new_pulse] += 1
    # print(modules)
    return nb_pulses

def ex1(data):
    """Compute ex answer"""
    modules = init_modules(data)
    # print({name: str(module) for name, module in modules.items()})

    nb_pulses = [0, 0]
    for _ in range(1000):
        nb_pulses = push_button(modules, nb_pulses)

    if DEBUG: print(nb_pulses, nb_pulses[0] * nb_pulses[1])
    return nb_pulses[0] * nb_pulses[1]

def ex2(data):
    """Compute ex answer"""

    result = 1
    for bn_parent in ['pl', 'mz', 'lz', 'zm']:
        modules = init_modules(data)
        # print({name: str(module) for name, module in modules.items()})

        pushes = 1
        while True:
            push_button(modules)
            if modules[bn_parent].highs > 0:
                if DEBUG: print(modules[bn_parent].highs)
                break
            pushes += 1

        if DEBUG: print(pushes)
        result = result * pushes
    return result

assert ex1(load("sample.txt")) == 32000000
assert ex1(load("sample2.txt")) == 11687500
print(f'ex1 : {ex1(load("input.txt"))}')

# assert ex2(load("sample.txt")) == 167409079868000
print(f'ex2 : {ex2((load("input.txt")))}')
DEBUG = True

sys.exit()
