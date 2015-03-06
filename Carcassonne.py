"""
Carcassonne Game

@author: Justin Divens
"""

import numpy as np
import pandas as pnd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Setup board
def StartGame():
    board = pnd.DataFrame(columns=['TILE_ID','TILE_X','TILE_Y','TILE_CONFIG','PLAYER_ID'])
    tiles = pnd.read_csv('tiles_start.csv',header=0) #import csv starter file
    tiles.insert(3,'STATUS',1) #insert status column in tiles dataframe
    return(board, tiles)

#Choose random tile from pile and update status column for chosen tile
def GetTile(tiles):
    tiles_current = tiles[tiles['STATUS']==1] #grab tiles with status=1
    tile_inhand = np.random.choice(tiles_current.index) #choose random tile
    status = np.array(tiles['STATUS']) #create status array from tiles
    status[tile_inhand] = 0 #set status=0 for randomly chosen tile
    tiles['STATUS'] = status #update status column of tiles dataframe   
    path = 'C:/Users/Justin/Box Sync/Python/Carcassonne/Graphics/Tiles/' + tiles['FILENAME'][tile_inhand] #define image path for chosen tile
    #img = mpimg.imread(path) #define image object
    #imgplot = plt.imshow(img) #show image
    print(tiles.values[tile_inhand])
    return(tiles, tile_inhand)
    
#Update Board
def PlaceTile(tiles, tile_inhand, board, tile_x, tile_y, tile_config, player):
    placement = pnd.DataFrame(columns=['TILE_ID','TILE_X','TILE_Y','TILE_CONFIG'], index=[0])
    placement['TILE_ID'] = tile_inhand
    placement['TILE_X'] = tile_x
    placement['TILE_Y'] = tile_y
    placement['TILE_CONFIG'] = tile_config
    placement['PLAYER_ID'] = player
    board = board.append(placement, ignore_index=True)
    print(board)
    return(board, tiles)

