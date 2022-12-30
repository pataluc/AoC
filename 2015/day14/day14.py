import re
from os import path
from sys import argv
import numpy as np

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def load(file):
    return re.findall(r'(.*) can fly (\d*) km/s for (\d*) seconds, but then must rest for (\d*) seconds.', open(file_path(file), "r").read(), flags=re.M)

debug = False

def distance(speed, sprint_time, rest_time, time):
    return (time//(sprint_time + rest_time))*speed*sprint_time + min(time % (sprint_time + rest_time), sprint_time)*speed

def ex1(data):
    data = list(map(lambda x: (int(x[1]), int(x[2]), int(x[3])), data))
    return max([ distance(speed, sprint_time, rest_time, 2503) for speed, sprint_time, rest_time in data ])

def ex2(data, end_time = 2503):
    data = list(map(lambda x: (int(x[1]), int(x[2]), int(x[3])), data))

    scores = [0] * len(data)
    
    for t in range(1, end_time + 1):
        score_t = [ distance(speed, sprint_time, rest_time, t) for speed, sprint_time, rest_time in data ]
        m = max(score_t)
        scores += np.array([1 if x == m else 0 for x in score_t])

    return max(scores)

data = load("input.txt")
print("ex1 : %s" % ex1(data))

sample = load("sample.txt")
assert ex2(sample, 1000) == 689
print("ex2 : %s" % ex2(data))