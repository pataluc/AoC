from os import path
import sys

def file_path(file):
    """Compute input file path"""
    return f'{path.dirname(sys.argv[0]) if path.dirname(sys.argv[0]) else "."}/{file}'

def load(file):
    """Load file"""
    return open(file_path(file), "r", encoding='utf-8').read().rstrip()

# Custo starts here
def load_data(data: str) -> tuple:
    """Loads data as a tuple"""
    return [list(line) for line in data.split('\n')]

def grid_print(points: set, R: int, C:int, p: str = 'X') -> None:
    for r in range(R):
        line = ''
        for c in range(C):
            if (r, c) in points:
                line += p
            else:
                line += '.'
        print(line)

def dragon_moves(reachable: set, R: int, C: int, include_past_positions = True) -> set:
    new_reachable = reachable.copy() if include_past_positions else set()
    for r, c in reachable:
        for dr, dc in [(-2,-1),(-1, -2),(1,-2),(2,-1),(1, 2), (2, 1), (-1,2),(-2,1)]:
            if 0 <= r + dr < R and 0 <= c + dc < C:
                new_reachable.add((r+dr, c+dc))
    return new_reachable

def part1(grid: list, moves: int = 4) -> int:
    # print(grid)
    R = len(grid)
    C = len(grid[0])

    dragon_reachable = {(R//2, C//2)}
    for _ in range(moves):
        dragon_reachable = dragon_moves(dragon_reachable, R, C)
        # grid_print(reachable, R, C)
    return sum(1 for r, c in dragon_reachable if grid[r][c] == 'S')


assert part1(load_data(load('sample1')), 3) == 27
print("Part 1: ", part1(load_data(load('notes1'))))

def get_positions(grid: list, R: int, C: int, searched: str) -> set:
    sheep_positions = set()
    for r in range(R):
        for c in range(C):
            if grid[r][c] == searched:
                sheep_positions.add((r, c))
    return sheep_positions

def move_sheeps(sheep_positions: set, R: int) -> set:
    new_sheep_positions = set()
    for r, c in sheep_positions:
        # if r + 1 < R:
            new_sheep_positions.add((r + 1, c))
    return new_sheep_positions

def part2(grid: list, moves: int = 20) -> int:
    R = len(grid)
    C = len(grid[0])

    dragon_reachable = {(R//2, C//2)}
    sheep_positions = get_positions(grid, R, C, 'S')
    hide_positions = get_positions(grid, R, C, '#')
    initial_sheep_numbers = len(sheep_positions)

    # grid_print(sheep_positions, R, C, 'S')
    # grid_print(hide_positions, R, C, '#')
    for _ in range(moves):
        # Dragon moves
        dragon_reachable = dragon_moves(dragon_reachable, R, C, False)
        # print("=" * C)
        # grid_print(dragon_reachable, R, C)
        # grid_print(hide_positions, R, C, '#')
        # grid_print(dragon_reachable - hide_positions, R, C, 'X')

        # Dragon eats sheep
        sheep_positions -= (dragon_reachable - hide_positions)

        # Sheeps moves
        sheep_positions = move_sheeps(sheep_positions, R)
        # Dragon eats sheep
        sheep_positions -= (dragon_reachable - hide_positions)
        # print(initial_sheep_numbers - len(sheep_positions), "sheeps eaten so far")

    return initial_sheep_numbers - len(sheep_positions)

assert part2(load_data(load('sample2')), 3) == 27
print("Part 2: ", part2(load_data(load('notes2'))))
exit()



def part3(scales: list) -> int:
    G = nx.Graph()
    result = 0
    for c in range(len(scales)):
        child = scales[c]
        for p1 in range(len(scales) - 1):
            parent1 = scales[p1]
            for p2 in range(p1, len(scales)):
                parent2 = scales[p2]
                if child != parent1 and child != parent2 and parent1 != parent2:
                    if is_child(child, parent1, parent2):
                        # print(f'{c+1} is child of {p1+1} and {p2+1}')
                        G.add_edge(c + 1, p1 + 1)
                        G.add_edge(c + 1, p2 + 1)

    fam_number = 0
    fam_value = 0
    for component in nx.connected_components(G):
        if len(component) > fam_number:
            fam_number = len(component)
            fam_value = sum(component)

    return fam_value

assert part3(load_data(load('sample3-1'))) == 12
assert part3(load_data(load('sample3-2'))) == 36
print("Part 3: ", part3(load_data(load('notes3'))))
