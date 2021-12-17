sample = {
    'min_x': 20,
    'max_x': 30,
    'min_y': -10,
    'max_y': -5
}
input = {
    'min_x': 135,
    'max_x': 155,
    'min_y': -102,
    'max_y': -78
}

def on_target(p, target):
    return target['min_x'] <= p[0] <= target['max_x'] \
        and target['min_y'] <= p[1] <= target['max_y']
def lower(p, target):
    return p[1] < target['min_y']
def farer(p, target):
    return p[0] > target['max_x']

def steps(v_x, v_y, target):
    x, y = 0, 0
    steps = []

    step = 0
    while True:
        step += 1
        x += max(0, v_x - (step - 1))
        y += v_y - (step - 1)
        steps.append((x,y))
                
        if lower((x, y), target) or farer((x, y), target):
            return 0
        elif on_target((x, y), target):
            return 1

def ex1(target):
    return (abs(target['min_y'])-1)*(abs(target['min_y']))/2
            
def ex2(target):
    soluces = 0
    for v_x in range(target['max_x'] + 1):
        for v_y in range(target['min_y'], abs(target['min_y'])):
            soluces += steps(v_x, v_y, target)
    return soluces


assert ex1(sample) == 45
print("ex1 : %d" % ex1(input))

assert ex2(sample) == 112
print("ex2 : %d" % ex2(input))
