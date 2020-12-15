import time

# ex 1
#puzzle = [16,12,1,0,15,7,11]
#turn = len(puzzle)
#
#while turn < 2020:
#    turn += 1
#
#    if puzzle.count(puzzle[-1]) == 1:
#        puzzle.append(0)
#    else:
#        puzzle.append(turn - (len(puzzle) - puzzle[:-1][::-1].index(puzzle[-1])))
#print("ex 1: %d" % puzzle[-1])


# ex 2
start = time.time()

puzzle = [16,12,1,0,15,7,11]
last_occur = dict()
for i in range(len(puzzle)):
    last_occur[puzzle[i]] = [i + 1]
turn = len(puzzle)

while turn < 30000000:
    turn += 1
    if turn % 100000 == 0:
        print("## %d " % turn)

    if len(last_occur[puzzle[-1]]) < 2:        
        puzzle.append(0)
        last_occur[0].append(turn)
    else:
        puzzle.append(turn - 1 - last_occur[puzzle[-1]][-2])
        if puzzle[-1] in last_occur:
            last_occur[puzzle[-1]].append(turn)
        else:
            last_occur[puzzle[-1]] = [turn]


print("ex 2: %d (en %f secondes)" % (puzzle[-1], time.time() - start))
