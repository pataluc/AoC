#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = sys.stdin.readlines()

for b in lines[1:]:
    if len(list(filter(lambda x: b == x, lines))) == 2:
        print(b)
        exit()