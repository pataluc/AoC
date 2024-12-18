#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))

from collections import defaultdict

wires = defaultdict(list)

for line in lines[1:]:
    sys.stderr.write(line)
    l, color = line.split(' ')
    wires[color].append(int(l))

# print(wires)

print(max(map(sum, wires.values())))

