import re
from yachalk import chalk

def load(file):
    return  [ list(map(int, l.rstrip())) for l in open(file, "r").readlines()]

def cprint(lines):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] > 0:
                print(lines[i][j], end="")
            else:
                print(chalk.red(lines[i][j]), end="")        
        print("")
    

def around(i, j, s):
    return set(filter(lambda p: (0 <= p[0] < s) and (0 <= p[1] < s), [
        (i-1, j-1), (i-1, j), (i-1, j+1),
        (i, j-1),             (i, j+1),
        (i+1, j-1), (i+1, j), (i+1, j+1)
        ]))

def step(lines):    
    to_flash = list()
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            lines[i][j] += 1
            if lines[i][j] > 9 and (i,j) not in to_flash:
                to_flash.append((i,j))        
    
    for i, j in to_flash:
        adjacents = around(i, j, len(lines))
        for x, y in adjacents:
            lines[x][y] += 1
            if lines[x][y] > 9 and (x,y) not in to_flash:
                to_flash.append((x,y))
        
    flashes = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] > 9:
                lines[i][j] = 0
                flashes += 1
    return flashes

def ex1(lines, steps):
    flashes = 0
    for _ in range(steps):
        flashes += step(lines)
    return flashes

def ex2(lines):
    i = 1
    while True:
        step(lines)
        if sum(map(sum, lines)) == 0:
            return i
        i+=1

sample1 = load("sample1.txt")
assert ex1(sample1, 2) == 9
sample = load("sample.txt")
assert ex1(sample, 2) == 35
sample = load("sample.txt")
assert ex1(sample, 10) == 204
sample = load("sample.txt")
assert ex1(sample, 100) == 1656

input = load("input.txt")
print("ex1 : %d" % ex1(input, 100))

sample = load("sample.txt")
assert ex2(sample) == 195
input = load("input.txt")
print("ex2 : %d" % ex2(input))



