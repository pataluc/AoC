from os import path
from sys import argv

import re

def file_path(file):
    return f'{path.dirname(argv[0]) if path.dirname(argv[0]) else "."}/{file}'

def load(file):
    return open(file_path(file), "r").read().rstrip()

DEBUG = False
def dprint(*s):
    if DEBUG:
        print(*s)

def convert(source: list, input_map: str):
    for i, element in enumerate(source):
        for transfo in input_map.split('\n')[1:]:
            dest_start, src_start, transfo_l = list(map(int, transfo.split()))
            if src_start <= element < src_start + transfo_l:
                source[i] = dest_start + element - src_start
    return source

def printable_range(r):
    #return f"{r[0]:_} --{r[1]:_}--> {r[0] + r[1] - 1:_}"
    return f"{r[0]} --{r[1]}--> {r[0] + r[1] - 1}"

def convert2(sources: list, input_map: str):
    result = []
    if DEBUG: print(f"### {' | '.join(printable_range(source) for source in sorted(sources))}")
    for range_start, range_l in sources:
        range_end = range_start + range_l
        if DEBUG: print(f"  # Range: {printable_range([range_start, range_l])}")

        for transfo in input_map.split('\n')[1:]:
            dest_start, src_start, transfo_l = list(map(int, transfo.split()))
            dest_end = dest_start + transfo_l
            src_end = src_start + transfo_l
            delta = dest_start - src_start
            if DEBUG: print(f"    #  from {src_start:_} to {src_end:_}, delta = {delta:_}\t\t({dest_start:_} -> {dest_end:_})")
            if src_start <= range_start < src_end and src_start <= range_end < src_end:
                apres = [range_start + delta, range_l]
                if DEBUG: print(f"      cas 1 - inclus {printable_range(apres)}")
                result.append(apres)
                break
            if src_start <= range_start <= src_end <= range_end:
                avant, apres = [range_start + delta, src_end - range_start + 1], [src_end + 1, range_end - src_end -1]
                if DEBUG: print(f"      cas 2 | {printable_range(avant)} | {printable_range(apres)}")
                result.append(avant)
                if apres[1] > 0:
                    result.append(apres)
                break
            if src_start >= range_start and src_end < range_end:
                avant, jointure, apres = [range_start, src_start - range_start], [dest_start, transfo_l + 1], [src_end + 1, range_end - src_end - 1]
                if DEBUG: print(f"      cas 3 | {printable_range(avant)} | {printable_range(jointure)} | {printable_range(apres)}")
                result += [avant, jointure, apres]
                break
            if range_start <= src_start <= range_end < src_end:
                avant, apres = [range_start, src_start - range_start], [src_start + delta, range_end - src_start]
                if DEBUG: print(f"      cas 4 | {printable_range(avant)} | {printable_range(apres)}")
                result += [avant, apres]
                break
        else:
            # dprint("      disjoint")
            result.append([range_start, range_l])

    if DEBUG: print("### out ", [f"{x} --{l}--> {x+l-1}" for x, l in sorted(result)])
    return result


def ex1(data):
    groups = data.split('\n\n')
    source = list(map(int, groups[0].split()[1:]))

    for transfo in groups[1:]:
        source = convert(source, transfo)
    return min(source)

def ex2_reverse(data):
    groups = data.split('\n\n')
    source = [list(map(int, group.split())) for group in re.findall(r'(\d+ \d+)', groups[0])]

    transfo_groups = [ [list(map(int, transfo.split())) for transfo in transfo_group.split('\n')[1:]] for transfo_group in groups[1:][::-1]]
    if DEBUG: print(transfo_groups)
    i = 46
    while True:
        nb = i
        if DEBUG: print("lancement")
        for transfo_group in transfo_groups:
            if DEBUG: print("#" *80 + "\n\nconversion ", transfo_group[0])
            for dest_start, src_start, transfo_l in transfo_group:
                delta = src_start - dest_start
                if dest_start <= nb <= dest_start + transfo_l - 1:
                    nb += delta
                    break

        if any([m <= nb <= m + n - 1 for m, n in source]):
            return i
        i += 1
        if i % 1000000 == 0:
            print(i)

def transform(sources, transfo, depth = 0):

    if depth == len(transfo) + 1:
        return min(map(lambda source: source[0], sources))

    mins = []
    for range_start, range_length in sources:
        dest_start, src_start, transfo_l = list(map(int, transfo[depth].split()))
        dest_end = dest_start + transfo_l
        src_end = src_start + transfo_l
        delta = dest_start - src_start
        if DEBUG: print(f"    #  from {src_start:_} to {src_end:_}, delta = {delta:_}\t\t({dest_start:_} -> {dest_end:_})")
        if src_start <= range_start < src_end and src_start <= range_end < src_end:
            apres = [range_start + delta, range_l]
            if DEBUG: print(f"      cas 1 - inclus {printable_range(apres)}")
            result.append(apres)
            break
        if src_start <= range_start <= src_end <= range_end:
            avant, apres = [range_start + delta, src_end - range_start + 1], [src_end + 1, range_end - src_end -1]
            if DEBUG: print(f"      cas 2 | {printable_range(avant)} | {printable_range(apres)}")
            result.append(avant)
            if apres[1] > 0:
                result.append(apres)
            break
        if src_start >= range_start and src_end < range_end:
            avant, jointure, apres = [range_start, src_start - range_start], [dest_start, transfo_l + 1], [src_end + 1, range_end - src_end - 1]
            if DEBUG: print(f"      cas 3 | {printable_range(avant)} | {printable_range(jointure)} | {printable_range(apres)}")
            result += [avant, jointure, apres]
            break
        if range_start <= src_start <= range_end < src_end:
            avant, apres = [range_start, src_start - range_start], [src_start + delta, range_end - src_start]
            if DEBUG: print(f"      cas 4 | {printable_range(avant)} | {printable_range(apres)}")
            result += [avant, apres]
            break
        else:
            # dprint("      disjoint")
            result.append([range_start, range_l])

        mins.append(transform(new_src, transfo, depth + 1))

    return min(mins)

def ex2(data):
    groups = data.split('\n\n')
    source = [list(map(int, group.split())) for group in re.findall(r'(\d+ \d+)', groups[0])]
    transfo_groups = [ [list(map(int, transfo.split())) for transfo in transfo_group.split('\n')[1:]] for transfo_group in groups[1:][::-1]]
    print(transfo_groups)
    i = 46
    while True:
        nb = i
        dprint("lancement")
        for transfo_group in transfo_groups:
            dprint("#" *80 + "\n\nconversion ", transfo_group[0])
            for dest_start, src_start, transfo_l in transfo_group:
                delta = src_start - dest_start
                if dest_start <= nb <= dest_start + transfo_l - 1:
                    nb += delta
                    break

        if any([m <= nb <= m + n - 1 for m, n in source]):
            return i
        i += 1
        if i % 10000 == 0:
            print(i)



assert convert([79, 14, 55, 13], "seed-to-soil map:\n50 98 2\n52 50 48") == [81, 14, 57, 13]
assert ex1(load("sample.txt")) == 35
print(f'ex1 : {ex1(load("input.txt"))}')

assert ex2_reverse(load("sample.txt")) == 46
print(f'ex2 : {ex2_reverse(load("input.txt"))}')
exit()

assert ex2(load("sample.txt")) == 46
print(f'ex2 : {ex2(load("input.txt"))}')
DEBUG = True

