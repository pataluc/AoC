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


seamonster = [
[False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False],
[True, False, False, False, False, True, True, False, False, False, False, True, True, False, False, False, False, True, True, True],
[False, True, False, False, True, False, False, True, False, False, True, False, False, True, False, False, True, False, False, False]
]

def get_edges(tile):
    return [tile[0],
            "".join([line[-1] for line in tile]),
            tile[-1],
            "".join([line[0] for line in tile])]

def get_borders(tiles, tile_ids = []):
    borders = []
    for tile_id, tile in tiles.items():
        if len(tile_ids) and tile_id not in tile_ids:
            continue

        possible_borders = get_edges(tile)

def get_external_tiles(tiles):
    borders = get_borders(tiles)

    external_tiles = list()
    for tile_id, tile in tiles.items():
        nb_unique_border = 0
        for border, border_tiles in borders:
            if tile_id i border_tiles and len(border_tiles) == 1:
                nb_unique_border += 1
        if nb_unique_border != 0:
            external_tiles[tile_id] =


def arrangeTiles(tiles):
    work_tiles = tiles.copy()
    stack = list()
    while True:
        externalTiles = get_external_tiles(work_tiles)
        nb_work_tiles = len(work_tiles)

    return puzzle



puzzle = arrangeTiles(tiles)


