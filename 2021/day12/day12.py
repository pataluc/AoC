def load(file):
    return [ tuple(l.rstrip().split("-")) for l in open(file, "r").readlines()]

def is_valid_neighbour1(new_node, path):
    return new_node not in path

def is_valid_neighbour2(new_node, path):
    small_caves_freq = {}
    for node in path:
        if node.isupper():
            continue
        if node not in small_caves_freq:
            small_caves_freq[node] = 0
        small_caves_freq[node] += 1
    if new_node not in small_caves_freq:
        return True
    if new_node == "start" or new_node == "end":
        return False
    return len(small_caves_freq) == sum(small_caves_freq.values())

def solve(lines, is_valid_neighbour):
    edges = {}
    for i, j in lines:
        if i not in edges:
            edges[i] = set()
        edges[i].add(j)
        if i != "start" and j != "end":
            if j not in edges:
                edges[j] = set()
            edges[j].add(i)
    
    paths = [['start']]
    while True:
        print(paths)
        new_paths = []
        for path in paths:
            last_node = path[-1]
            if last_node == 'end' or last_node not in edges:
                new_paths.append(path)
                continue

            for neighbour in edges[last_node]:
                if neighbour.islower() and not is_valid_neighbour(neighbour, path):
                    continue

                new_paths.append(path + [neighbour])
    
        if len(paths) == len(new_paths):
            break

        paths = new_paths

    #print(len(paths))
    return len(paths)

sample = load("sample.txt")
sample1 = load("sample1.txt")
sample2 = load("sample2.txt")
input = load("input.txt")

assert solve(sample, is_valid_neighbour1) == 10
exit()
assert solve(sample1, is_valid_neighbour1) == 19
assert solve(sample2, is_valid_neighbour1) == 226
print("ex1 : %d" % solve(input, is_valid_neighbour1))

assert solve(sample, is_valid_neighbour2) == 36
assert solve(sample1, is_valid_neighbour2) == 103
assert solve(sample2, is_valid_neighbour2) == 3509
print("ex2 : %d" % solve(input, is_valid_neighbour2))