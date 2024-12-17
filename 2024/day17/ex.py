"""Imports"""
from __future__ import annotations
from os import path
# from copy import deepcopy
import sys
from collections import defaultdict, deque
# import math
import re
# from colorama import Fore
# import numpy as np
# from heapq import *
# import networkx as nx
# import functools
# from sympy import solve, symbols, Eq

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> tuple[list, list]:
    """Loads data as a tuple"""

    registers, prgm = data.split('\n\n')

    return [int(r[12:]) for r in registers.split('\n')], list(map(int,  prgm[9:].split(',')))

DEBUG = False

def run(registers: list, prgm: list) -> str:
    ans = []
    A, B, C = 0, 1, 2
    instruction_pointer = 0

    while instruction_pointer < len(prgm):
        opcode = prgm[instruction_pointer]
        literal_operand = prgm[instruction_pointer + 1]
        combo_operand = literal_operand if literal_operand < 4 else registers[literal_operand - 4]

        if DEBUG: 
            print('\n=======================')
            print("Pointer: %d" % instruction_pointer, ", register: ", registers)
            print("Applying opcode %d to literal_operand %d (combo_operand: %d)" % (opcode, literal_operand, combo_operand))

        if opcode == 0: # adv, division A / 2 ** operand_value -> A
            v = registers[A] // (2**combo_operand)
            if DEBUG: print("writing %d in A" % v)
            registers[A] = v
        elif opcode == 1: # bxl, B XOR literal -> B
            v = registers[B] ^ literal_operand
            if DEBUG: print("writing %d in B" % v)
            registers[B] = v
        elif opcode == 2: # bst, combo modulo 8 -> B
            v = combo_operand % 8
            if DEBUG: print("writing %d in B" % v)
            registers[B] = v
        elif opcode == 3: # jnz, nothing if A = 0 else jumps to literal
            if registers[A] != 0:
                instruction_pointer = literal_operand
                if DEBUG: print("jumping to %d" % literal_operand)
                continue
        elif opcode == 4: # bxc B XOR C -> B
            v = registers[B] ^ registers[C]
            if DEBUG: print("writing %d in B" % v)
            registers[B] = v
        elif opcode == 5: # out
            v = combo_operand % 8
            if DEBUG: print("outputing %d" % v)
            ans.append(v)
        elif opcode == 6: # bdv, division A / 2 ** operand_value -> B
            v = registers[A] // (2**combo_operand)
            if DEBUG: print("writing %d in B" % v)
            registers[B] = v
        elif opcode == 7: # adv, division A / 2 ** operand_value -> C
            v = registers[A] // (2**combo_operand)
            if DEBUG: print("writing %d in C" % v)
            registers[C] = v

        instruction_pointer += 2

    return ans

def ex1(data: str) -> int:
    """Solve ex1"""
    registers, prgm = load_data(data)

    return ','.join(map(str, run(registers, prgm)))

def ex2(data: str):
    registers, prgm = load_data(data)
    ##################
    #   164542125272765
    i = 164542124634108
    while True:
        registers[0] = i
        res = run(registers, prgm)
        if res == prgm:
            return i
        # print(i, res, prgm)
        # if res[-1] == 0 and res[-2] == 3 and res[-3] == 5: print(i, res, prgm, len(res), len(prgm))
        if i % 500 == 0 : print(i, res, prgm, len(res), len(prgm))
        i += 1


# assert ex1(load("sample.txt")) == '4,6,3,5,6,3,5,2,1,0'
# print(f'ex1 : {ex1(load("input.txt"))}')

# DEBUG = True
# assert ex2(load("sample2.txt")) == 117440
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()
