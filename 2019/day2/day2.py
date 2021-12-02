import sys
file = "sample.txt" if len(sys.argv) == 2 and sys.argv[1] == "-d" else "input.txt"
inputs = [int(line) for line in open(file, "r").readlines()[0].split(',')]

def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
operators = [None, add, multiply]

def process(array,  pos = 0):
    op = array[pos]

    if op != 99:
        a, b = array[array[pos + 1]], array[array[pos + 2]]
        output = array[pos + 3]
        #print("lets put %d on pos %d" %(operators[op](a, b), output))
        array[output] = operators[op](a, b)
        process(array, pos + 4)
    return array
    
def ex1():
    mem = inputs.copy()
    mem[1] = 12
    mem[2] = 2 
    return process(mem)[0]

def ex2():
    for noun in range(100):
        for verb in range(100):
            mem = inputs.copy()
            mem[1] = noun
            mem[2] = verb
            mem = process(mem)

            if mem[0] == 19690720:
                return 100 * noun + verb

print("ex1 : %d" % ex1())
print("ex2 : %d" % ex2())