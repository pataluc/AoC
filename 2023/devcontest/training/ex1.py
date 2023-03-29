#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

def debug(s):
    sys.stderr.write("%s\n" % s)
    
subs = {
    '000': '00',
    '111': '1',
    '10': '1'
}
    
f = input()

for p, r in subs.items():
    while p in f:
        f = f.replace(p, r)
print(f)