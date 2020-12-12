import sys, re
f = open("%s_input.txt" % sys.argv[0].split('_')[0], "r")

total = 0
group_answers = dict()
group_size = 0

for line in f:
    if line == "\n":
        print('new group, previous group size: %d, total= %d' % (group_size, total))
        print(group_answers)
        
        for answers_count in group_answers.values():
            if answers_count == group_size:
                total += 1
        group_answers = dict()
        group_size = 0
    else :        
        group_size += 1
        for char in line.rstrip():
            group_answers[char] = group_answers[char] + 1 if char in group_answers else 1



for answers_count in group_answers.values():
    if answers_count == group_size:
        total += 1
        
print(total)