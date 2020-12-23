def move(cups, max):
    print("cups: %s" % " ".join(map(str, cups[:25])))
    removed = [cups.pop(1) for i in range(3)]
    #print("pick up: %s" % " ".join(map(str, removed)))
    
    destination = ((cups[0] - 2) % max) + 1
    while destination in removed:
        destination = ((destination - 2) % max) + 1
    print(destination)

    d_index = cups.index(destination) + 1

    #print("index: %d" % d_index)

    cups = cups[1:d_index] + removed + cups[d_index:] + cups[:1]
    return cups

def ex1():
    cups = list(map(int, list("538914762"))) #my input
    cups = list(map(int, list("389125467"))) #sample

    i = 0
    while i < 100:
        i += 1
        #print("-- move %d --" % i)
        cups = move(cups, 9)
    print("Ex 1: %s" % "".join(map(str, cups[cups.index(1)+1:] + cups[:cups.index(1)])))

def ex2():
    cups = list(map(int, list("538914762"))) + list(range(10, 1_000_001)) #my input
    cups = list(map(int, list("389125467"))) + list(range(10, 1_000_001)) #sample

    i = 0
    while i < 30:
        i += 1
        print("-- move %d --" % i)
        if i % 10_000 == 0:
            print(i)
        cups = move(cups, 1_000_000)

    print(cups[-50:])

ex2()