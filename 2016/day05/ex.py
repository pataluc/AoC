from os import path
from sys import argv
import hashlib



# def ex(data, zeros):
#     i = 0
#     while hashlib.md5(("%s%d" % (data, i)).encode()).hexdigest()[0:zeros] != "0" * zeros:

# def file_path(file):
#     return "%s/%s" % (path.dirname(argv[0]) if path.dirname(argv[0]) else ".", file)

# def load(file):
#     return open(file_path(file), "r").read().strip()

debug = False
def dprint(*s):
    if debug:
        print(*s)

def ex1(data):
    password = ''

    i = 0
    while len(password) < 8:
        hash = hashlib.md5(("%s%d" % (data, i)).encode()).hexdigest()
        if hash.startswith('00000'):
            password += hash[5]
            print(hash, password)
        i += 1
        
    return password

def ex2(data):
    password = list('        ')

    i = 0
    while ' ' in password:
        hash = hashlib.md5(("%s%d" % (data, i)).encode()).hexdigest()
        if hash.startswith('00000') and '0' <= hash[5] < '8' and password[int(hash[5])] == ' ':
            password[int(hash[5])] = hash[6]
            print(hash, ''.join(password))
        i += 1
        
    return ''.join(password)

# assert ex1('abc') == '18f47a30'
print("ex1 : %s" % ex1('reyedfim'))
# assert ex2('abc') == '05ace8e3'
print("ex2 : %s" % ex2('reyedfim'))