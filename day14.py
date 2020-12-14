import sys

f = open("%s_input.txt" % sys.argv[0].split('.')[0], "r")
lines = []
for line in f:
    lines.append(line.rstrip().split(' = '))

def apply_mask(mask, val):
    val = format(int(val), '036b')
    return "".join([mask[i] if mask[i] != 'X' else val[i] for i in range(36)])

def apply_mask_address(mask, val):
    val = format(int(val), '036b')
    return "".join([val[i] if mask[i] == '0' else mask[i] for i in range(36)])

def gen_floating(val):
    if 'X' in val:
        return gen_floating(val.replace("X", "0", 1)) + gen_floating(val.replace("X", "1", 1))
    else:
        return [val]

# Ex 1
def ex1(lines):
    mask, mem = '', dict()

    for arg, value in lines:
        if arg == "mask":
            mask = value
        else:
            address = int(arg.replace('mem[', '').replace(']', ''))
            mem[address] = int(apply_mask(mask, value), 2)
    print("ex1: %d" % sum([val for val in mem.values()]))

# Ex 2
def ex2(lines):
    mask, mem = '', dict()

    for arg, value in lines:
        if arg == "mask":
            mask = value
        else:
            address = apply_mask_address(mask, int(arg.replace('mem[', '').replace(']', '')))
            for a in gen_floating(address):
                mem[a] = int(value)
    print("ex2: %d" % sum([val for val in mem.values()]))
    
ex1(lines)
ex2(lines)
