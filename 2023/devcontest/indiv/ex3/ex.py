#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

def debug(s):
    sys.stderr.write("%s\n" % s)

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

def to_str(path):
    return " ".join(map(str, path))


def find_path(path):
    # debug(to_str(path))
    if len(path) == k + 1 and n == path [-1]:
        # debug("trouvé")
        print(to_str(path))
        exit()
    elif len(path) <= k + 1:
        for child in graph[path[-1]]:
            path.append(child)
            find_path(path)
            path.pop()
    # else:
    #     debug("oversized path")


# debug("going from 1 to %d in %d slopes (path of %d nodes)" %(m, k, k+1))

find_path([1])
print("IMPOSSIBLE")
