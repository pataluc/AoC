import sys
file = "sample.txt" if len(sys.argv) == 2 and sys.argv[1] == "-d" else "input.txt"
inputs = [int(line) for line in open(file, "r").readlines()]


def count_increased(array):
    return sum([1 for i in range(len(array)) if array[i] > array[i-1]])

def ex1():
    return count_increased(inputs)

def ex2():
    depths = inputs
    return count_increased(list(map(sum, zip(depths, depths[1:], depths[2:]))))


print("ex1 : %d" % ex1())
print("ex2 : %d" % ex2())