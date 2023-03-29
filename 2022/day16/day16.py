import re
from os import path
from sys import argv

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    data = dict()
    for groups in [ re.match(r'Valve (.*) has flow rate=(.*); tunnels* leads* to valves* (.*)', line).groups() for line in open(file_path(file), "r").read().split("\n") ]:
        # print(groups)
        data[groups[0]] = (int(groups[1]), groups[2].split(", "))
    return data

def bfs(graph, start, endvalue):
    queue  = []
    queue.append([start])
    visited = set()

    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == endvalue:
            return path
        # print(graph[node])
        for neighbour in graph[node][1]:
            if neighbour not in visited:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                visited.add(neighbour)

debug = True
def ex1(data):
    total_pressure = 0
    opened_valves = set()
    closed_valves = set(filter(lambda x: data[x][0] > 0, data))
    current = 'AA'
    print(closed_valves)

    distances = dict()
    for v1 in closed_valves:
        if v1 != current and (v1, current) not in distances:
            distances[(v1, current)] = distances[(current, v1)] = bfs(data, v1, current)
        for v2 in closed_valves:
            if v1 != v2 and (v1, v2) not in distances:
                distances[(v1, v2)] = distances[(v2, v1)] = bfs(data, v1, v2)
    
    mn = 0
    next_valve = None
    while mn <= 5:
        mn += 1

        print("== Minute %d ==" % mn) if debug else None
        if len(opened_valves):
            current_pressure = sum(map(lambda x: data[x][0], opened_valves))
            total_pressure += current_pressure
            print("Valves", opened_valves, "are open, releasing: %d" % current_pressure)
        else:
            print("No valves are open.")

        if next_valve == current:
            print("You open valve %s." % current)
            closed_valves.remove(next_valve)
            opened_valves.add(next_valve)


        options = [((30 - mn - len(distances[(current, v)])) * data[v][0] // len(distances[(current, v)]), v) for v in closed_valves]
        options.sort()
        pressure, next_valve = options[-1]

        print("You move to valve %s. (route to %s)" % (distances[(current, next_valve)][0], next_valve), distances[(current, next_valve)]) if debug else None
        current = distances[(current, next_valve)][0]
        
        # ouverture vanne si > 0 et pas ouverte
        # for neighbour in data[current][1]:


    return

def ex2(data):
    return

sample = load("sample.txt")
# print(sample)
assert ex1(sample) == 1651

data = load("input.txt")
print("ex1 : %s" % ex1(data))


assert ex2(sample) == 56000011
print("ex2 : %s" % ex2(data))
