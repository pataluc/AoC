def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().split(',') for line in file.readlines()]

def get_wire_path(directions):
    x, y = 0, 0
    path = set()
    for direction in directions:
        dir = direction[0]
        length = int(direction[1:])
        for _ in range(length):
            if dir == 'R':
                x += 1
            elif dir == 'L':
                x -= 1
            elif dir == 'U':
                y += 1
            elif dir == 'D':
                y -= 1
            path.add((x, y))
    return path

def manhattan_distance(point):
    return abs(point[0]) + abs(point[1])

def find_closest_intersection(wire1, wire2):
    intersections = wire1 & wire2
    return min(manhattan_distance(intersection) for intersection in intersections)

if __name__ == "__main__":
    wires = read_input('input.txt')
    wire1_path = get_wire_path(wires[0])
    wire2_path = get_wire_path(wires[1])
    closest_distance = find_closest_intersection(wire1_path, wire2_path)
    print(f"The Manhattan distance from the central port to the closest intersection is {closest_distance}")

# Assertions with examples
assert find_closest_intersection(get_wire_path("R75,D30,R83,U83,L12,D49,R71,U7,L72".split(',')),
                                 get_wire_path("U62,R66,U55,R34,D71,R55,D58,R83".split(','))) == 159
assert find_closest_intersection(get_wire_path("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(',')),
                                 get_wire_path("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(','))) == 135