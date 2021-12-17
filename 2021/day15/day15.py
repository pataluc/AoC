from collections import defaultdict
def load(file):
    return [ list(map(int, l.rstrip())) for l in open(file, "r").readlines() ]

def get_neighbours(tile, scale, graph):
    height = len(graph)
    width = len(graph[-1])
    x, y = tile
    out = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [(a, b) for a, b in out if 0 <= a < width*scale and 0 <= b < height*scale]

def get_weight(graph, p):
    x, y = p
    height = len(graph)
    width = len(graph[-1])
    c = graph[x % width][y % height]
    c = (c + x // width + y // height)
    c = 1 + (c-1) % 9
    return c

def dijkstra(weighted_graph, scale):
    """
    Calculate the shortest path for a directed weighted graph.

    Node can be virtually any hashable datatype.

    :param start: starting node
    :param end: ending node
    :param weighted_graph: {"node1": {"node2": "weight", ...}, ...}
    :return: ["START", ... nodes between ..., "END"] or None, if there is no
            path
    """
    start = (0,0)
    end = (len(weighted_graph)*scale - 1, len(weighted_graph[-1])*scale -1)

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

        neighbours = list(filter(lambda x: start[0] <= x[0] <= end[0] and start[1] <= x[1] <= end[1], get_neighbours(current, scale, weighted_graph)))
        
        for neighbour in neighbours:
            distance = get_weight(weighted_graph, current)
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
        result += get_weight(weighted_graph, t)

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

def a_star(graph, scale):
    start = (0,0)
    end = (len(graph)*scale - 1, len(graph[-1])*scale -1)
    open_list = set([start])
    closed_list = set([])
    poo = {}
    poo[start] = 0
    par = {}
    par[start] = start
    
    while len(open_list) > 0:
        n = None

        for v in open_list:
            if n == None or (poo[v] + (end[0] - v[0]) + (end[1] - v[1])) < (poo[n] +  (end[0] - n[0]) + (end[1] - n[1])):
                n = v
        
        if n == None:
            print("path does not exists!")
            return None

        if n == end:
            reconst_path = []
            while par[n] != n:
                reconst_path.append(n)
                n = par[n]
            reconst_path.append(start)
            reconst_path.reverse()

            #print("path found: ", reconst_path)
            result = 0
            for t in reconst_path[1:]:
                result += get_weight(graph, t)
            print(result)
            return result

        neighbours = list(filter(lambda x: start[0] <= x[0] <= end[0] and start[1] <= x[1] <= end[1], get_neighbours(n, scale, graph)))
        
        for m in neighbours:
            distance = get_weight(graph, n)

            if m not in open_list and m not in closed_list:
                open_list.add(m)
                par[m] = n
                poo[m] = poo[n] + distance
            else:
                if poo[m] > poo[n] + distance:
                    poo[m] = poo[n] + distance
                    par[m] = n
                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)
        
        open_list.remove(n)
        closed_list.add(n)

    print('Path does not exist!')
    return None

method = a_star
method = dijkstra

sample = load("sample.txt")
input = load("input.txt")

assert method(sample, 1) == 40
print("ex1 : %d" % method(input, 1))

assert method(sample, 5) == 315
print("ex2 : %d" % method(input, 5))