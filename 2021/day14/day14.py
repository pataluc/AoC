
def load(file):
    lines = open(file, "r").readlines()
    return lines[0].strip(), dict(map(lambda x: tuple(x.strip().split(" -> ")), lines[2:]))

def process(template, instructions):
    d = {}
    for k in template.keys():
        if k in instructions:
            if k[0] + instructions[k] in d:
                d[k[0] + instructions[k]] += template[k]
            else:
                d[k[0] + instructions[k]] = template[k]
            if instructions[k] + k[1] in d:
                d[instructions[k] + k[1]] += template[k]
            else:
                d[instructions[k] + k[1]] = template[k]
        else:
            d[k] = template[k]

    return d


def ex(input, rounds = 1):
    template, intructions = input
    
    t = {}
    for i in range(len(template) - 1):
        if template[i:i+2] in t:
            t[template[i:i+2]] += 1
        else:
            t[template[i:i+2]] = 1

    for i in range(rounds):
        t = process(t, intructions)

    r = {}
    for k in t.keys():
        n = t[k]
        for c in k:
            if c in r:
                r[c] += n
            else:
                r[c] = n
    r[template[0]] += 1
    r[template[-1]] += 1

    l = list(r.values())
    l.sort()
    return ((l[-1]-l[0]) // 2)

sample = load("sample.txt")
assert ex(sample, 10) == 1588

input = load("input.txt")
print("ex1 : %d" % ex(input, 10))

assert ex(sample, 40) == 2188189693529
print("ex2 : %d" % ex(input, 40))