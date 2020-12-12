import sys, re
f = open("%s_input.txt" % sys.argv[0].split('_')[0], "r")

valid = 0


for line in f:
    (omin, omax, letter, password) = re.findall(r"[\w']+", line)

    o = len(re.findall(letter, password))
    if (o <= int(omax) and o >= int(omin)):
        valid += 1

print(valid)