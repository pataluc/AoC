import sys
import re
lines = open("%s_input.txt" % sys.argv[0].split('.')[0], "r").readlines()

tiles = dict()

i = 0
while i < len(lines):
    tile = [['']] *10
    tile_id = lines[i].replace("Tile ", "").replace(":\n", "")
    #print("tile id: %s" % tile_id)
    i += 1

    for j in range(i, i + 10):
        #print("i : %d, j: %d" %(i, j), lines[j].rstrip())
        tile[j-i] = lines[j].rstrip()
    i = j + 2    
    tiles[tile_id] = tile

def canonical(edge):
    reverse = edge[::-1]
    return edge if edge < reverse else reverse

def get_edges(tile):
    return [tile[0],
            "".join([line[-1] for line in tile]),
            tile[-1],
            "".join([line[0] for line in tile])]

def get_canonical_edges(tile):
    return list(map(canonical, get_edges(tile)))


def count_common_edges(tile1, tile2):
    count = 0
    for e1 in get_edges(tile1):
        for e2 in get_edges(tile2):
            if e1 == e2 or e1 == e2[::-1]:
                count =+ 1
    return count

puzzle = {}
for tile_id, tile in tiles.items():
    for b in get_canonical_edges(tile):
        if b[::-1] in puzzle:
            puzzle.pop(b[::-1])
        else:
            puzzle[b[::-1]] = tile_id

borders = sorted(puzzle.values())

product = 1
for i, b in enumerate(borders):
    if (i > 0 and b == borders[i-1]):
        product *= int(b)

print("ex 1: %d" % product)
