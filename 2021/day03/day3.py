import sys
file = "sample.txt" if len(sys.argv) == 2 and sys.argv[1] == "-d" else "input.txt"
inputs = list([list(map(int, list(line.rstrip()))) for line in open(file, "r").readlines()])

def bin_to_dec(array):
    return int("".join(map(str, array)), 2)

def get_gamma_epsilon(array, a, b):
    return bin_to_dec([a if sum(map(lambda line : line[x], array)) > len(array) / 2 else b for x in range(len(array[0]))])

def get_o2_co2(array, a, b, index = 0):
    to_filter = a if (sum(map(lambda line : line[index], array)) < len(array) / 2) else b
    inputs = [line for line in array if line[index] == to_filter]

    return bin_to_dec(inputs[0]) if len(inputs) == 1 else get_o2_co2(inputs, a, b, index + 1)

def ex1():
    return get_gamma_epsilon(inputs, 1, 0) * get_gamma_epsilon(inputs, 0, 1)

def ex2():
    return get_o2_co2(inputs, 0, 1) * get_o2_co2(inputs, 1, 0)

print("ex1 : %d" % ex1())
print("ex2 : %d" % ex2())

