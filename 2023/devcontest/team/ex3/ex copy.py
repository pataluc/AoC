#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

def debug(s):
    sys.stderr.write("%s\n" % s)

lines = [ l.rstrip() for l in sys.stdin.readlines()[1:]]
for i in range(1, len(lines)):
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
            
def a_star(graph, start, end):
    
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
            debug("path does not exists!")
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
            print(reconst_path)
            print("".join(list(map(lambda p: graph[p[0]][p[1]],reconst_path))))
            for t in reconst_path[1:]:
                result += 1 if graph[t[0]][t[1]] == '#' else 0
            debug(result)
            return result
        neighbours = get_neighbours(n, graph)
        
        for m in neighbours:
            distance = 1 if graph[m[0]][m[1]] == '#' else 0

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

    debug('Path does not exist!')
    return None

debug(lines)
print(a)
print(b)
print('----')
a_star(lines, a, b)