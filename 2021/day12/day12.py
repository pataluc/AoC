from collections import defaultdict
  
# This class represents a directed graph
# using adjacency list representation
class Graph:

  
    def __init__(self, vertices):
        # No. of vertices
        self.V = len(vertices)
        self.points = vertices
         
        # default dictionary to store graph
        self.graph = defaultdict(list)
  
    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
  
    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''
    def printAllPathsUtil(self, u, d, visited, path, paths = []):
        
 
        # Mark the current node as visited and store in path
        visited[u] = not self.points[u].isupper()
        path.append(u)
 
        # If current vertex is same as destination, then print
        # current path[]
        if u == d and sum(map(lambda x: 1 if "2" in self.points[x] else 0, path)) <= 1:

            #print(",".join(map(lambda x: self.points[x], path)).replace("2", ""))
            paths.append(",".join(map(lambda x: self.points[x], path)).replace("2", ""))
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)
                     
        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False
        return paths
  
  
    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d):
 
        # Mark all the vertices as not visited
        visited = [False]*(self.V)
 
        # Create an array to store paths
        path = []
 
        # Call the recursive helper function to print all paths
        c = self.printAllPathsUtil(s, d, visited, path)
        return c
  
  
  
def load(file):
    return [ tuple(l.rstrip().split("-")) for l in open(file, "r").readlines()]

def get_paths(input):
    points = list(set(map(lambda x: x[0], input)).union(set(map(lambda x: x[1], input))))
    points.sort()
        
    g = Graph(points)
    #print(points, len(points))
    for a, b in input:
        g.addEdge(points.index(a), points.index(b))
        g.addEdge(points.index(b), points.index(a))
        
    #print(g.graph)
    #print("Following are all different paths from start to end :")
    return g.printAllPaths(points.index("start"), points.index("end"))

def get_paths2(input):
    points = list(set(map(lambda x: x[0], input)).union(set(map(lambda x: x[1], input))))
    points += list(map(lambda x: "%s2" % x,  filter(lambda x: x not in ['start', 'end'] and x.islower(), points)))    
    points.sort()
        
    g = Graph(points)
    #print(points, len(points))
    for a, b in input:
        g.addEdge(points.index(a), points.index(b))
        g.addEdge(points.index(b), points.index(a))
        if a not in ['start', 'end'] and a.islower():
            g.addEdge(points.index("%s2" % a), points.index(b))
            g.addEdge(points.index(b), points.index("%s2" % a))
        if b not in ['start', 'end'] and b.islower():
            g.addEdge(points.index(a), points.index("%s2" % b))
            g.addEdge(points.index("%s2" % b), points.index(a))

        
    #print(g.graph)
    #print("Following are all different paths from start to end :")
    return g.printAllPaths(points.index("start"), points.index("end"))


def ex1(lines):    
    return get_paths(lines)

def ex2(lines):
    c = set(get_paths2(lines))
    print(c)
    print(len(c))
    return len(c)

sample = load("sample.txt")
sample1 = load("sample1.txt")
sample2 = load("sample2.txt")
input = load("input.txt")

#assert ex1(sample) == 10
#assert ex1(sample1) == 19
#assert ex1(sample2) == 226
#print("ex1 : %d" % ex1(input))

#assert ex2(sample) == 36
#assert ex2(sample1) == 103
#assert ex2(sample2) == 3509
print("ex1 : %d" % ex2(input))