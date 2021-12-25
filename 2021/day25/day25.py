from os import path
from sys import argv

def load(file):
    east, south = set(), set()
    i = 0
    lines = open("%s/%s" % ((path.dirname(argv[0]) if path.dirname(argv[0]) else "."), file), "r").readlines()
    for line in lines:
        j = 0
        for region in line.strip():
            if region == "v":
                south.add((i,j))
            elif region == ">":
                east.add((i,j))
            j += 1
        i += 1

    return (east, south, len(lines[0].strip()), len(lines))


def step(herds):
    east, south, width, height = herds
    new_east, new_south = set(), set()
    changes = 0
    for cucumber in east:
        x, y = cucumber
        if (x, (y + 1) % width) not in east and (x, (y + 1) % width) not in south:
            new_east.add((x, (y + 1) % width))
            changes += 1
        else:
            new_east.add(cucumber)
    for cucumber in south:
        x, y = cucumber
        if ((x + 1) % height, y) not in new_east and ((x + 1) % height, y) not in south:
            new_south.add(((x + 1) % height, y))
            changes += 1
        else:
            new_south.add(cucumber)

    return changes, new_east, new_south

def print_herds(herds):    
    east, south, width, height = herds

    #print("#" * width)
    for i in range(height):
        s = ""
        for j in range(width):
            if (i,j) in east:
                s += ">"
            elif (i,j) in south:
                s += "v"
            else:
                s += "."
        print(s)
    print()


def ex1(herds):
    _, _, width, height = herds
    i = 1
    #print("Initial state:")
    #print_herds(herds)
    changes, new_east, new_south = step(herds)
    while changes > 0:
        i += 1
        #print("After %d step%s:" % (i, "s" if i > 1 else ""))
        #print_herds((new_east, new_south, width, height))
        changes, new_east, new_south = step((new_east, new_south, width, height))
    print_herds((new_east, new_south, width, height))
    return i


sample = load("sample.txt")
input = load("input.txt")

assert ex1(sample) == 58


print("ex1 : %d" % ex1(input))