import re
from os import path
from sys import argv

import numpy as np

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)


def load(file):
    instructions = [tuple(x.split(" ")) for x in open(file_path(file), "r").read().split("\n")]
    return instructions

def ex1(instructions):
    score = i = cycle = 0
    X = 1
    for i, instruction in enumerate(instructions):
        cycle += 1
        if (cycle - 20) % 40 == 0:
            score += cycle * X
            # print("")
            # print("end of cycle %d, X = %d, strength = %d, score = %d" % (cycle, X, cycle*X, score))

        if instruction[0] == 'addx':
            cycle += 1
            if (cycle - 20) % 40 == 0:
                score += cycle * X
                # print("")
                # print("end of cycle %d, X = %d, strength = %d, score = %d" % (cycle, X, cycle*X, score))
            X += int(instruction[1])
                
        
        # if cycle > 25:
        #     exit()
    return score

def ex2(instructions):
    output = ""
    row = ""
    i = 0
    cycle = 1
    X = 1
    # print("Sprite position: %s\n" % "".join(["#" if abs(X-x) < 2 else "." for x in range(40)]))
    for i, instruction in enumerate(instructions):
        # print("Start cycle  %2s: begin executing %s" % (cycle, " ".join(instruction)))
        # print("During cycle %2s: CRT draws pixel in position %d" % (cycle, (cycle-1) % 40))
        
        # print(X, cycle, abs(X - cycle))
        if abs(X - (cycle-1) % 40) <= 1:
            row += "#"
        else: 
            row += "."
        # print("Current CRT row: %s" % row)
        if len(row) == 40:
            output += "%s\n" % row
            row = ""

        if instruction[0] == 'addx':
            cycle += 1
            # print(X, cycle, abs(X - cycle))
            if abs(X - (cycle-1) % 40) <= 1:
                row += "#"
            else: 
                row += "."
            # print("\nDuring cycle %2s: CRT draws pixel in position %d" % (cycle, (cycle-1) % 40))
            # print("Current CRT row: %s" % row)
            
            if len(row) == 40:
                output += "%s\n" % row
                row = ""

            X += int(instruction[1])
            # print("End of cycle %2s: finish executing addx %s (Register X is now %d)" % (cycle, instruction[1], X))
            # print("Sprite position: %s\n" % "".join(["#" if abs(X-x) < 2 else "." for x in range(40)]))
        # else:
        #     print("End of cycle %2s: finish executing noop\n" % cycle)

        cycle += 1
        # if cycle > 45:
        #     exit()

    return output

sample1 = load("sample.txt")
# print(sample1)
# ex1(sample1)
# exit()
sample2 = load("sample2.txt")
assert ex1(sample2) == 13140

data = load("input.txt")
print("ex1 : %s" % ex1(data))

sample2_output = "##..##..##..##..##..##..##..##..##..##..\n###...###...###...###...###...###...###.\n####....####....####....####....####....\n#####.....#####.....#####.....#####.....\n######......######......######......####\n#######.......#######.......#######.....\n"
assert ex2(sample2) == sample2_output
print("ex2 : \n%s" % ex2(data))