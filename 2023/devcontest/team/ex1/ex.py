#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

def debug(s):
    sys.stderr.write("%s\n" % s)

lines = list(map(str.strip, sys.stdin.readlines()))

w, _ = map(int, lines[0].strip().split(" "))
for line in lines[1:]:
    for i in range(w):
        if '#' in [line[i], line[-1 * i - 1]]:
            print('#', end='')
        else:
            print('.', end='')
    print('')