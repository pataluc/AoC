from itertools import permutations, product
from os import X_OK, path
from sys import argv



def load(file):
    input = open(file, "r").read().split("\n\n")
    image = []
    i = 0
    for line in input[1].split("\n"):
        i += 1
        j = 0
        for c in line:
            j += 1
            if c == "#":
                image.append((i,j))
    return image, input[0]

def enhance(image, algo, default, framesize):
    if framesize:
        min_x, max_x, min_y, max_y = framesize
    else:
        xs = list(map(lambda x: x[0], image))
        min_x, max_x = min(xs), max(xs)
        ys = list(map(lambda x: x[1], image))
        min_y, max_y = min(ys), max(ys)

    new_image = []
    for i in range(min_x - 2, max_x + 3):
        for j in range(min_y - 2, max_y + 3):
            s = ""
            #print("---", i, j)
            #print_image(image, (i - 1, i + 2, j - 1, j+ 2))
            for m in (-1, 0, 1):
                for n in (-1, 0, 1):
                    if (i + m, j + n) in image or (
                        (not (min_x <= i + m <= max_x) or not(min_y <= j + n <= max_y)) and default == "#"
                        ):
                        s += '1'
                    else:
                        s += '0'
            #print("%s = %d, algo: %s" % (s, int(s, 2), algo[int(s, 2)]))
            if algo[int(s, 2)] == "#":
                new_image.append((i, j))
                
    return new_image, (min_x - 1, max_x + 1, min_y - 1, max_y + 1)

def print_image(image, default, frame = None):
    if frame:
        min_x, max_x, min_y, max_y = frame
    else:
        xs = list(map(lambda x: x[0], image))
        min_x, max_x = min(xs), max(xs)
        ys = list(map(lambda x: x[1], image))
        min_y, max_y = min(ys), max(ys)

    for i in range(min_x - 2, max_x + 3):
        for j in range(min_y - 2, max_y + 3):
            if (i, j) in image or (
                (not (min_x <= i <= max_x) or not(min_y <= j <= max_y)) and default == "#"
                ):
                print("#", end="")
            else:
                print(".", end="")
        print("")


def ex1(image, algo):
    default = '.'
    framesize = None
    #print(len(image))
    #print_image(image, default)
    for _ in range (2):
        image, framesize = enhance(image, algo, default, framesize)
        if algo[0] == "#":
            default = '.' if default == "#" else "#"
        #print(len(image))
        #print_image(image, default)
    return len(image)

def ex2(image, algo):
    default = '.'
    #print(len(image))
    #print_image(image, default)
    for i in range (50):
        image = enhance(image, algo, default)
        if algo[0] == "#":
            default = '.' if default == "#" else "#"
        print(i, len(image))
        #print_image(image, default)
    return len(image)


image, algo = load("%s/sample.txt" % (path.dirname(argv[0]) if path.dirname(argv[0]) else "."))
r = ex1(image, algo)
assert r == 35

image, algo = load("%s/input.txt" % (path.dirname(argv[0]) if path.dirname(argv[0]) else "."))
print("ex1 : %d" % ex1(image, algo))

exit()
image, algo = load("%s/sample.txt" % (path.dirname(argv[0]) if path.dirname(argv[0]) else "."))
#r = ex2(image, algo)
#assert r == 3351

image, algo = load("%s/input.txt" % (path.dirname(argv[0]) if path.dirname(argv[0]) else "."))
print("ex2 : %d" % ex2(image, algo))
