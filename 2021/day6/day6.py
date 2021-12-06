import sys
file = "sample.txt" if len(sys.argv) == 2 and sys.argv[1] == "-d" else "input.txt"
lanternfishes = [0 for i in range (9)]

for l in list(map(int, open(file, "r").readlines()[0].rstrip().split(','))):
    lanternfishes[l] += 1

def simulate(lfs):
    new_lfs = lfs.pop(0)
    lfs[6] += new_lfs
    lfs.append(new_lfs)   

def ex1():
    lf1 = lanternfishes.copy()
    for i in range(80):
        simulate(lf1)
    return sum(lf1)

def ex2():    
    lf2 = lanternfishes.copy()
    for i in range(256):
        simulate(lf2)
    return sum(lf2)

print("ex1 : %d" % ex1())
print("ex2 : %d" % ex2())



