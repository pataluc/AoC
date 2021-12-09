def load(file):
    l = [[9] + list(map(int, l.rstrip())) + [9] for l in open(file, "r").readlines()]

    return [[9] * len(l[0])] + l + [[9] * len(l[0])]

def low_points(heightmap):
    o = []
    c = []
    for i in range(1, len(heightmap) - 1):
        for j in range(1, len(heightmap[i]) - 1):
            if (heightmap[i][j] < heightmap[i-1][j] and
               heightmap[i][j] < heightmap[i+1][j] and 
               heightmap[i][j] < heightmap[i][j+1] and 
               heightmap[i][j] < heightmap[i][j-1]):
                o.append(heightmap[i][j])
                c.append((i, j))
    return o, c

def explore_basin(p, heightmap, points):
    if p not in points:
        points.add(p)

        i, j = p
        if i >= 2 and heightmap[i][j] < heightmap[i-1][j] and heightmap[i-1][j] < 9:
            explore_basin((i-1, j), heightmap, points)
        if i < len(heightmap) - 2 and heightmap[i][j] < heightmap[i+1][j]  and heightmap[i+1][j] < 9:
            explore_basin((i+1, j), heightmap, points)
        if j >= 2 and heightmap[i][j] < heightmap[i][j-1] and heightmap[i][j-1] < 9:
            explore_basin((i, j-1), heightmap, points)
        if j < len(heightmap[i]) - 2 and heightmap[i][j] < heightmap[i][j+1] and heightmap[i][j+1] < 9:
            explore_basin((i, j+1), heightmap, points)

def ex1(lines):
    p = low_points(lines)[0]
    return sum(p) + len(p)

def ex2(lines):
    _, c = low_points(lines)
    r = []
    for p in c:
        b = set()
        explore_basin(p, lines, b)
        r.append(len(b))
    r.sort()
    return r[-1] * r[-2] * r[-3]

lines = load("sample.txt")
assert ex1(lines) == 15
assert ex2(lines) == 1134

lines = load("input.txt")
print("ex1 : %d" % ex1(lines))
print("ex2 : %d" % ex2(lines))



