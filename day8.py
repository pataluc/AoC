import sys, re
f = open("%s_input.txt" % sys.argv[0].split('.')[0], "r")


stack = []

for line in f:
    instruction = dict()
    op, arg = line.rstrip().split(" ")

    instruction['op'] = op
    instruction['arg'] = int(arg)
    instruction['has_run'] = False

    stack.append(instruction)



def process(stack):
    accumulator = 0

    current_op = 0

    while current_op < len(stack) and not stack[current_op]['has_run']:
        #print('____')
        #print('current op: %d, accumulator: %d' % (current_op, accumulator), stack[current_op])

        stack[current_op]['has_run'] = True

        if stack[current_op]['op'] == 'jmp':
            current_op += stack[current_op]['arg']
        elif stack[current_op]['op'] == 'acc':
            accumulator += stack[current_op]['arg']
            current_op += 1
        else:
            current_op += 1

    print("current_op: %d, len(stack): %d" % (current_op, len(stack)))
    return accumulator, current_op >= len(stack)
    
# ex1 
#print(process(stack))


#ex 2

def reset_run_status(stack):
    for cmd in stack:
        cmd['has_run'] = False

for cmd in stack:
    if cmd['op'] in ['noop', 'jmp']:
        cmd['op'] = 'jmp' if cmd['op'] == 'noop' else 'noop'

        acc, has_terminated = process(stack)
        reset_run_status(stack)
        if has_terminated:
            print(acc)
            exit()
        else:
            cmd['op'] = 'jmp' if cmd['op'] == 'noop' else 'noop'




