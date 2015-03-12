"""
Carcassonne Game
Python Back-end

@author: Justin Divens
"""

import numpy as np
import pandas as pnd

# ----------------------------------------------------------------------        
#   Initial game setup. Creates board object and tile object
# ---------------------------------------------------------------------- 
def StartGame():
    #Setup Board
    start_append = pnd.DataFrame({'TILE_ID':'0','TILE_X':0,'TILE_Y':0,'TILE_CONFIG':'CRFR','PLAYER_ID':'START','MEEPLE':'0'}, index=[0])
    board = pnd.DataFrame(columns=['TILE_ID','TILE_X','TILE_Y','TILE_CONFIG','PLAYER_ID','MEEPLE'])
    board = board.append(start_append, ignore_index=True) #add starting tile
    #Setup Tiles    
    tiles = pnd.read_csv('tiles_start.csv',header=0) #import csv starter file
    tiles.insert(3,'STATUS',1) #insert status column in tiles dataframe
    status = np.array(tiles['STATUS']) #create status array from tiles
    status[0] = 0 #set status=0 for starting tile
    tiles['STATUS'] = status #update status column of tiles dataframe
    return(board, tiles)

# ----------------------------------------------------------------------        
#   Choose random tile from pile and mark tile as used
# ---------------------------------------------------------------------- 
def GetTile(tiles):
    tiles_current = tiles.query('STATUS == 1') #grab tiles with status=1
    #tiles_current = tiles[tiles['STATUS']==1] #grab tiles with status=1
    tile_inhand = np.random.choice(tiles_current.index) #choose random tile
    status = np.array(tiles['STATUS']) #create status array from tiles
    status[tile_inhand] = 0 #set status=0 for randomly chosen tile
    tiles['STATUS'] = status #update status column of tiles dataframe   
    return(tiles, tile_inhand)
    
# ----------------------------------------------------------------------        
#   Update game with player's turn choices
# ----------------------------------------------------------------------     
def PlaceTile(tiles, tile_inhand, board, tileX, tileY, rotate, player, meeple):
    #Create dataframe object of current placement to be appended to board
    placement = pnd.DataFrame(columns=['TILE_ID','TILE_X','TILE_Y','TILE_CONFIG','PLAYER_ID','MEEPLE'], index=[0])
    placement['TILE_ID'] = tile_inhand
    placement['TILE_X'] = tileX
    placement['TILE_Y'] = tileY
    placement['PLAYER_ID'] = player
    placement['MEEPLE'] = meeple
    #Rotate tile algorithm
    if rotate == '0':
        new_config = tiles['TILE_CONFIG'][tile_inhand]
        placement['TILE_CONFIG'] = new_config
    elif rotate == '90':
        new_config = tiles['TILE_CONFIG'][tile_inhand][3] + tiles['TILE_CONFIG'][tile_inhand][0] +\
        tiles['TILE_CONFIG'][tile_inhand][1] + tiles['TILE_CONFIG'][tile_inhand][2]
        placement['TILE_CONFIG'] = new_config
    elif rotate == '180':
        new_config = tiles['TILE_CONFIG'][tile_inhand][2] + tiles['TILE_CONFIG'][tile_inhand][3] + \
        tiles['TILE_CONFIG'][tile_inhand][0] + tiles['TILE_CONFIG'][tile_inhand][1]
        placement['TILE_CONFIG'] = new_config
    elif rotate == '270':
        new_config = tiles['TILE_CONFIG'][tile_inhand][1] + tiles['TILE_CONFIG'][tile_inhand][2] + \
        tiles['TILE_CONFIG'][tile_inhand][3] + tiles['TILE_CONFIG'][tile_inhand][0]
        placement['TILE_CONFIG'] = new_config
    else: 
        error_msg = 'Invalid rotate'
        return(error_msg)
    #Check placement for invalid moves
    tileX = float(tileX)
    tileY = float(tileY)
    check_center = board.query('TILE_X == @tileX & TILE_Y == @tileY')
    check_top = board.query('TILE_X == @tileX & TILE_Y == (@tileY+1)')
    check_right = board.query('TILE_X == (@tileX+1) & TILE_Y == @tileY')
    check_bottom = board.query('TILE_X == @tileX & TILE_Y == (@tileY-1)')
    check_left = board.query('TILE_X == (@tileX-1) & TILE_Y == @tileY')
    #Update board if all checks pass
    if check_center.empty: #check if spot is already taken
        if (check_top.empty and check_right.empty and check_bottom.empty and check_left.empty): #check if next to existing tile
            error_msg = 'Not next to existing tile'
            return(error_msg, board)
        else:
            if (check_top.empty or str(check_top['TILE_CONFIG'])[7]==new_config[0]) & \
            (check_right.empty or str(check_right['TILE_CONFIG'])[8]==new_config[1]) & \
            (check_bottom.empty or str(check_bottom['TILE_CONFIG'])[5]==new_config[2]) & \
            (check_left.empty or str(check_left['TILE_CONFIG'])[6]==new_config[3]):        
                board = board.append(placement)
                return(board)
            else:
                error_msg = 'Tile features do not line up'
                return(error_msg, board)
    else:
        error_msg = 'Spot already taken'
        return(error_msg, board)

