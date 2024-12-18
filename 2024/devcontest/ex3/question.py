#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import re

lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))

colors = [
   'Black',
   'Brown',
   'Red',
   'Orange',
   'Yellow',
   'Green',
   'Blue',
   'Purple',
   'Grey',
   'White'
]

val = 0

for line in lines[1:]:
    r1, r2, m = line.split()
    line_val = (10 * colors.index(r1) + colors.index(r2)) * (10**colors.index(m))
    val += line_val

if val < 1000:
    val = str(val)
elif val < 1000000:
    val = '%.4fk' % (val / 1000)
elif val < 1000000000:
    val = '%.4fM' % (val / 1000000)
else:
    val = '%.4fG' % (val / 1000000000)

print(re.sub(r'(\.[0-9][1-9]*)0*', r'\1', val))

