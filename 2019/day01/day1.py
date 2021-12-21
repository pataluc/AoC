import sys
file = "sample.txt" if len(sys.argv) == 2 and sys.argv[1] == "-d" else "input.txt"
inputs = [int(line) for line in open(file, "r").readlines()]

def ex1():
    return sum(map(lambda x: int(x/3)-2, inputs))

def fuel_cost(mass):
    fuel = int(mass / 3) - 2
    if fuel < 0:
        return 0
    else:
        return fuel + fuel_cost(fuel)

def ex2():
    return sum(map(fuel_cost, inputs))

print("ex1 : %d" % ex1())
print("ex2 : %d" % ex2())