#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import math

def debug(s):
    sys.stderr.write("%s\n" % s)

def get_coord(line):
    tokens = line.split(' ')
    return int(tokens[0]), int(tokens[1])
    
def get_time(line):
    h = line.split(' ')[-1].split(':')
    return int(h[0])*3600 + (int(h[1]) * 60) + int(h[2])

lines = sys.stdin.readlines()

distance = 0
for i, line in enumerate(lines[1:]):
    x2, y2 = get_coord(line)
    x1, y1 = get_coord(lines[i])
    distance += math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

duration = get_time(lines[-1]) - get_time(lines[0])

mean = 3.6 * distance / duration
print("%0.2f" % mean)