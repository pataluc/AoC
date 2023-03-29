#*******
#* Read input from STDIN
#* Use print to output your result to STDOUT.
#* Use sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
import numpy

def debug(s):
    sys.stderr.write("%s\n" % s)

notes = list(map(float, sys.stdin.readlines()))

notes = sorted(notes)
# debug(notes)

#min
# debug(sum(notes[0:9])/9)
print(sum(notes[0:9])/9)

#mean
# debug(sum(notes)/12)
print(sum(notes)/12)


#med
def medianne(notes):
    judges= []
    for i in range(12):
        for j in range(12):
            for k in range(12):
                if i != j and i != k and j != k:
                    judges.append( (sum(notes) - notes[i] - notes[j] - notes[k]) / 9)
    # debug(judges)
    return numpy.median(judges)
                    
    
    
# debug(medianne(notes))
print(medianne(notes))

#max
# debug(sum(notes[3:])/9)
print(sum(notes[3:])/9)
