"""Imports"""
from __future__ import annotations
from os import path
import sys
from collections import deque, defaultdict
from itertools import combinations

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

def load_data(data: str) -> tuple[dict[str: str], dict[str: list]]:
    """Loads data as a tuple"""

    wires, gates = data.split('\n\n')

    wires = {line.split(': ')[0]: line.split(': ')[1] for line in wires.split('\n')}
    # print(init_wires)

    gates = {line.split()[4]: tuple(line.split()[0:3]) for line in gates.split('\n')}

    return wires, gates

def apply_op(a:str, op: str, b: str) -> str:
    """Apply one single operation"""
    if op =='AND':
        return '1' if a == '1' and b == '1' else '0'
    elif op == 'OR':
        return '1' if a == '1' or b == '1' else '0'
    else: # op == XOR
        return '1' if a != b else '0'


def apply_gate(wires: dict, gates: dict, gate: str) -> str:
    """Apply gate recursively"""

    a, op, b = gates[gate]

    return apply_op(
        wires[a] if a in wires else apply_gate(wires, gates, a),
        op,
        wires[b] if b in wires else apply_gate(wires, gates, b)
    )

def get_involved_gates(wires: dict, gates: dict, gate: str, involved: set = set()) -> set[str]:
    """Returns gates involved in wrong result"""

    a, _, b = gates[gate]
    involved.add(a)
    involved.add(b)

    if a not in wires:
        involved = involved.union(get_involved_gates(wires, gates, a, involved))
    if b not in wires:
        involved = involved.union(get_involved_gates(wires, gates, b, involved))

    return involved


def ex1(data: str) -> int:
    """Solve ex1"""

    wires, gates = load_data(data)

    ans = ''
    for gate in sorted(filter(lambda g: g.startswith('z'), gates.keys()), reverse=True):
        ans += apply_gate(wires, gates, gate)

    ans = int(ans, 2)
    return ans


def ex2(data: str) -> int:
    """Solve ex2"""

    wires, gates = load_data(data)


    x = ''
    for gate in sorted(filter(lambda g: g.startswith('x'), wires.keys()), reverse=True):
        x += wires[gate]
    # x = int(x, 2)
    y = ''
    for gate in sorted(filter(lambda g: g.startswith('y'), wires.keys()), reverse=True):
        y += wires[gate]
    # y = int(y, 2)

    z = ''
    for gate in sorted(filter(lambda g: g.startswith('z'), gates.keys()), reverse=True):
        z += apply_gate(wires, gates, gate)

    print('Looking for: ')
    xy = bin(int(x, 2) + int(y, 2))[2:]
    print(xy)
    print(z)
    # print(len(gates.keys()), len(wires.keys()))

    involved = set()
    for i in range(len(x)):
        index = len(x)-1-1*i
        if z[index] != xy[index]:
            involved = involved.union(get_involved_gates(wires, gates, f'z{index:02d}'))

    print(involved, len(involved))
    print(involved - set(wires.keys()), len(involved - set(wires.keys())))
    exit()
    return ''


assert ex1(load("sample.txt")) == 4
assert ex1(load("sample2.txt")) == 2024
print(f'ex1 : {ex1(load("input.txt"))}')

# ex2('123')
# exit()
# ex2(load("sample2.txt"))
print(f'ex2 : {ex2(load("input.txt"))}')


sys.exit()