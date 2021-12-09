def load(file):
    return list(map(int, open(file, "r").readlines()[0].rstrip().split(',')))



def mediane(positions):
    positions.sort()
    l = len(positions)
    if l % 2 == 0:
        return (positions[l // 2] + positions[(l // 2) - 1]) / 2
    else:
        return positions[l // 2]

def ex1(positions):
    target = mediane(positions)
    return sum(abs(p - target) for p in positions)

def ex2(positions):
    best_cost = None
    for target in range(min(positions), max(positions) + 1):
        cost = sum(abs(p - target)*(abs(p - target) + 1) // 2 for p in positions)
        if best_cost is None or cost < best_cost:
            best_cost = cost
    return best_cost

positions = load("sample.txt")
assert ex1(positions) == 37
assert ex2(positions) == 168

positions = load("input.txt")
print("ex1 : %d" % ex1(positions))
print("ex2 : %d" % ex2(positions))



