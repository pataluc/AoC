from collections import defaultdict
import sys
import re
f = open("%s_sample1.txt" % sys.argv[0].split('.')[0], "r")

adapters = []
for line in f:
    adapters.append(int(line))

adapters.sort()
adapters.append(max(adapters) + 3)

# ex 1
soustracted = list(map(lambda x: x[0] - x[1], zip(adapters, [0] + adapters[:-1])))
print("ex1: %d" % (soustracted.count(1) * soustracted.count(3)))

# ex 2 (1322306994176)

print(adapters)
weights = dict()

for adapter in adapters:
    if adapter not in weights:
        weights[adapter] = 1

    for i in range(1, 4):
        child = adapter + i
        if child in adapters:
            if child not in weights:
                weights[child] = 0 if child > 3 else 1
            weights[child] += weights[adapter]
    print(weights)

print(weights[adapters[-1]])

exit()




#exit()
# ex 2 (bis)
adapters.append(0)
adapters.sort()

def print_matrix(m):
    for l in m:
        print(l)

s = len(adapters)
m = [[0] * s for i in range(s)]

for i in range(0, len(adapters)):
    #print("i = %d,\tadapters[i] = %d" % (i, adapters[i]))
    j = i + 1
    while j < len(adapters) and adapters[j] - adapters[i] <= 3:
        #print(" j = %d,\tadapters[j] = %d" % (j, adapters[j]))
        #g.addEdge(i, j)
        m[i][j] = 1
        j += 1

print(adapters)
#print_matrix(m)

#s=0; d=len(adapters)-2
#print("Following are all different paths from % d to % d :" % (s, d))
#g.printAllPaths(s, d)
# This code is contributed by Neelam Yadav

import numpy

count = 0
for i in range(len(adapters)):
    count += numpy.linalg.matrix_power(m, i)[0][len(adapters) - 1]

print("ex2: %d" % (count))
