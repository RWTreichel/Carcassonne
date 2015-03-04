"""
Carcassonne Game

@author: Justin Divens
"""

import numpy as np
import pandas as pnd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Setup board
def SetupBoard():
    board = pnd.DataFrame(columns=['TILE_ID','TILE_X','TILE_Y','TILE_CONFIG'])
    return(board)
    

#Import tile setup from csv. Create dataframe with fresh status.
def SetupTiles():
    tiles = pnd.read_csv('tiles_start.csv',header=0) #import csv starter file
    tiles.index.name = 'TILE_ID' #define index of dataframe
    tiles.insert(3,'STATUS',1) #insert status column in tiles dataframe
    return(tiles)


#Choose random tile from pile and update status column for chosen tile
def GetTile(tiles):
    tiles_current = tiles[tiles['STATUS']==1] #grab tiles with status=1
    tile_inhand = np.random.choice(tiles_current.index) #choose random tile
    status = np.array(tiles['STATUS']) #create status array from tiles
    status[tile_inhand] = 0 #set status=0 for randomly chosen tile
    tiles['STATUS'] = status #update status column of tiles dataframe   
    path = 'C:/Users/Justin/Box Sync/Python/Carcassonne/Graphics/Tiles/' + tiles['FILENAME'][tile_inhand] #define image path for chosen tile
    img = mpimg.imread(path) #define image object
    #imgplot = plt.imshow(img) #show image
    #print(tiles.values[tile_inhand])
    return(tiles, tile_inhand)
    

#Update Board
def PlaceTile(tiles, tile_inhand, board, tile_x, tile_y, tile_config):
    placement = np.array([tile_inhand, tile_x, tile_y, tile_config]) 
    placement_df = pnd.DataFrame(placement, columns=['TILE_ID','TILE_X','TILE_Y','TILE_CONFIG'])
    print(placement_df)
    board = pnd.concat(placement_df, board)
    print(board)

    
   
PlaceTile(GetTile(SetupTiles())[0],GetTile(SetupTiles())[1],SetupBoard(),2,3,'CCRF')