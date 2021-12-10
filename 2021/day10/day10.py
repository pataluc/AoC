import re

def load(file):
    return  [ l.rstrip() for l in open(file, "r").readlines()]

def remove_chunks(line):
    while "()" in line or "{}" in line or "<>" in line or "[]" in line:
        for chunk in ["()", "[]", "{}", "<>"]:
            line = line.replace(chunk, "")
    return line

def line_score_ex1(line):    
    values = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }
    line = re.sub(r'[\(\[\{\<]', '', remove_chunks(line))
    
    return values[line[0]] if len(line) > 0 else 0

def ex1(lines):
    return sum(map(line_score_ex1, lines))

def line_score_ex2(line):
    values = {
        '(': 1,
        '[': 2,
        '{': 3,
        '<': 4
    }
    line = remove_chunks(line)
    if re.match(r'.*[\)\]\}\>].*', line):
        return 0
    else:
        score = 0
        for c in line[::-1]:
            score = score * 5 + values[c]
        return score

def ex2(lines):
    scores = list(filter(lambda x : x > 0, map(line_score_ex2, lines)))    
    scores.sort()
    return scores[len(scores) // 2]


lines = load("sample.txt")
assert ex1(lines) == 26397
assert ex2(lines) == 288957

print("######################")
lines = load("input.txt")
print("ex1 : %d" % ex1(lines))
print("ex2 : %d" % ex2(lines))



