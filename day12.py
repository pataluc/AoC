import sys
import numpy as np

lines = open("%s_input.txt" % sys.argv[0].split('.')[0], "r")
instructions = []
for line in lines:
    instructions.append(line)

directions = {'N': np.array([0, 1]),
              'E': np.array([1, 0]),
              'S': np.array([0, -1]),
              'W': np.array([-1, 0])}

def move(position, vector, value):
    return position + value * vector

def turn(facing, degrees):
    return list(directions.keys())[(list(directions.keys()).index(facing) + int(degrees / 90)) % 4]

def rotate_waypoint(waypoint, degrees):
    if (abs(degrees) == 180):
        return -waypoint
    elif degrees in [90, -270]:
        return np.array([waypoint[1], -waypoint[0]])
    elif degrees in [-90, 270]:
        return np.array([-waypoint[1], waypoint[0]])

def process_instruction(position, action, value):
    if action in directions.keys():
        position['coordinates'] = move(position['coordinates'], directions[action], value)
    elif action == 'F':
        position['coordinates'] = move(position['coordinates'], directions[position['facing']], value)
    elif action in ['R', 'L']:
        position['facing'] = turn(position['facing'], value if action == 'R' else -value)
    return position

def process_instruction2(position, waypoint, action, value):
    if action in directions.keys():
        waypoint = move(waypoint, directions[action], value)
    elif action == 'F':
        position = move(position, waypoint, value)
    elif action in ['R', 'L']:
        waypoint = rotate_waypoint(waypoint, value if action == 'R' else -value)
    return position, waypoint

#ex 1:
position = {'coordinates': np.array([0, 0]), 'facing': 'E'}
for instruction in instructions:
    position = process_instruction(position, instruction[0], int(instruction[1:]))
print("ex1: %d" % (abs(position['coordinates'][0]) + abs(position['coordinates'][1])))

#ex 2:
position = np.array([0, 0])
waypoint = np.array([10, 1])
for instruction in instructions:
    position, waypoint = process_instruction2(position, waypoint, instruction[0], int(instruction[1:]))
print("ex2: %d" % (abs(position[0]) + abs(position[1])))