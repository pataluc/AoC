#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

def debug(s):
    sys.stderr.write("%s\n" % s)

def dfs(graph, u, k, path, used):
    path.append(u)
    debug(path)
    debug(u)
    debug(len(graph))
    if u + 1 == len(graph) and k == used:
        return path
    if u in graph:
        for v in graph[u]:
            if used < k:
                result = dfs(graph, v, k, path, used+1)
                if result is not None:
                    return result
    path.pop()

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

debug(graph)

result = dfs(graph, 1, k, [], 0)
if result is not None:
    print(" ".join(str(x) for x in result), end='')
else:
    print("IMPOSSIBLE", end='')