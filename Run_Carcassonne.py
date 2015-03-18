"""
Carcassonne Game
Version 2 - Object oriented
Front End

@author: Justin Divens
"""

import Carcassonne as carc

#Initiate game
#-------------------------------------------------
tile_pile = carc.StartGame()[0]
board = carc.StartGame()[1]

#First turn
#-------------------------------------------------
tile_inhand = carc.GetTile(tile_pile)[0]
tile_pile = carc.GetTile(tile_pile)[1]
print(tile_inhand.id, tile_inhand.type, tile_inhand.config)

place_x = int(input('Enter X position: '))
place_y = int(input('Enter Y position: '))
rotate_choice = input('Choose rotation angle: ')
player_id = input('Enter player id: ')

board2 = carc.PlaceTile(tile_inhand, board, place_x, place_y, rotate_choice, player_id)

print(board2)