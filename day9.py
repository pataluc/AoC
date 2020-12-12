import sys, re
f = open("%s_input.txt" % sys.argv[0].split('.')[0], "r")

preamble_length = 25

previous = []

all_previous = []


def compute_previous_sums(previous = []):
    sums = set()
    for i in range(0, len(previous)):
        for j in range(i + 1, len(previous)):
            sums.add(previous[i]+previous[j])
    return sums

def get_invalid(previous, preamble_length):
    i = 0
    for line in f:
        i += 1     

        if i > preamble_length:
            if int(line) not in compute_previous_sums(previous):
                return int(line)
            previous.pop(0)

        previous.append(int(line))
        all_previous.append(int(line))

#ex1 
invalid = get_invalid(previous, preamble_length)
print(invalid)

for i in range(0, len(all_previous)):
    j = i
    r = []
    
    while sum(r) < invalid:
        r.append(all_previous[j])
        j += 1
    
    if sum(r) == invalid:
        print(r)
        print(min(r) + max(r))
        exit()