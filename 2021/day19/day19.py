from os import path
from sys import argv

class Beacon:
    def __init__(self, p):
        x, y, z = p
        self.x = x
        self.y = y
        self.z = z


class Scanner:
    def __init__(self, name):
        self.name = name
        self.beacons = []
    
    def add_beacon(self, beacon):
        self.beacons.append(beacon)


def load(file):
    scanners = list()   
    for ls in open(file, "r").read().split("\n\n"):
        scanner = Scanner(ls[4:13])
        for l in ls.split("\n")[1:]:
            beacon = Beacon(l.split(","))
            scanner.add_beacon(beacon)
        scanners.append(scanner)
    return scanners


def ex1(lines):
    return 0

def ex2(lines):
    return 0




sample = load("%s/sample.txt" % path.dirname(argv[0]))
r = ex1(sample)
print(r)
assert r == 79

input = load("%s/input.txt" % path.dirname(argv[0]))
print("ex1 : %d" % ex1(input))

input = load("%s/input.txt" % path.dirname(argv[0]))
print("ex2 : %d" % ex2(input))
