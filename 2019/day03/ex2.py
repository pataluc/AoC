def read_input(file_path):
    with open(file_path, 'r') as file:
        return [line.strip().split(',') for line in file.readlines()]

def get_wire_path_with_steps(directions):
    x, y = 0, 0
    steps = 0
    path = {}
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
            steps += 1
            if (x, y) not in path:
                path[(x, y)] = steps
    return path

def find_fewest_combined_steps(wire1, wire2):
    intersections = set(wire1.keys()) & set(wire2.keys())
    return min(wire1[intersection] + wire2[intersection] for intersection in intersections)

if __name__ == "__main__":
    wires = read_input('input.txt')
    wire1_path = get_wire_path_with_steps(wires[0])
    wire2_path = get_wire_path_with_steps(wires[1])
    fewest_steps = find_fewest_combined_steps(wire1_path, wire2_path)
    print(f"The fewest combined steps the wires must take to reach an intersection is {fewest_steps}")

# Assertions with examples
assert find_fewest_combined_steps(get_wire_path_with_steps("R75,D30,R83,U83,L12,D49,R71,U7,L72".split(',')),
                                  get_wire_path_with_steps("U62,R66,U55,R34,D71,R55,D58,R83".split(','))) == 610
assert find_fewest_combined_steps(get_wire_path_with_steps("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(',')),
                                  get_wire_path_with_steps("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(','))) == 410