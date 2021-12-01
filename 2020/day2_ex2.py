import sys, re
f = open("%s_input.txt" % sys.argv[0].split('_')[0], "r")

valid = 0


for line in f:
    (pos1, pos2, letter, password) = re.findall(r"[\w']+", line)

    if (bool(password[int(pos1)-1] == letter) != bool(password[int(pos2)-1] == letter)):
        valid += 1

print(valid)