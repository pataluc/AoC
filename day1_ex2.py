f = open("day1_input.txt", "r")

t = []
for x in f:
    t.append(int(x))

for x1 in t:
    for x2 in t:
        for x3 in t:
            if x1+x2+x3 == 2020:
                print(x1*x2*x3)
                break
        if x1+x2+x3 == 2020:
            break
    if x1+x2+x3 == 2020:
        break
