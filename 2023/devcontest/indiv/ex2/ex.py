#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import numpy

def debug(s):
    sys.stderr.write("%s\n" % s)

bobs = 0

for line in sys.stdin.readlines()[1:]:
    for spaces in line.strip().split('X'):
        bobs += len(spaces) // 4
print(bobs)