#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))

val = 0

states = []
observes  =[]

for n in range(int(lines[0])):
    states.append(lines[1 + n*8])
    observe = [
       '0' if lines[3 + n*8][2] == ' ' else '1',
       '0' if lines[4 + n*8][1] == ' ' else '1',
       '0' if lines[4 + n*8][3] == ' ' else '1',
       '0' if lines[5 + n*8][2] == ' ' else '1',
       '0' if lines[6 + n*8][1] == ' ' else '1',
       '0' if lines[6 + n*8][3] == ' ' else '1',
       '0' if lines[7 + n*8][2] == ' ' else '1'
    ]
    observes.append(''.join(observe))


# print([(''.join(list(map(lambda x: x[i], states))), ''.join(list(map(lambda x: x[i], observes)))) for i in range(7)])
defaults = set()
ans = [' '] * 7
for j in range(7):
    sys.stderr.write("Looking for %s\n" % (chr(65 + j)))
    for i in range(7):

        s = ''.join(list(map(lambda x: x[i], states)))
        o = ''.join(list(map(lambda x: x[j], observes)))
        sys.stderr.write("%d | %s %s equals? %s\n" % (i, s, o, str(s==o)))

        if s == o:
            sys.stderr.write("%s is in %d \n" % (chr(65 + j), i))
            ans[i] = chr(65 + j)
            # print(chr(65 + j), end = '')
            # break
print(''.join(ans))