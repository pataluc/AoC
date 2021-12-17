from yachalk import chalk

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

max_steps = 500

def cprint(steps, target):
    print("_" * (target['max_x'] + 2))
    y_coords = list(map(lambda x: x[1], steps))
    
    m = [[]] * (max(y_coords) - target['min_y'] + 1)
    for i in range(len(m)):
        m[i] = ['.'] * (target['max_x'] + 2)

    m[max(y_coords)][0] = 'S'

    for i in range(target['min_x'], target['max_x']):
        for j in range(target['min_y'], target['max_y']  + 1):
            m[max(y_coords) - j][i] = 'T'
    for step in steps:
        m[max(y_coords) - step[1]][step[0]] = chalk.red('X')
    print("\n".join(map(lambda x: "".join(x), m)))

def steps(v_x, v_y, target, max_y):
    x, y = 0, 0
    #steps = []
    better = False

    for step in range(1, max_steps):
        #print("# step %d" % step)
        x += max(0, v_x - (step - 1))
        y += v_y - (step - 1)
        #steps.append((x,y))
        #print(x, y)
        
        if y > max_y:
            max_y = y
            better = True
        if better and on_target((x, y), target):
            #cprint(steps, target)
            return max_y
    return 0

def steps2(v_x, v_y, target):
    x, y = 0, 0

    for step in range(1, max_steps):
        #print("# step %d" % step)
        x += max(0, v_x - (step - 1))
        y += v_y - (step - 1)
        #print(x, y)
        
        if on_target((x, y), target):
            #cprint(steps, target)
            #print("## %d, %d" % (v_x, v_y))
            return 1
    return 0

def ex1(target):
    max_y = 0
    for v_x in range(target['max_x'] + 1):
        for v_y in range(target['min_y'], abs(target['min_y'])):
            r = steps(v_x, v_y, target, max_y)
            if r and r > max_y:
                max_y = r
    #print(max_y)
    return max_y

def ex1_o1(target):
    return (abs(target['min_y'])-1)*(abs(target['min_y']))/2
            
def ex2(target):
    soluces = 0
    for v_x in range(target['max_x'] + 1):
        for v_y in range(target['min_y'], abs(target['min_y'])):
            soluces += steps2(v_x, v_y, target)
    #print(soluces)
    return soluces


assert ex1_o1(sample) == 45
print("ex1 : %d" % ex1_o1(input))

assert ex2(sample) == 112
print("ex2 : %d" % ex2(input))
