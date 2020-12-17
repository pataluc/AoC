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
    n = []
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            for z_offset in range(-1, 2):
                n.append((x + x_offset, y + y_offset, z + z_offset))
    return n

def neighbours4(x, y, z, w):
    n = []
    for x_offset in range(-1, 2):
        for y_offset in range(-1, 2):
            for z_offset in range(-1, 2):
                for w_offset in range(-1, 2):
                    n.append((x + x_offset, y + y_offset, z + z_offset, w + w_offset))
    return n

# 6 tours
for i in range(6):
    print("# Tour %d" % i)
    print("3d: %d, 4d: %d" % (len(actives), len(actives4)))

    new_actives = []

    for active_cell in actives:
        #print("active_cell: ", active_cell)
        for cell in neighbours(*active_cell):        
            #print("cell: ", cell)
            nb_active_neighours = len(list(set(actives) & set(neighbours(*cell))))
            if (cell not in new_actives
                and ((cell in actives and 3 <= nb_active_neighours <= 4)
                or (cell not in actives and nb_active_neighours == 3))):

                new_actives.append(cell)            
    actives = new_actives

    new_actives4 = []
    for active_cell in actives4:
        #print("active_cell: ", active_cell)
        for cell in neighbours4(*active_cell):        
            #print("cell: ", cell)
            nb_active_neighours = len(list(set(actives4) & set(neighbours4(*cell))))
            if (cell not in new_actives4
                and ((cell in actives4 and 3 <= nb_active_neighours <= 4)
                or (cell not in actives4 and nb_active_neighours == 3))):

                new_actives4.append(cell)
    actives4 = new_actives4

print("ex1: %s" % len(actives))
print("ex2: %s" % len(actives4))


