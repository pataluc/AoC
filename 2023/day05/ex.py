from os import path
from sys import argv

import regex as re

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)


def load(file):
    return open(file_path(file), "r").read().rstrip()

debug = False
def dprint(*s):
    if debug:
        print(*s)

def convert(source: list, input_map: str):
    for i, element in enumerate(source):
        for transfo in input_map.split('\n')[1:]:
            dest_start, src_start, l = list(map(int, transfo.split()))
            if src_start <= element < src_start + l:
                source[i] = dest_start + element - src_start
    return source

def convert2(source: list, input_map: str):
    result = []
    for transfo in input_map.split('\n')[1:]:
        dest_start, src_start, transfo_l = list(map(int, transfo.split()))
        # for start, l in source:
            
            # if src_start <= element < src_start + transfo_l:
            #     source[i] = dest_start + element - src_start
    return result

def ex1(data):
    groups = data.split('\n\n')
    source = list(map(int, groups[0].split()[1:]))

    for transfo in groups[1:]:
        source = convert(source, transfo)
    return min(source)

def ex2(data):
    groups = data.split('\n\n')
    source = re.findall(r'(\d+ \d+)', groups[0])

    for transfo in groups[1:]:
        source = convert(source, transfo)
    return min(source)

assert convert([79, 14, 55, 13], "seed-to-soil map:\n50 98 2\n52 50 48") == [81, 14, 57, 13]
assert ex1(load("sample.txt")) == 35
print("ex1 : %s" % ex1(load("input.txt")))

assert ex2(load("sample.txt")) == 46
print("ex2 : %s" % ex2(load("input.txt")))