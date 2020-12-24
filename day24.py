import sys
import re
import operator
import numpy as np

#lines = open("%s_sample.txt" % sys.argv[0].split('.')[0], "r").readlines()
lines = open("%s_input.txt" % sys.argv[0].split('.')[0], "r").readlines()
directions = {
    "e": [1, 0],
    "w": [-1, 0],
    "ne": [1, 1],
    "nw": [0, 1],
    "se": [0, -1],
    "sw": [-1, -1]
}

# Ex 1
black_tiles = set()
for line in lines:
    p = tuple(sum(np.array(list(map(lambda x: directions[x], re.findall(r"([ns]{0,1}[ew])", line))))))
    if p in black_tiles:
        black_tiles.remove(p)
    else:
        black_tiles.add(p)

print("Ex 1 : %d" % len(black_tiles))

# Ex 2
def get_neighbours(tile):
    x, y = tile
    return [(x-1, y), (x-1, y-1), (x, y-1), (x+1, y), (x+1, y+1), (x, y+1)]

def get_black_neighbours(tile, black_tiles):
    return set(get_neighbours(tile)) & set(black_tiles)

def daily_flip(black_tiles):
    new_tiles = set()
    black_and_neigbours = set()
    for tile in black_tiles:
        black_and_neigbours.add(tile)
        black_and_neigbours.update(get_neighbours(tile))
    
    for tile in black_and_neigbours:
        tile_neighbours = get_neighbours(tile)
        if ((tile in black_tiles and len(get_black_neighbours(tile, black_tiles)) in [1, 2])
            or (tile not in black_tiles and len(get_black_neighbours(tile, black_tiles)) == 2)):
            new_tiles.add(tile)

    return new_tiles

i = 0
print("Day %d : %d" % (i, len(black_tiles)))
while i < 100:
    i += 1

    black_tiles = daily_flip(black_tiles)
    print("Day %d : %d" % (i, len(black_tiles)))