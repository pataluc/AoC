#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))

for i in range(int(lines[0]), -1, -1):
    # print(i)
    print(format(i, '#0%db' % (2 + int(lines[1]))).replace('0b', ''))