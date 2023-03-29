#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

def debug(s):
    sys.stderr.write("%s\n" % s)

lines = sys.stdin.readlines()

bosses = dict()

for line in lines[1:]:
    agent, boss = line.strip().split(' ')

    if boss in bosses:
        bosses[boss].append(agent)
    else:
        bosses[boss] = [agent]

debug(bosses)
print("1 ", end='')
previous = ['0']

for i in range(9):
    debug(previous)
    agents = sum([bosses[agent] if agent in bosses else [] for agent in previous], [])
    debug(agents)
    print("%d " % len(agents), end='')
    previous = agents