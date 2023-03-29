# Advent of Code 2022, Day 22
# Author: https://github.com/david3x3x3

import sys

dirs = ((0, 1),(1,0),(0,-1),(-1,0))

for part in (1, 2):
    dir = 0
    mymaps = []

    with open(sys.argv[1]) as fp:
        scale = len(fp.readline().rstrip()) // 3

    if scale == 4:
        # sample.txt

        #   0
        # 123
        #   45

        offsets = [[0,2],[1,0],[1,1],[1,2],[2,2],[2,3]]
        if part == 1:
            borders = [[[0,0],[3,1],[0,2],[4,3]],
                       [[2,0],[1,1],[3,2],[1,3]],
                       [[3,0],[2,1],[1,2],[2,3]],
                       [[1,0],[4,1],[2,2],[0,3]],
                       [[5,0],[0,1],[5,2],[3,3]],
                       [[4,0],[5,1],[4,2],[5,3]]]
        else:
            borders = [[[5,2],[3,1],[2,1],[1,1]],
                       [[2,0],[4,3],[5,3],[0,1]],
                       [[3,0],[4,0],[1,2],[0,0]],
                       [[5,1],[4,1],[2,2],[0,3]],
                       [[5,0],[1,3],[2,3],[3,3]],
                       [[0,2],[1,0],[4,2],[3,2]]]
    else:
        # input.txt

        #  01
        #  2
        # 34
        # 5

        offsets = [[0,1],[0,2],[1,1],[2,0],[2,1],[3,0]]
        if part == 1:
            borders = [[[1,0],[2,1],[1,2],[4,3]],
                       [[0,0],[1,1],[0,2],[1,3]],
                       [[2,0],[4,1],[2,2],[0,3]],
                       [[4,0],[5,1],[4,2],[5,3]],
                       [[3,0],[0,1],[3,2],[2,3]],
                       [[5,0],[3,1],[5,2],[3,3]]]
        else:
            borders = [[[1,0],[2,1],[3,0],[5,0]],
                       [[4,2],[2,2],[0,2],[5,3]],
                       [[1,3],[4,1],[3,1],[0,3]],
                       [[4,0],[5,1],[0,0],[2,0]],
                       [[1,2],[5,2],[3,2],[2,3]],
                       [[4,3],[1,1],[0,1],[3,3]]]

    with open(sys.argv[1]) as fp:
        lines = fp.readlines()

    for mapnum in range(6):
        mymap = []
        for r1 in range(scale):
            mymap += [[]]
            for c1 in range(scale):
                r2 = offsets[mapnum][0]*scale+r1
                c2 = offsets[mapnum][1]*scale+c1
                mymap[r1] += [lines[r2][c2]]
        mymaps += [mymap]

    mapnum = 0
    mymap = mymaps[mapnum]
    r1 = 0
    c1 = mymap[0].index('.')
    directions = lines[-1].strip()+'S'
    count_start = 0

    for line_pos, turn in enumerate(directions):
        if turn.isnumeric():
            continue
        for count in range(int(directions[count_start:line_pos])):
            r2, c2 = r1 + dirs[dir][0], c1 + dirs[dir][1]
            if r2 >= 0 and r2 < scale and c2 >= 0 and c2 < scale:
                # not wrapping
                if mymap[r2][c2] == '#':
                    break # hit wall
                r1, c1 = r2, c2
                continue
            # wrapping
            mapnum2, dir2 = borders[mapnum][dir]
            r3 = [r2, scale-1-c2, scale-1-r2, c2][dir]
            c3 = [scale-1-r2, c2, r2, scale-1-c2][dir]
            r2 = [r3, 0, scale-1-r3, scale-1][dir2]
            c2 = [0, c3, scale-1, scale-1-c3][dir2]
            if mymaps[mapnum2][r2][c2] == '#':
                break # hit wall
            mapnum = mapnum2
            mymap = mymaps[mapnum]
            dir = dir2
            r1, c1 = r2, c2
        dir = { 'R': (dir+1)%4, 'L': (dir+3)%4, 'S': dir }[turn]
        count_start = line_pos+1
    r2 = offsets[mapnum][0] * scale + r1
    c2 = offsets[mapnum][1] * scale + c1
    print(f'Part {part}: {(r2+1)*1000+(c2+1)*4+dir}')
