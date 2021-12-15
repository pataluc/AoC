from collections import defaultdict
def load_ex1(file):
    return [ list(map(int, l.rstrip())) for l in open(file, "r").readlines() ]

def load_ex2(file):
    lines = [ list(map(int, l.rstrip())) for l in open(file, "r").readlines() ]

    # fois 5 en largeur
    for line in lines:
        size = len(line)
        for n in range(4):
            for i in range(size):
                line.append(line[i] + n + 1 if line[i] + n + 1 <= 9 else line[i] + n + 1 - 9)

    # fois 5 en hauteur
    size = len(lines)
    for n in range(4):
        for i in range(size):
            line = []
            for j in lines[i]:
                #print(lines[i])
                line.append(j + n + 1 if j + n + 1 <= 9 else j + n + 1 - 9)
            lines.append(line)
    return lines

def get_neighbours(tile):
    x, y = tile
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

def get_shortest_path(weighted_graph, start, end):
    """
    Calculate the shortest path for a directed weighted graph.

    Node can be virtually any hashable datatype.

    :param start: starting node
    :param end: ending node
    :param weighted_graph: {"node1": {"node2": "weight", ...}, ...}
    :return: ["START", ... nodes between ..., "END"] or None, if there is no
            path
    """

    # We always need to visit the start
    nodes_to_visit = {start}
    visited_nodes = set()
    distance_from_start = defaultdict(lambda: float("inf"))
    # Distance from start to start is 0
    distance_from_start[start] = 0
    tentative_parents = {}

    while nodes_to_visit:
        # The next node should be the one with the smallest weight
        current = min(
            [(distance_from_start[node], node) for node in nodes_to_visit]
        )[1]
        # The end was reached
        if current == end:
            break

        nodes_to_visit.discard(current)
        visited_nodes.add(current)

        neighbours = list(filter(lambda x: start[0] <= x[0] <= end[0] and start[1] <= x[1] <= end[1], get_neighbours(current)))
        
        for neighbour in neighbours:
            distance = weighted_graph[current[0]][current[1]]
            if neighbour in visited_nodes:
                continue
            neighbour_distance = distance_from_start[current] + distance
            if neighbour_distance < distance_from_start[neighbour]:
                distance_from_start[neighbour] = neighbour_distance
                tentative_parents[neighbour] = current
                nodes_to_visit.add(neighbour)

    path = _deconstruct_path(tentative_parents, end)
    result = 0
    for t in path[1:]:
        result += weighted_graph[t[0]][t[1]]
        #print(weighted_graph[f][t], result)

    return result

def _deconstruct_path(tentative_parents, end):
    if end not in tentative_parents:
        return None
    cursor = end
    path = []
    while cursor:
        path.append(cursor)
        cursor = tentative_parents.get(cursor)
    return list(reversed(path))

    

graph = load_ex1("sample.txt")
start = (0,0)
end = (len(graph) - 1, len(graph[-1]) -1)
assert get_shortest_path(graph, start, end) == 40

graph = load_ex1("input.txt")
start = (0,0)
end = (len(graph) - 1, len(graph[-1]) -1)
print("ex1 : %d" % get_shortest_path(graph, start, end))

graph = load_ex2("sample.txt")
start = (0,0)
end = (len(graph) - 1, len(graph[-1]) -1)
assert get_shortest_path(graph, start, end) == 315

graph = load_ex2("input.txt")
start = (0,0)
end = (len(graph) - 1, len(graph[-1]) -1)
print("ex2 : %d" % get_shortest_path(graph, start, end))