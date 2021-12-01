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

def move(cups, max, current_cup):
    removed = (cups[current_cup], cups[cups[current_cup]], cups[cups[cups[current_cup]]])

    destination = ((current_cup - 2) % max) + 1
    while destination in removed:
        destination = ((destination - 2) % max) + 1
    
    cups[current_cup] = cups[removed[2]]
    cups[removed[2]] = cups[destination]
    cups[destination] = removed[0]
    
    return cups, cups[current_cup]

def ex1(input):
    cups = init_cups(list(map(int, list(input))))
    current_cup = int(input[0])

    i = 0
    while i < 100:
        i += 1
        cups, current_cup = move(cups, 9, current_cup)
    return print_cups(cups, 1)[1:]

def ex2(input):
    cups = init_cups(list(map(int, list(input))) + list(range(10, 1_000_001)))
    current_cup = int(input[0])

    i = 0
    while i < 10_000_000:
        i += 1
        cups, current_cup = move(cups, 1_000_000, current_cup)
    return cups[1] * cups[cups[1]]

print("Ex1: %s" % ex1("538914762"))
print("Ex2: %s" % ex2("538914762"))