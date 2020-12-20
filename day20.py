import sys
import re
lines = open("%s_sample.txt" % sys.argv[0].split('.')[0], "r").readlines()

tiles = dict()

i = 0
while i < len(lines):
    tile = [['']] *10
    tile_id = lines[i].replace("Tile ", "").replace(":\n", "")
    #print("tile id: %s" % tile_id)
    i += 1

    for j in range(i, i + 10):
        #print("i : %d, j: %d" %(i, j), lines[j].rstrip())
        tile[j-i] = lines[j].rstrip().split()
    i = j + 2 
    
    tiles[tile_id] = tile

print(tiles)

def adjacent(tile1, tile2):

    return False
