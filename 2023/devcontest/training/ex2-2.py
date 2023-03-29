#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

def debug(s):
    sys.stderr.write("%s\n" % s)

lines = sys.stdin.readlines()

j = 19

while j > 2:
    col = lines[j].index('.')
    debug(lines[j].strip())
    if lines[j].count('.') == 1 \
        and lines[j - 1].count('.') == 1 \
        and lines[j - 2].count('.') == 1 \
        and lines[j - 3].count('.') == 1 \
        and all([lines[y][col] == '.' for y in range(0, j+1)]):
        print("BOOM %d" % (col + 1))
        exit()
    j = j - 1
print("NOPE")