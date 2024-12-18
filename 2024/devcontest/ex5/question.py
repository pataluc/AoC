#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
  lines.append(line.rstrip('\n'))

to_count = int(lines[0], 16)
digits = int(lines[1])

costs_to_zero = {
   '0': 6,
   '1': 8,
   '2': 13,
   '3': 18,
   '4': 22,
   '5': 27,
   '6': 33,
   '7': 36,
   '8': 43,
   '9': 49,
   'a': 55,
   'b': 60,
   'c': 63,
   'd': 68,
   'e': 74,
   'f': 78
}
costs = {
   '0': 6,
   '1': 2,
   '2': 5,
   '3': 5,
   '4': 4,
   '5': 5,
   '6': 6,
   '7': 3,
   '8': 7,
   '9': 6,
   'a': 6,
   'b': 5,
   'c': 3,
   'd': 5,
   'e': 6,
   'f': 4
}

to_count_padded_hex = "{0:#0{1}x}".format(to_count, digits + 2)[2:]

ans = 2 * (to_count + 1)

print("cost of %s (dec: %d, controller already consumes %d)" %(to_count_padded_hex, to_count, ans))
for i in range(digits - 1, -1, -1):
   c = to_count_padded_hex[i]
   before = int(to_count_padded_hex[:i], 16) if i > 0 else 0
   after = int(to_count_padded_hex[i+1:], 16) + 1 if i < digits - 1 else 0

   # print("before: %s, char: %s, after: %s" % (before, c, after))

   ans += before * costs_to_zero['f'] + costs[c] * after + costs_to_zero[hex(int(c, 16) - 1)[2:]] * 16**(digits - i - 1)

   print("  digit: %d, before: %d, after: %d, before * costs_to_zero['f']: %d, costs[c] * after: %d, costs_to_zero[hex(int(c, 16) - 1)[2:]] * 16**(digits - i - 1): %d\n  ans: %d" % \
         (i, before, after, before * costs_to_zero['f'], \
          costs[c] * after, costs_to_zero[hex(int(c, 16) - 1)[2:]] * 16**(digits - i - 1), ans))



#########################""

# ans = 0
# for n in range(to_count, -1, -1):
#     s = "{0:#0{1}x}".format(n, digits + 2)[2:]
#     sys.stderr.write('%s\n'%s)

#     ans += 2
#     for c in list(s):
#         if c in ['0', '6', '9', 'a', 'e']:
#            ans += 6
#         elif c == '1':
#            ans += 2
#         elif c in ['4', 'f']:
#            ans += 4
#         elif c in ['7', 'c']:
#            ans += 3
#         elif c == '8':
#            ans += 7
#         elif c in ['2', '3', '5', 'b', 'd']:
#            ans += 5
#     # sys.stderr.write('%d\n' % ans)

print(ans %  1000000007)