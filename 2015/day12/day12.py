from os import path
from sys import argv

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return eval(open(file_path(file), "r").read())

debug = False

def sum_numbers(o):
    if isinstance(o, str):
        return 0
    if isinstance(o, int):
        return o
    if isinstance(o, list):
        return sum(map(sum_numbers, o))
    if isinstance(o, dict):
        return sum(map(sum_numbers, o.values()))

def sum_numbers_not_red(o):
    if isinstance(o, str):
        return 0
    if isinstance(o, int):
        return o
    if isinstance(o, list):
        return sum(map(sum_numbers_not_red, o))
    if isinstance(o, dict):
        if "red" in o.values():
            return 0
        else:
            return sum(map(sum_numbers_not_red, o.values()))

assert sum_numbers([1,2,3]) == 6
assert sum_numbers({"a":2,"b":4}) == 6
assert sum_numbers([[[3]]]) == 3
assert sum_numbers({"a":{"b":4},"c":-1}) == 3
assert sum_numbers({"a":[-1,1]}) == 0
assert sum_numbers([-1,{"a":1}]) == 0
assert sum_numbers([]) == 0
assert sum_numbers({}) == 0


data = load("input.txt")
print("ex1 : %s" % sum_numbers(data))

assert sum_numbers_not_red([1,2,3]) == 6
assert sum_numbers_not_red([1,{"c":"red","b":2},3]) == 4
assert sum_numbers_not_red({"d":"red","e":[1,2,3,4],"f":5}) == 0
assert sum_numbers_not_red([1,"red",5]) == 6

print("ex2 : %s" % sum_numbers_not_red(data))