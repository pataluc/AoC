import sys

lines = open("%s_input.txt" % sys.argv[0].split('.')[0], "r")
actives = []
actives4 = []

for x, line in enumerate(lines):
    for y, cell in enumerate((line.rstrip())):
        if cell == '#':
            actives.append((x, y, 0))
            actives4.append((x, y, 0, 0))

def neighbours(x, y, z):
    return [(x + x_offset, y + y_offset, z + z_offset)
            for x_offset in range(-1, 2)
            for y_offset in range(-1, 2)
            for z_offset in range(-1, 2)]

def neighbours4(x, y, z, w):    
    return [(x + x_offset, y + y_offset, z + z_offset, w + w_offset)
            for x_offset in range(-1, 2)
            for y_offset in range(-1, 2)
            for z_offset in range(-1, 2)
            for w_offset in range(-1, 2)]

def process(actives, neighbours_function):
    new_actives = []
    for active_cell in actives:
        for cell in neighbours_function(*active_cell):        
            nb_active_neighours = len(list(set(actives) & set(neighbours_function(*cell))))
            if (cell not in new_actives
                and ((cell in actives and 3 <= nb_active_neighours <= 4)
                or (cell not in actives and nb_active_neighours == 3))):
                new_actives.append(cell)            
    return new_actives

for i in range(6):
    print("Tour %d" % i)
    actives = process(actives, neighbours)
    actives4 = process(actives4, neighbours4)

print("ex1: %s" % len(actives))
print("ex2: %s" % len(actives4))


