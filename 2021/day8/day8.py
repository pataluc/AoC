def load(file):
    return [(l.split()[:10], l.split()[-4:]) for l in open(file, "r").readlines()]

def ex1(lines):
    l = [item for sublist in list(map(lambda x: x[1], lines)) for item in sublist]
    return len(list(filter(lambda x: len(x) in [2, 4, 3, 7], l)))

def sort_string(s):
    s = list(s)
    s.sort()
    return ''.join(s)

def guess(uniques):
    inputs = [''] * 10
    lengths = {}
    points = {}
    for s in uniques:
        if len(s) in [2,4,3,7]:
            lengths[len(s)] = sort_string(s)
        else:
            lengths[len(s)] = [sort_string(s)] if len(s) not in lengths else lengths[len(s)] + [sort_string(s)]
    
    # get 1
    inputs[1] = lengths[2]
    # get 7
    inputs[7] = lengths[3]
    # get 1
    inputs[4] = lengths[4]
    # get 1
    inputs[8] = lengths[7]

    # get N 
    points['N'] = ''.join(list(set(lengths[3]) - set(list(lengths[2]))))

    # get C
    for c in list('abcdefg'):
        if c in lengths[4] and all(map(lambda x : c in x, lengths[5])):
            points['C'] = c
            continue

    # get NW
    for c in list(lengths[4]):
        if c not in lengths[2] and c != points['C']:
            points['NW'] = c
            continue
    
    # get 9 and S
    for i6 in lengths[6]:
        r = set(i6) - set(list(inputs[4]) + list(inputs[7]))
        if len(r) == 1:
            points['S'] = list(r)[0]
            inputs[9] = i6
    lengths[6].remove(inputs[9])

    # get 0, 6 and NE
    for i6 in lengths[6]:
        if points['C'] not in i6:
            inputs[0] = i6
        else:
            inputs[6] = i6
            points['NE'] = list(set(list(inputs[8])) - set(list(i6)))[0]

    # get SW
    points['SW'] = list(set(list(inputs[8])) - set(list(inputs[9])))[0]
    # get SE
    for c in list('abcdefg'):
        if c not in points.values():
            points['SE'] = c
    
    # get 2
    inputs[2] = sort_string(points['N'] + points['NE'] + points['C'] + points['SW'] + points['S'])
    # get 3
    inputs[3] = sort_string(points['N'] + points['NE'] + points['C'] + points['SE'] + points['S'])
    # get 5
    inputs[5] = sort_string(points['N'] + points['NW'] + points['C'] + points['SE'] + points['S'])

    output = {}
    for i, v in enumerate(inputs):
        output[v] = i

    return output

def translate(line):
    uniques, digit = line
    k = guess(uniques)
    return int(''.join(list(map(lambda x: str(k[sort_string(x)]), digit))))


def ex2(lines):
    return sum(list(map(lambda x: translate(x), lines)))

lines = load("sample.txt")
assert ex1(lines) == 26
assert ex2(lines) == 61229

lines = load("input.txt")
print("ex1 : %d" % ex1(lines))
print("ex2 : %d" % ex2(lines))



