import sys
import re

lines = open("%s_input.txt" % sys.argv[0].split('.')[0], "r")

def do_the_math(line):
    #print("do the math for %s" % line)
    if "(" in line:
        s = re.findall(r"(.*)(\([^)]*\))(.*)", line)
        #print("returns %s" % s[0][0] + str(do_the_math(s[0][1][1:-1])) + s[0][2])
        return do_the_math(s[0][0] + str(do_the_math(s[0][1][1:-1])) + s[0][2])

    else:
        t = line.split(" ")
        if len(t) > 3:
            #print("returns %s (invoke do_themath)" % do_the_math(" ".join([str(int(t[0])*int(t[2]) if t[1] == "*" else int(t[0])+int(t[2]))] + t[3:])))
            return do_the_math(" ".join([str(int(t[0])*int(t[2]) if t[1] == "*" else int(t[0])+int(t[2]))] + t[3:]))
        else:
            #print("returns %d (calcul)" % (int(t[0])*int(t[2]) if t[1] == "*" else int(t[0])+int(t[2])))
            return int(t[0])*int(t[2]) if t[1] == "*" else int(t[0])+int(t[2])

def do_the_math2(line):
    #print(line)
    if "(" in line:
        s = re.findall(r"(.*)(\([^)]*\))(.*)", line)
        return do_the_math2(s[0][0] + str(do_the_math2(s[0][1][1:-1])) + s[0][2])
        
    if "+" in line:
        s = re.findall(r"(.* )*([0-9]+) \+ ([0-9]+)(.*)", line)
        #print(s)
        return do_the_math2(s[0][0] + str(int(s[0][1]) + int(s[0][2])) + s[0][3])
    else:
        prod = 1
        for p in map(int, line.split(" * ")):
            prod = prod * p
        return prod

# tests
#print("26 = ? %d" % do_the_math("2 * 3 + (4 * 5)"))
#print("71 = ? %d" % do_the_math("1 + 2 * 3 + 4 * 5 + 6"))
#print("437 = ? %d" % do_the_math("5 + (8 * 3 + 9 + 3 * 4 * 3)"))
#print("12240 = ? %d" % do_the_math("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))
#print("13632 = ? %d" % do_the_math("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))

# Ex 1
#print("Ex 1: %d" % sum(map(do_the_math, lines)))


# Ex 2
print("51 = ? %d" % do_the_math2("1 + (2 * 3) + (4 * (5 + 6))"))
print("46 = ? %d" % do_the_math2("2 * 3 + (4 * 5)"))
print("1445 = ? %d" % do_the_math2("5 + (8 * 3 + 9 + 3 * 4 * 3)"))
print("669060 = ? %d" % do_the_math2("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"))
print("23340 = ? %d" % do_the_math2("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"))
print("Ex 2: %d" % sum(map(do_the_math2, lines)))