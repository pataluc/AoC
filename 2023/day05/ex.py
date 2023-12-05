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

def convert2(sources: list, input_map: str):
    result = []
    for transfo in input_map.split('\n')[1:]:
        dest_start, src_start, transfo_l = list(map(int, transfo.split()))
        dest_end = dest_start + transfo_l
        src_end = src_start + transfo_l

        print(sources)
        for range_start, range_l in sources:
            range_end = range_start + range_l
            if range_end < src_start or range_start > dest_start:
                result.append([range_start, range_l])
            elif src_start <= range_start < src_end and src_start <= range_end < src_end:
                result.append([dest_start + range_start - src_start, range_l])
            elif src_start <= range_start <= src_end and range_end > src_end:
                result.append([dest_start + range_start - src_start, src_end - range_start])
                result.append([src_end + 1, range_end - src_end])
            elif src_start >= range_start and src_end < range_end:
                result.append([range_start, src_start - range_start])
                result.append([dest_start + range_start - src_start, src_end - src_start])
                result.append([src_end + 1, range_end - src_end])
            elif range_start <= src_start and range_end < src_end:
                result.append([range_start, src_start - range_start])
                result.append([src_start, range_end - src_start])
    return result
    

def ex1(data):
    groups = data.split('\n\n')
    source = list(map(int, groups[0].split()[1:]))

    for transfo in groups[1:]:
        source = convert(source, transfo)
    return min(source)

def ex2(data):
    groups = data.split('\n\n')
    source = [list(map(int, group.split())) for group in re.findall(r'(\d+ \d+)', groups[0])]

    for transfo in groups[1:]:
        source = convert2(source, transfo)
    return min(list(map(lambda s: s[0], source)))

assert convert([79, 14, 55, 13], "seed-to-soil map:\n50 98 2\n52 50 48") == [81, 14, 57, 13]
assert ex1(load("sample.txt")) == 35
print("ex1 : %s" % ex1(load("input.txt")))

assert ex2(load("sample.txt")) == 46
print("ex2 : %s" % ex2(load("input.txt")))