import sys

f = open("%s_input.txt" % sys.argv[0].split('.')[0], "r")

line1, line2 = f.readlines()

# Ex 1
your_timestamp = int(line1)
bus_ids = list(int(x) for x in filter(lambda x: x != "x", line2.split(',')))

i = 0
q = True
while q:
    b = list(filter(lambda x: ((your_timestamp + i) % x) == 0, bus_ids))
    if len(b) == 1:
        print("ex1: %d (line: %d and wait: %d)" % ((i * b[0]), b[0], i))
        q = False
    i += 1

# Ex 2
bus_ids = list(filter(lambda x: x[0] != 0, [(int(x), i) if x != "x" else (0, i) for i, x in enumerate(line2.split(','))]))

n = 0
m = 0
inc = 1
while True:
    n += inc

    # Pour incrémenter de plus en plus vite
    for j in range(len(bus_ids)):
        if all((n + x[1]) % x[0] == 0 for x in bus_ids[:j+1]) and j > m:
            m = j
            inc *= bus_ids[j][0]

    if all((n + x[1]) % x[0] == 0 for x in bus_ids):
        print("ex2: %d" % n)
        exit()

