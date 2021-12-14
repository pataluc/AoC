from types import new_class


def load(file):
    lines = open(file, "r").readlines()
    return lines[0].strip(), dict(map(lambda x: tuple(x.strip().split(" -> ")), lines[2:]))

def process(template, instructions):
    #print("Process template %s with inscructions " % template, instructions)
    result = template[0]
    for i in range(len(template) - 1):
        #print(template[i:i+2])
        #print(template[i+1])
        if template[i:i+2] in instructions:
            result += instructions[template[i:i+2]]
        result += template[i+1]
    #print(result)
    return result


def ex1(input, rounds = 1):
    r = input[0]
    for i in range(rounds):
        print("round %d, size template: %d" % (i, len(r)))
        r = process(r, input[1])

    #print(r)
    l = list(r)
    # empty dictionary to hold pair of number and its count
    d = {}
    # loop through all elements and store count
    [ d.update( {i:d.get(i, 0)+1} ) for i in l ]

    v = list(d.values())
    v.sort()
    return v[-1]-v[0]

def ex2(dots, folds):
    return 0

sample = load("sample.txt")
assert process(sample[0], sample[1]) == 'NCNBCHB'
assert process(process(sample[0], sample[1]), sample[1]) == 'NBCCNBBBCBHCB'
assert ex1(sample, 10) == 1588

input = load("input.txt")
print("ex1 : %d" % ex1(input, 10))

assert ex1(sample, 40) == 2188189693529
print("ex2 : %d" % ex1(input, 40))