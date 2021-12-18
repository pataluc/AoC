def load(file):
    return open(file, "r").readlines()

def find_nested4(term, depth = 1):
    #print(" " * depth, "parsing %s, depth: %d" % (term, depth))
    for index, element in enumerate(term):
        #print(" " * depth, index, element)
        if isinstance(element, list):
            #print(" " * depth, element, "is a list")
            if depth == 4:
                #print(" " * depth, "depth is 4, exiting with element")
                return element, index
            else:
                #print(" " * depth, "depth is less than 4 diving into ", element)
                r = find_nested4(element, depth + 1)
                #print(" " * depth, "result: ", r)
                if r != (None, None):
                    r = r[0], [index] + r[1] if isinstance(r[1], list) else [index] + [r[1]]
                    #print(" " * depth, "return: ", r)
                    return r
        #else:
        #    print(" " * depth, element, "is a scalar")
    return None, None

def set_previous_scalar(term, index, value):
    #print("add %d on previous scalar in " % value, term, ", index %d" % index)
    if not isinstance(term[index], list):
        term[index] += value
    else:
        term[index] = set_previous_scalar(term[index], -1, value)
    return term

def set_next_scalar(term, index, value):
    #print("add %d on next scalar in " % value, term, ", index %d" % index)
    if not isinstance(term[index], list):
        term[index] += value
    else:
        term[index] = set_next_scalar(term[index], 0, value)
    return term

def s_explode(term):
    #print("explode: \n  before: ", term)
    nested, position = find_nested4(term)
    if nested != None:
        #print(position)
        term[position[0]][position[1]][position[2]][position[3]] = 0
        
        #print("        : ", term)
        if 0 <= position[3] - 1 < len(term[position[0]][position[1]][position[2]]):
            term[position[0]][position[1]][position[2]] = set_previous_scalar(term[position[0]][position[1]][position[2]], position[3] - 1, nested[0])
        elif 0 <= position[2] - 1 < len(term[position[0]][position[1]]):
            term[position[0]][position[1]] = set_previous_scalar(term[position[0]][position[1]], position[2] - 1, nested[0])
        elif 0 <= position[1] - 1 < len(term[position[0]]):
            term[position[0]] = set_previous_scalar(term[position[0]], position[1] - 1, nested[0])
        elif 0 <= position[0] - 1 < len(term):
            term = set_previous_scalar(term, position[0] - 1, nested[0])
            
        if 0 <= position[3] + 1 < len(term[position[0]][position[1]][position[2]]):
            term[position[0]][position[1]][position[2]] = set_next_scalar(term[position[0]][position[1]][position[2]], position[3] + 1, nested[1])
        elif 0 <= position[2] + 1 < len(term[position[0]][position[1]]):
            term[position[0]][position[1]] = set_next_scalar(term[position[0]][position[1]], position[2] + 1, nested[1])
        elif 0 <= position[1] + 1 < len(term[position[0]]):
            term[position[0]] = set_next_scalar(term[position[0]], position[1] + 1, nested[1])
        elif 0 <= position[0] + 1 < len(term):
            term = set_next_scalar(term, position[0] + 1, nested[1])


    #print("  after: ", term)

    #if nested != None:
    #    print(nested[max(-1, 0)], nested[max(1, 0)])
        
    return term

def s_split(term, depth = 0):
    changed = False
    for index, element in enumerate(term):
        if isinstance(element, list):
            s = s_split(element, depth + 1)
            if s != None:
                term[index] = s[0]
                changed = s[1]
                return term, changed
        elif element >= 10:
            term[index] = [element // 2, element - element // 2]
            return term, True
    if depth == 0:
        #print(term)
        return term, changed

def magnitude(term):
    r = 3 * (term[0] if not isinstance(term[0], list) else magnitude(term[0]))
    r += 2 * (term[1] if not isinstance(term[1], list) else magnitude(term[1]))
    return r

def reduce(term):
    while find_nested4(term)[0] != None:
        term = s_explode(term)
        #print("after explode: ", term)
    
    term, changed = s_split(term)
    #print("after split: ", term)
    if changed:
        term = reduce(term)
        return term
    else:
        return term


def ex1(lines):
    r = eval(lines[0])
    for i in range(1, len(lines)):
        #print("\n ", r)
        #print("+", lines[i])
        #print(" = ", [r, lines[i]])
        r = reduce([r, eval(lines[i])])
        #print("=", r)
    return magnitude(r)

def ex2(lines):
    max = 0
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i != j:
                #print([lines[i], lines[j]], " -> ", end = "")
                r = magnitude(reduce([eval(lines[i]), eval(lines[j])]))
                #print(r)
                if r > max:
                    max = r
                #print([lines[j], lines[i]], " -> ", end = "")
                r = magnitude(reduce([eval(lines[j]), eval(lines[i])]))
                #print(r)
                if r > max:
                    max = r
    #print(max)
    return max



assert s_explode([[[[4,0],[5,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]) \
    == [[[[4,0],[5,4]],[[0,[7,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]

assert s_explode([[[[9,8],1],2],3]) == [[[[9,8],1],2],3]
assert s_explode([[[[[9,8],1],2],3],4]) == [[[[0,9],2],3],4]
assert s_explode([7,[6,[5,[4,[3,2]]]]]) == [7,[6,[5,[7,0]]]]
assert s_explode([[6,[5,[4,[3,2]]]],1]) == [[6,[5,[7,0]]],3]
assert s_explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]) == [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
assert s_explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]) == [[3,[2,[8,0]]],[9,[5,[7,0]]]]

assert s_split([[[[0,7],4],[15,[0,13]]],[1,1]])[0] == [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
assert s_split([[[[0,7],4],[[7,8],[0,13]]],[1,1]])[0] == [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
assert s_split([[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]])[0] == [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]

assert magnitude([[1,2],[[3,4],5]]) == 143
assert magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]]) == 1384
assert magnitude([[[[1,1],[2,2]],[3,3]],[4,4]]) == 445
assert magnitude([[[[3,0],[5,3]],[4,4]],[5,5]]) == 791
assert magnitude([[[[5,0],[7,4]],[5,5]],[6,6]]) == 1137
assert magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]) == 3488

assert reduce([[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]) == [[[[0,7],4],[[7,8],[6,0]]],[8,1]]


sample = load("2021/day18/sample.txt")
r = ex1(sample)
assert r == 3488
sample2 = load("2021/day18/sample2.txt")
r = ex1(sample2)
assert r == 4140

input = load("2021/day18/input.txt")
print("ex1 : %d" % ex1(input))

sample2 = load("2021/day18/sample2.txt")
assert ex2(sample2) == 3993

input = load("2021/day18/input.txt")
print("ex2 : %d" % ex2(input))
