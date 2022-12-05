from os import path
from sys import argv

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    raw_stacks, moves = open(file_path(file), "r").read().split("\n\n")

    raw_stacks = raw_stacks.split("\n")[::-1]
    stacks = [[] for a in range(((len(raw_stacks[0]) + 1) // 4))]
    
    for stack_line in raw_stacks[1::]:
        for i, stack in enumerate(stacks):
            c = stack_line[4*i + 1]
            if c != ' ':
                stack.append(c)

    moves = [[int(t.split(" ")[1]), int(t.split(" ")[3]), int(t.split(" ")[5])] for t in moves.split("\n")]
    return stacks, moves


def ex1(stacks, moves):
    for move in moves:
        for i in range(move[0]):
            if stacks[move[1]-1]:
                stacks[move[2]-1].append(stacks[move[1]-1].pop())           
    
    return "".join(list(map(lambda s: s[-1], stacks)))

def ex2(stacks, moves):
    for move in moves:
        print("moves %d :" % move[0], stacks[move[1]-1][-1*move[0]:])
        stacks[move[2]-1] += stacks[move[1]-1][-1*move[0]:]
        stacks[move[1]-1] = stacks[move[1]-1][:-1*move[0]]
        print(stacks)
            
    
    return "".join(list(map(lambda s: s[-1], stacks)))

stacks, moves = load("sample.txt")
print(stacks, moves)
#assert ex1(stacks, moves) == "CMZ"
assert ex2(stacks, moves) == "MCD"

stacks, moves = load("input.txt")
#print("ex1 : %s" % ex1(stacks, moves))
print("ex2 : %s" % ex2(stacks, moves))