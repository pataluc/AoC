import re
from os import path
from sys import argv
import numpy as np

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    board, path = open(file_path(file), "r").read().split("\n\n")
    path = list(map(lambda x: int(x) if x not in "RL" else x, filter(lambda x: x != '', re.findall(r'(\d*|[RL])', path))))

    board = board.split('\n')
    start = (len(re.findall(r'^ *', board[0])[0]), 0)
    # board_map = set()
    # board_rock = set()
    # for j, line in enumerate(lines.split("\n")):
    #     for i, c in enumerate(line):
    #         if c == '.':
    #             board_map.add((i, j))
    #         elif c == '#':
    #             board_rock.add((i, j))

    return (start, board, path)

debug = False

def string_replace(s, pos, c):
    l = list(s)
    l[pos] = c
    return ''.join(l)

def get_next_pos(board, pos, dir):
    i, j = pos + dir
    # print(i,j)

    # horiz
    if dir[0]:
        line = board[j]
        if not 0 <= i < len(line) or line[i] == ' ':
            i = i % len(line)
            while not 0 <= i < len(line) or line[i] not in '#.':
                i = (i + dir[0]) % len(line)
    else:
        col = ''
        for y in range(len(board)):
            if i < len(board[y]):
                col += board[y][i]
        # print("col: %s" % col)
        if not 0 <= j < len(col) or col[j] == ' ':
            while not 0 <= j < len(col) or col[j] not in '#.':
                j = (j + dir[1]) % len(col)
    
    next = (i, j)

    # if rock or space
    if board[next[1]][next[0]] == '.':
        return tuple(next)
    elif board[next[1]][next[0]] == '#':
        return pos



def ex1(data):
    pos, board, path = data

    dirs = {
        (1,0): '>',
        (0,1): 'v',
        (-1,0): '<',
        (0,-1): '^'
    }
    facing = {
        (1,0): 0,
        (0,1): 1,
        (-1,0): 2,
        (0,-1): 3
    }

    shift_dirs = {
        'R': {
            (1,0): np.array((0,1)),
            (0,-1): np.array((1,0)),
            (-1,0): np.array((0,-1)),
            (0,1): np.array((-1,0))
        },
        'L': {
            (1,0): np.array((0,-1)),
            (0,1): np.array((1,0)),
            (-1,0): np.array((0,1)),
            (0,-1): np.array((-1,0))
        }
    }

    dir = np.array((1, 0))
    
    board2 = board.copy()
    board2[pos[1]] = string_replace(board2[pos[1]], pos[0], dirs[tuple(dir)])

    # print("\n".join(board))
    for p in path:
        # print(p, pos)
        if isinstance(p, str):
            dir = shift_dirs[p][tuple(dir)]
            board2[pos[1]] = string_replace(board2[pos[1]], pos[0], dirs[tuple(dir)])
        else:
            i = 0
            next_pos = get_next_pos(board, pos, dir)
            # print(pos, next_pos)
            
            while i < p and next_pos != pos:
                board2[next_pos[1]] = string_replace(board2[next_pos[1]], next_pos[0], dirs[tuple(dir)])
                i += 1
                pos = next_pos
                next_pos = get_next_pos(board, pos, dir)
            # print("----\n" + "\n".join(board2))

        # print(pos)
    return 1000 * (pos[1] + 1) + 4 * (pos[0] + 1) + facing[tuple(dir)]

def ex2(data: dict):
    return

sample = load("sample.txt")
# print(sample)
assert ex1(sample) == 6032
data = load("input.txt")
print("ex1 : %s" % ex1(data))

assert ex2(sample) == 5031
print("ex2 : %s" % ex2(data))
