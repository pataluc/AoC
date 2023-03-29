#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import numpy

def debug(s):
    sys.stderr.write("%s\n" % s)

last_country = ''
last_time = 0

for line in sys.stdin.readlines()[1:]:
    country, dist, speed = line.strip().split(" ")
    t = int(dist) / int(speed)
    if t > last_time:
        last_time = t
        last_country = country
print(last_country)