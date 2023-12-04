from os import path
from sys import argv
import re

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return open(file_path(file), "r").read().strip()

debug = False
def dprint(*s):
    if debug:
        print(*s)

def get_pixels(pixels):
    result = ''
    for line in pixels:
        result += ''.join(line) + '\n'
    return result

def apply_instructions(data, W = 50, H = 6):
    pixels = [['.'] * W for _ in range(H)]
    lines = data.split('\n')

    for line in lines:
        verb, params = re.match(r'(\w*) (.*)', line).groups()
        if verb == 'rect':
            c_max, r_max = params.split('x')
            for x in range(int(r_max)):
                for y in range(int(c_max)):
                    pixels[x][y] = '#'
        else:
            param, which, shift = re.match(r'(\w+) .=(\d+) by (\d+)', params).groups()
            which = int(which)
            shift = int(shift)
            if param == 'row':
                row = pixels[which]
                pixels[which] = row[-1*shift:] + row[:-1*shift]
            else:
                tmp = []
                for j in range(H):
                    tmp.append(pixels[j][which])
                tmp = tmp[-1*shift:] + tmp[:-1*shift]
                for j in range(H):
                    pixels[j][which] = tmp[j]

                
        
        dprint(get_pixels(pixels))
    return pixels

assert get_pixels(apply_instructions(load("sample.txt"), 7, 3)) == '.#..#.#\n#.#....\n.#.....\n'
print("ex1 : %s" % get_pixels(apply_instructions(load("input.txt"))).count('#'))
print("ex2 : \n%s" % get_pixels(apply_instructions(load("input.txt"))).replace('.', ' '))
