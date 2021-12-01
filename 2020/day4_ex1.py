import sys, re
f = open("%s_input.txt" % sys.argv[0].split('_')[0], "r")

passports = []
passport = dict()

for line in f:    
    if line == "\n":
        passports.append(passport)
        passport = dict()
    else:
        for field in line.rstrip().split(" "):
            (key, value) = field.split(":")
            if key != "cid":
                passport[key] = value

passports.append(passport)

print(passports[len(passports)-1])

valid = 0
for passport in passports:
    if len(passport) == 7:
        valid += 1

print(valid)