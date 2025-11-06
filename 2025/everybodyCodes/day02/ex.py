import sys

def add(x: list, y: list) -> list:
    return [x[0] + y[0], x[1] + y[1]]

assert add([1,1], [2,2]) == [3,3]
assert add([2,5], [3,7])  == [5,12]
assert add([-2,5], [10,-1]) == [8,4]
assert add([-1,-2], [-3,-4]) == [-4,-6]


def multiply(x: list, y: list) -> list:
    return [x[0] * y[0] - x[1] * y[1], x[0] * y[1] + y[0] * x[1]]
assert multiply([1,1], [2,2]) == [0,4]
assert multiply([2,5], [3,7]) == [-29,29]
assert multiply([-2,5], [10,-1]) == [-15,52]
assert multiply([-1,-2], [-3,-4]) == [-5,10]


def divide(x: list, y: list) -> list:
    return [int(x[0] / y[0]), int(x[1] / y[1])]
assert divide([10,12], [2,2]) == [5,6]
assert divide([11,12], [3,5]) == [3,2]
assert divide([-10,-12], [2,2]) == [-5,-6]
assert divide([-11,-12], [3,5]) == [-3,-2]

def part1(number: list) -> list:
    result = [0,0]
    for _ in range(3):
        result = multiply(result, result)
        result = divide(result, [10, 10])
        result = add(result, number)
    return result

assert(part1([25,9])) == [357,862]

print("Part 1: ", part1([165,52]))

def check_point(a: list) -> int:
    result = [0, 0]
    for i in range(100):
        result = multiply(result, result)
        result = divide(result, [100000, 100000])
        result = add(result, a)
        # print(" -> ", result)
        if not(-1000000 <= result[0] <= 1000000 and -1000000 <= result[1] <= 1000000):
            # print("Out of range", result, i+1)
            return 0

    return 1

def part2(number: list) -> list:
    result = 0
    for j in range(number[1], number[1] + 1001, 10):
        for i in range(number[0], number[0] + 1001, 10):
            t = check_point([i, j])
            result += t
            # print('.' if t == 0 else 'x', end = '')
        # print('')
    return result

assert(part2([35300,-64910])) == 4076
print("Part 2: ", part2([-3334,68783]))

def part3(number: list) -> list:
    result = 0
    for j in range(number[1], number[1] + 1001):
        for i in range(number[0], number[0] + 1001):
            t = check_point([i, j])
            result += t
    return result

assert(part3([35300,-64910])) == 406954
print("Part 3: ", part3([-3334,68783]))