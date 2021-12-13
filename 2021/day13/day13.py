from types import new_class


def load(file):
    lines = open(file, "r").readlines()
    sep = lines.index("\n")
    return [tuple(map(int, line.strip().split(','))) for line in lines[:sep]], \
        list(map(lambda x: (x[0], int(x[1])), map(lambda x: x.strip().replace("fold along ", "").split('='), lines[sep+1:])))

def solve(dots, folds):
    last_x, last_y = (0, 0)

    for fold in folds:
        new_dots = set()

        for dot in dots:
            if fold[0] == "x":
                new_dots.add((abs(dot[0] - 2*fold[1]) if dot[0] > fold[1] else dot[0], dot[1]))
                last_x = fold[1]
            else:
                new_dots.add((dot[0], abs(dot[1] - 2*fold[1]) if dot[1] > fold[1] else dot[1]))  
                last_y = fold[1]
        dots = new_dots
    return dots, last_x, last_y


def ex1(dots, folds):
    return len(solve(dots, folds[:1])[0])

def ex2(dots, folds):
    dots, width, length = solve(dots, folds)

    r = [[' '] * width for _ in range(length)]
    for dot in dots:
        r[dot[1]][dot[0]] = "#"

    for rr in r:
        print("".join(rr))

    return dots

sample = load("sample.txt")
assert ex1(sample[0], sample[1]) == 17

input = load("input.txt")
print("ex1 : %d" % ex1(input[0], input[1]))
print("ex2 :")
ex2(input[0], input[1])