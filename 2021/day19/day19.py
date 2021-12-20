from itertools import permutations, product
from collections import defaultdict
from os import path
from sys import argv

class Scanner:
    def __init__(self, name):
        self.name = name
        self.beacons = []
        self.vectors = {}
    
    def add_beacon(self, beacon):
        self.beacons.append(beacon)                   


def load(file):
    scanners = list()   
    for ls in open(file, "r").read().split("\n\n"):
        scanner = Scanner(ls[4:13])
        for l in ls.split("\n")[1:]:
            beacon = tuple(map(int, l.split(",")))
            scanner.add_beacon(beacon)
        scanners.append(scanner)
    return scanners

def print_coord(p):
    return "(%d, %d, %d)" % (p[0], p[1], p[2])

def coord_product(p):
    return abs(p[0]*p[1]*p[2])

def get_all_rotations(scanner):
    for perm in permutations((0, 1, 2)):
        for orient in product((-1, 1), repeat=3):
            rotation = []
            for beacon in scanner.beacons:
                rotation.append(tuple(o * beacon[p] for o, p in zip(orient, perm)))
            yield rotation

def point_diff(p: tuple, o: tuple):
    return (p[0] - o[0], p[1] - o[1], p[2] - o[2])

def compute_rotation(beacon_map, new_beacons):
    diffs = defaultdict(int)
    for b in beacon_map:
        for nb in new_beacons:
            diffs[point_diff(nb, b)] += 1
    for key, value in diffs.items():
        if value >= 12:
            return key

def ex1(scanners: list):
    scanner0 = scanners.pop(0)
    beacon_map = set(scanner0.beacons)

    while scanners:
        for scanner in scanners:
            for rotated_beacons in get_all_rotations(scanner):
                found_translation = compute_rotation(beacon_map, rotated_beacons)
                if found_translation:
                    found_scanners.append(found_translation)
                    for b in rotated_beacons:
                        beacon_map.add(point_diff(b, found_translation))
                    scanners.remove(scanner)
                    break
            else: continue
            break
                    

    return len(beacon_map)

def ex2(found_scanners):
    max = 0
    for i in range(len(found_scanners)):
        for j in range(i + 1, len(found_scanners)):
            d = sum(map(abs, point_diff(found_scanners[i], found_scanners[j])))
            if d > max:
                max = d
    return max


found_scanners = [(0,0,0)]
sample = load("%s/sample.txt" % (path.dirname(argv[0]) if path.dirname(argv[0]) else "."))
assert ex1(sample) == 79
assert ex2(found_scanners) == 3621

input = load("%s/input.txt" % (path.dirname(argv[0]) if path.dirname(argv[0]) else "."))
found_scanners = [(0,0,0)]
print("ex1 : %d" % ex1(input))
print("ex2 : %d" % ex2(found_scanners))
