import sys, re
f = open("%s_input.txt" % sys.argv[0].split('_')[0], "r")

collisions = 0
lines = []

for line in f:
    lines.append(line)

i = 0
j = 0

while j < len(lines):
    if lines[j][i % (len(line) - 1)] == "#":
        collisions += 1

    l = list(lines[j])

    l[i % (len(line) - 1)] = "X" if line[i % (len(line) - 1)] == "#" else "O"
    lines[j] = "".join(l)

    i += 1
    j += 2


for line in lines:    
    print(line)
    
print(collisions)

# 1,1: 90
# 3,1: 244
# 5,1: 97
# 7,1: 92
# 2,1: 48