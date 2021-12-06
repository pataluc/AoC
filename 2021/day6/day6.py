import sys
file = "sample.txt" if len(sys.argv) == 2 and sys.argv[1] == "-d" else "input.txt"
lanternfishes = [0 for i in range (9)]

for l in list(map(int, open(file, "r").readlines()[0].rstrip().split(','))):
    lanternfishes[l] += 1

def simulate(lfs, days):
    for i in range(days):
        new_lfs = lfs.pop(0)
        lfs[6] += new_lfs
        lfs.append(new_lfs)
    return lfs

def ex1():
    return sum(simulate(lanternfishes.copy(), 80))

def ex2():
    return sum(simulate(lanternfishes.copy(), 256))

print("ex1 : %d" % ex1())
print("ex2 : %d" % ex2())



