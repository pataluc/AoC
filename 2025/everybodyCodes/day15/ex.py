from os import path
import sys
from collections import deque

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

# Custo starts here
def load_data(data: str) -> tuple:
    """Loads data as a tuple"""
    return data.split(',')



def part1(instructions: list) -> int:
    dir = (0, -1)
    turning_right = {
        (1, 0): (0, -1),
        (0, -1): (-1, 0),
        (-1, 0): (0, 1),
        (0, 1): (1, 0)
    }
    turning_left = {
        (1, 0): (0, 1),
        (0, 1): (-1, 0),
        (-1, 0): (0, -1),
        (0, -1): (1, 0)
    }

    points = [(0,0)]
    for instruction in instructions:
        turn, dist = instruction[0], int(instruction[1:])

        # Change direction
        dir = turning_right[dir] if turn == 'R' else turning_left[dir]

        # Move
        for _ in range(dist):
            last_point = points[-1]
            points.append((last_point[0] + dir[0], last_point[1] + dir[1]))

    min_x = min(point[0] for point in points)
    max_x = max(point[0] for point in points)
    min_y = min(point[1] for point in points)
    max_y = max(point[1] for point in points)
    grid = [['.' for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]
    for point in points:
        grid[point[1] - min_y][point[0] - min_x] = '#'

    grid[points[0][1] - min_y][points[0][0] - min_x] = 'S'
    grid[points[-1][1] - min_y][points[-1][0] - min_x] = 'E'

    for row in grid:
        print(''.join(row))


    result = 0

    return result

# assert part1(load_data(load('sample1'))) == 16
print("Part 1: ", part1(load_data(load('notes1'))))


print("Part 2: ", part1(load_data(load('notes2'))))

exit()
print("Part 3: ", part2(load_data2(load('notes3')), 202520252025))
