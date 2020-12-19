import sys
import re
lines = open("%s_input.txt" % sys.argv[0].split('.')[0], "r").readlines()

RECURSE_MAX = 5

rules = dict()
for line in filter(lambda x: ":" in x, lines):
    rule_nb, rule = line.rstrip().split(": ")
    rules[rule_nb] = rule if "\"" not in rule else rule[1]

messages = set()    
for line in filter(lambda x: ":" not in x and x != "\n", lines):
    messages.add(line.rstrip())

def resolve_rules(rule_nb, root = True, recurse8 = 0, recurse11 = 0):

    recurse8 = recurse8 + 1 if rule_nb == "8" else recurse8
    recurse11 = recurse11 + 1 if rule_nb == "11" else recurse11

    if recurse8 > RECURSE_MAX or recurse11 > RECURSE_MAX:
        return ""
    else:
        result = ""
        for element in rules[rule_nb].split(" "):
            if element in ["a", "b", "|"]:
                result += "%s " % element
            elif "|" in rules[element]:
                result += "(%s) " % resolve_rules(element, False, recurse8, recurse11)
            else:
                result += "%s " % resolve_rules(element, False, recurse8, recurse11)

        return result if not root else ("^%s$" % result).replace(" ", "")


# Ex 1
regex = resolve_rules("0")
print("Ex 1: %d" % len(set(filter(lambda m: re.match(regex, m), messages))))


# Ex 2
rules["8"] = "42 | 42 8"
rules["11"] = "42 31 | 42 11 31"

regex = resolve_rules("0")
print("Ex 2: %d" % len(set(filter(lambda m: re.match(regex, m), messages))))
