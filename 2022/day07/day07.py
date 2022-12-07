import re
from os import path
from sys import argv

def file_path(file):
    return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

def du(d, fs):
    return sum(map(lambda x: int(x.split(" ")[1]), [f for f in fs if d in f and f[-1] != "/"]))

def parse_fs(data):
    fs = []
    cwd = '/'
    dirs = ['/']
    for c in data:
        command = c.split("\n")[0]
        results = c.split("\n")[1:]
        if command == 'ls':
            for r in results:
                if "dir " in r:
                    fs.append("%s%s/" % (cwd, r.replace("dir ", "")))
                    dirs.append("%s%s/" % (cwd, r.replace("dir ", "")))
                else:
                    s, f = r.split(" ")
                    fs.append("%s%s %s" % (cwd, f, s))
        elif command == "cd ..":
            cwd = "/".join(cwd.split("/")[:-2]) + "/"
        elif command == "cd /":
            cwd = "/"
        elif "cd " in command:
            cwd = "%s%s/" % (cwd, command.replace("cd ", ""))
    
    return list(map(lambda d: du(d, fs), dirs))

def load(file):
    commands = open(file_path(file), "r").read().split("\n$ ")
    return parse_fs(commands[1:])

def ex1(dirsizes):
    return sum([size for size in dirsizes if size <= 100000])

def ex2(dirsizes):
    dirsizes.sort()
    target = 30000000 - (70000000 - dirsizes[-1])
    return [size for size in dirsizes if size > target][0]

sample_dirs = load("sample.txt")
assert ex1(sample_dirs) == 95437

dirs = load("input.txt")
print("ex1 : %s" % ex1(dirs))

assert ex2(sample_dirs) == 24933642
print("ex2 : %s" % ex2(dirs))