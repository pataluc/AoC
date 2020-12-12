import sys
import copy
import itertools

lines = open("%s_input.txt" % sys.argv[0].split('.')[0], "r")

def matrix_to_string(m):
    return '|'.join(list(map(lambda x: ''.join(x), m)))

def adjacent_seats(m, i, j):
    return sum(map(lambda x: (x[max(0, j - 1):min(j + 1, len(x) - 1) + 1]), m[max(0, i - 1):min(i + 1, len(m) - 1) + 1]), list())

def first_seen(m, i, j):
    a = []
    if m[i][j] == '.':
        return a    
    for k, l in itertools.product(range(-1,2), range(-1,2)):
        n = 1
        while 0 <= i + n*k < len(m) and 0 <= j + n*l < len(m[0]) and m[i + n*k][j + n*l] == ".":
            n += 1
        if (0 <= i + n*k < len(m) and 0 <= j + n*l < len(m[0])):
            a.append(m[i + n*k][j + n*l])    
    return a

def apply_round(m, func, tolerance):
    n = [[''] * len(m[0]) for _ in range(len(m))]
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            a = func(m, i, j)
            if m[i][j] == "L" and "#" not in a:
                n[i][j] = "#"
            elif m[i][j] == "#" and a.count('#') > tolerance:
                n[i][j] = "L"
            else:
                n[i][j] = m[i][j]
    return n

# init
m1 = []
for line in lines:
    m1.append(list(line.rstrip()))
m2 = copy.deepcopy(m1) # Copy pour ex2

# ex 1
m_str = ''
while matrix_to_string(m1) != m_str:
    m_str = matrix_to_string(m1)
    m1 = apply_round(m1, adjacent_seats, 4)
print("ex1: %d" % sum(m1, list()).count('#'))

# ex 2
m_str = ''
while matrix_to_string(m2) != m_str:
    m_str = matrix_to_string(m2)
    m2 = apply_round(m2, first_seen, 5)
print("ex2: %d" % sum(m2, list()).count('#'))
