import sys
file = "sample.txt" if len(sys.argv) == 2 and sys.argv[1] == "-d" else "input.txt"
inputs = list(map(lambda r : [r[0], int(r[1])], [line.rstrip().split(' ') for line in open(file, "r").readlines()]))

def process_depth(array):
    return sum([row[1] for row in array if row[0] == 'down']) - sum([row[1] for row in array if row[0] == 'up'])

def process_pos(array):
    return sum([row[1] for row in array if row[0] == 'forward'])

def process_position1(array):
    return process_depth(array) * process_pos(array)

def process_position2(array):
    aim = 0
    depth = 0
    pos = 0
    for row in array:
        if row[0] == "down":
            aim = aim + row[1]
        if row[0] == "up":
            aim = aim - row[1]
            
        if row[0] == "forward":
            pos = pos + row[1]
            depth = depth + aim * row[1]
        
    return depth * pos


def ex1():
    return process_position1(inputs)

def ex2():
    return process_position2(inputs)


print("ex1 : %d" % ex1())
print("ex2 : %d" % ex2())