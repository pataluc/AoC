import sys, re
lines = open("%s_input.txt" % sys.argv[0].split('.')[0], "r")

def getRow(line):
    return int(line.replace('F', '0').replace('B', '1')[0:7], 2)

def getCol(line):
    return int(line.replace('R', '1').replace('L', '0')[7:10], 2)

def getSeatId(line):
    return int(line.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0'), 2)

maxp = 0
seats = []

for line in lines:
    #p = 8*getRow(line)+getCol(line)
    p = getSeatId(line)
    if p > maxp:
        maxp = p
    seats.append(p)

print(maxp)

seats_sorted = sorted(seats)
my_seat = seats_sorted[0]

for i in range(1, len(seats_sorted)):
    if seats_sorted[i] != seats_sorted[i-1] + 1:
        print(seats_sorted[i]-1)
