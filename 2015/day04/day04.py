import hashlib



def ex(data, zeros):
    i = 0
    while hashlib.md5(("%s%d" % (data, i)).encode()).hexdigest()[0:zeros] != "0" * zeros:
        i += 1
    return i

def ex1(data):
    return ex(data, 5)

def ex2(data):
    return ex(data, 6)

data = "bgvyzdsv"
assert ex1("abcdef") == 609043
assert ex1("pqrstuv") == 1048970

print("ex1 : %s" % ex1(data))

print("ex2 : %s" % ex2(data))