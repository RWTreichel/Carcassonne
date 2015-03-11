"""
Testing area for Carcassonne.py
"""
import Carcassonne as carc
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

#Initiate Game
start = carc.StartGame()
board = start[0]
tiles = start[1]

#Start Loop
turn = 1
while turn < 5:
    get_tile = carc.GetTile(tiles)
    tiles = get_tile[0]
    tile_inhand = get_tile[1]
    print(tiles.values[tile_inhand])
    
    place_x = int(input('Enter X position: '))
    place_y = int(input('Enter Y position: '))
    rotate = input('Enter rotation: ')
    player = input('Enter player ID: ')
    meeple = input('Enter meeple option: ')
    place = carc.PlaceTile(tiles, tile_inhand, board, place_x, place_y, rotate, player, meeple)
    board = place
    print(board)
    
    turn = turn + 1