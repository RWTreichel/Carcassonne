"""
Carcassonne Game

@author: Justin Divens
"""

import numpy as np
import pandas as pnd

#Setup game
def StartGame():
    #Setup Board
    start_append = pnd.DataFrame({'TILE_ID':'0','TILE_X':'0','TILE_Y':'0','TILE_CONFIG':'CRFR','PLAYER_ID':'START''MEEPLE':'0'}, index=[0])
    board = pnd.DataFrame(columns=['TILE_ID','TILE_X','TILE_Y','TILE_CONFIG','PLAYER_ID','MEEPLE'])
    board = board.append(start_append, ignore_index=True) #starting tile
    #Setup Tiles    
    tiles = pnd.read_csv('tiles_start.csv',header=0) #import csv starter file
    tiles.insert(3,'STATUS',1) #insert status column in tiles dataframe
    status = np.array(tiles['STATUS']) #create status array from tiles
    status[0] = 0 #set status=0 for starting tile
    tiles['STATUS'] = status #update status column of tiles dataframe
    return(board, tiles)

#Choose random tile from pile and update status column for chosen tile
def GetTile(tiles):
    tiles_current = tiles[tiles['STATUS']==1] #grab tiles with status=1
    tile_inhand = np.random.choice(tiles_current.index) #choose random tile
    status = np.array(tiles['STATUS']) #create status array from tiles
    status[tile_inhand] = 0 #set status=0 for randomly chosen tile
    tiles['STATUS'] = status #update status column of tiles dataframe   
    return(tiles, tile_inhand)
    
#Update Board
def PlaceTile(tiles, tile_inhand, board, tile_x, tile_y, rotate, player, meeple):
    #Create dataframe object of current placement to be appended to board
    placement = pnd.DataFrame(columns=['TILE_ID','TILE_X','TILE_Y','TILE_CONFIG','PLAYER_ID','MEEPLE'], index=[0])
    placement['TILE_ID'] = tile_inhand
    placement['TILE_X'] = tile_x
    placement['TILE_Y'] = tile_y
    
    if rotate == '0':
        new_config = tiles['TILE_CONFIG'][tile_inhand]
        placement['TILE_CONFIG'] = new_config
    elif rotate == '90':
        new_config = tiles['TILE_CONFIG'][tile_inhand][3] + tiles['TILE_CONFIG'][tile_inhand][0] + tiles['TILE_CONFIG'][tile_inhand][1] + tiles['TILE_CONFIG'][tile_inhand][2]
        placement['TILE_CONFIG'] = new_config
    elif rotate == '180':
        new_config = tiles['TILE_CONFIG'][tile_inhand][2] + tiles['TILE_CONFIG'][tile_inhand][3] + tiles['TILE_CONFIG'][tile_inhand][0] + tiles['TILE_CONFIG'][tile_inhand][1]
        placement['TILE_CONFIG'] = new_config
    elif rotate == '270':
        new_config = tiles['TILE_CONFIG'][tile_inhand][1] + tiles['TILE_CONFIG'][tile_inhand][2] + tiles['TILE_CONFIG'][tile_inhand][3] + tiles['TILE_CONFIG'][tile_inhand][0]
        placement['TILE_CONFIG'] = new_config
    else: 
        print('Invalid Rotate')
        
    placement['PLAYER_ID'] = player
    placement['MEEPLE'] = meeple
    
    #Check placement for invalid moves
    check_center = board[(board['TILE_X']==tile_x) & (board['TILE_Y']==tile_y)]
    check_top = board[(board['TILE_X']==tile_x) & (board['TILE_Y']==tile_y+1)]
    check_right = board[(board['TILE_X']==tile_x+1) & (board['TILE_Y']==tile_y)]
    check_bottom = board[(board['TILE_X']==tile_x) & (board['TILE_Y']==tile_y-1)]
    check_left = board[(board['TILE_X']==tile_x-1) & (board['TILE_Y']==tile_y)]
    
    if check_center.empty:
        if (str(check_top['TILE_CONFIG'])[2]==new_config[0] or check_top.empty) and \
        (str(check_right['TILE_CONFIG'])[3]==new_config[1] or check_right.empty) and \
        (str(check_bottom['TILE_CONFIG'])[0]==new_config[2] or check_bottom.empty) and \
        (str(check_left['TILE_CONFIG'])[1]==new_config[3] or check_left.empty):
        
            board = board.append(placement, ignore_index=True)
            return(board)
        else:
            print('Tile features do not line up')
            return(board)
    else:
        print('Invalid Move')
        return(board)

