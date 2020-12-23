def move(cups, max):
    #print("cups: %s" % " ".join(map(str, cups[:25])))
    removed = [cups.pop(1) for i in range(3)]
    #print("pick up: %s" % " ".join(map(str, removed)))
    
    destination = ((cups[0] - 2) % max) + 1
    while destination in removed:
        destination = ((destination - 2) % max) + 1
    #print(destination)

    d_index = cups.index(destination) + 1

    #print("index: %d" % d_index)

    cups = cups[1:d_index] + removed + cups[d_index:] + cups[:1]
    return cups

def init_cups(cups):
    result = dict()
    max = len(cups)
    for i, c in enumerate(cups):
        result[c] = cups[(i + 1) % max]
    return result

def print_cups(cups, current):
    first = current
    result = [current]
    current = cups[current]

    while first != current:
        result.append(current)
        current = cups[current]
    return "".join(map(str, result))

def move2(cups, max, current_cup):
    #print("cups: ", print_cups(cups, current_cup), cups)
    #print("current_cup: ", current_cup)
    removed = (cups[current_cup], cups[cups[current_cup]], cups[cups[cups[current_cup]]])
    #print("removed: ", removed)

    destination = ((current_cup - 2) % max) + 1
    while destination in removed:
        destination = ((destination - 2) % max) + 1
    #print("destination", destination)

    cups[current_cup] = cups[removed[2]]
    cups[removed[2]] = cups[destination]
    cups[destination] = removed[0]
    
    return cups, cups[current_cup]



def ex1(input):
    cups = list(map(int, list(input)))

    i = 0
    while i < 100:
        i += 1
        #print("-- move %d --" % i)
        cups = move(cups, 9)
    return "".join(map(str, cups[cups.index(1)+1:] + cups[:cups.index(1)]))

def ex1_bis(input):
    cups = init_cups(list(map(int, list(input))))
    current_cup = int(input[0])
    #print("cups: ", cups)
    #print("current_cup: ", current_cup)

    i = 0
    while i < 100:
        i += 1
        #print("\n-- move %d --" % i)
        cups, current_cup = move2(cups, 9, current_cup)
    #print(current_cup)
    return print_cups(cups, 1)[1:]

def ex2(input):
    cups = init_cups(list(map(int, list(input))) + list(range(10, 1_000_001)))
    current_cup = int(input[0])
    #print("cups: ", cups)
    #print("current_cup: ", current_cup)

    i = 0
    while i < 10_000_000:
        i += 1
        #print("\n-- move %d --" % i)
        cups, current_cup = move2(cups, 1_000_000, current_cup)
    print("%d %d" % (cups[1], cups[cups[1]]))
    return cups[1] * cups[cups[1]]


#print("Sample Ex1: %s" % ex1("389125467")) #sample
#print("Sample Ex1 bis: %s" % ex1_bis("389125467")) #sample

print("Sample Ex1 bis: %s" % ex1_bis("538914762")) #my input


#print("Sample Ex2: %s" % ex2("389125467")) #sample
print("Sample Ex2: %s" % ex2("538914762")) #my input