#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
from collections import defaultdict

def debug(s):
    sys.stderr.write("%s\n" % s)

lines = [ l.rstrip() for l in sys.stdin.readlines()[1:]]
for i in range(len(lines)):
    for j in range(len(lines[1])):
        if lines[i][j] == 'A':
            a = (i,j)
        if lines[i][j] == 'B':
            b = (i,j)

def get_neighbours(tile, graph):
    height = len(graph)
    width = len(graph[-1])
    x, y = tile
    out = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(a, b) for a, b in out if 0 <= a < height and 0 <= b < width]    

def _deconstruct_path(tentative_parents, end):
    if end not in tentative_parents:
        return None
    cursor = end
    path = []
    while cursor:
        path.append(cursor)
        cursor = tentative_parents.get(cursor)
    return list(reversed(path))

def dijkstra(weighted_graph, start, end):
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

        neighbours = get_neighbours(current, weighted_graph)
        
        for neighbour in neighbours:
            distance = 1 if weighted_graph[neighbour[0]][neighbour[1]] == '#' else 0
            if neighbour in visited_nodes:
                continue
            neighbour_distance = distance_from_start[current] + distance
            if neighbour_distance < distance_from_start[neighbour]:
                distance_from_start[neighbour] = neighbour_distance
                tentative_parents[neighbour] = current
                nodes_to_visit.add(neighbour)

    # print(tentative_parents)
    path = _deconstruct_path(tentative_parents, end)

    result = 0
    if path is None:
        print('0')
        exit()
    for t in path[1:]:
        result += 1 if weighted_graph[t[0]][t[1]] == '#' else 0

    return result

# debug(graph)
print(a)
print(b)

print(dijkstra(lines, a, b))