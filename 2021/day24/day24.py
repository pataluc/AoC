from os import path
from sys import argv

def load(file):
    return [line.strip().split(" ") for line in open("%s/%s" % ((path.dirname(argv[0]) if path.dirname(argv[0]) else "."), file), "r").readlines()]

def monad(instructions, input):
    operations = {
        "add": lambda a, b: a + b,
        "mul": lambda a, b: a * b,
        "div": lambda a, b: a // b,
        "mod": lambda a, b: a % b,
        "eql": lambda a, b: 1 if a == b else 0
    }
    
    mem = {
        'w': 0,            
        'x': 0,
        'y': 0,
        'z': 0
    }

    input = str(input)

    for instruction in instructions:
        if instruction[0] == "inp":
            mem[instruction[1]] = int(input[0])
            input = input[1:]
        else:
            op = operations[instruction[0]]
            b = mem[instruction[2]] if instruction[2] in mem else int(instruction[2])
            mem[instruction[1]] = op(mem[instruction[1]], b)

          
    return mem



def ex1(instructions):
    model_number = 99999999999999

    mem = monad(instructions, model_number)
    while mem["z"] != 0:
        model_number -= 1
        if model_number % 10000 == 1111:
            print(model_number)
        #print(model_number, mem["z"])
        #decremente tant que 0 dans le modele
        while '0' in str(model_number):
            model_number -= 1

        mem = monad(instructions, model_number)
    
    return model_number


sample = load("sample.txt")
instructions = load("input.txt")

assert monad([['inp', 'x'], ['mul', 'x', '-1']], "2")['x'] == -2
assert monad(sample, "9") == {'w': 1, 'x': 0, 'y': 0, 'z': 1}


print("ex1 : %d" % ex1(instructions))

