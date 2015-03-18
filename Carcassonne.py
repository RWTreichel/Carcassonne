"""
Carcassonne Game
Version 2 - Object oriented

@author: Justin Divens
"""

import pandas as pnd
import numpy as np

# ----------------------------------------------------------------------        
#   Define Tile class
# ---------------------------------------------------------------------- 
class Tile:
    """Tile class"""
    def __init__(self, tile_id, tile_type, tile_config, tile_file):
        self.id = tile_id
        self.type = tile_type
        self.config = tile_config
        self.filename = tile_file
        self.status = 1
        
    def rotate(self, deg):
        if deg == '0':
            pass
        elif deg == '90':
            new_config = self.config[9:12] + self.config[0:3] + self.config[3:6] + self.config[6:9]
            self.config = new_config
        elif deg == '180':
            new_config = self.config[6:9] + self.config[9:12] + self.config[0:3] + self.config[3:6]
            self.config = new_config
        elif deg == '270':
            new_config = self.config[3:6] + self.config[6:9] + self.config[9:12] + self.config[0:3]
            self.config = new_config
        else:
            print('nah, can\'t rotate')
        
        return(str(self.config))

# ----------------------------------------------------------------------        
#   Initial game setup. Creates board object and tile object
# ----------------------------------------------------------------------         
def StartGame():
    #read in tile setup. May include options for expansion/edits later
    tiles_start = pnd.read_csv('tiles_start.csv',header=0)
    #create list of tile objects
    tile_pile = []  
    for row in range(len(tiles_start['TILE_TYPE'])):
        tile_pile.append(Tile(len(tile_pile),tiles_start['TILE_TYPE'][row],tiles_start['TILE_CONFIG'][row],tiles_start['TILE_FILENAME'][row]))
    #checkout start tile
    tile_pile[0].status=0        
    #create board dataframe, which will hold tile objects
    board = pnd.DataFrame({'TILE_ID':'0','TILE_X':0,'TILE_Y':0,'TILE_CONFIG':tile_pile[0].config,'PLAYER_ID':'START','MEEPLE':'0'}, index=[0])
    #want to change ^^^board creation^^^ to be an append like during normal play
    return(tile_pile, board)
    
# ----------------------------------------------------------------------        
#   Choose random tile from pile and mark tile as used
# ---------------------------------------------------------------------- 
def GetTile(tile_pile):
    #create list of available tile objects
    tiles_current = []
    for row in range(len(tile_pile)):
        if tile_pile[row].status == 1:
            tiles_current.append(tile_pile[row])
    #choose random tile
    tile_choice = np.random.choice(len(tiles_current))
    tile_inhand = tiles_current[tile_choice]
    #update tile pile
    for row in range(len(tile_pile)):
        if tile_pile[row].id == tile_choice:
            tile_pile[row].status=0
    return(tile_inhand, tile_pile)
            
# ----------------------------------------------------------------------        
#   Update game with player's turn choices
# ----------------------------------------------------------------------     
def PlaceTile(tile_inhand, board, tileX, tileY, rotation, player):
    #Check placement for invalid moves
    tileX = float(tileX)
    tileY = float(tileY)
    check_center = board.query('TILE_X == @tileX & TILE_Y == @tileY')
    check_top = board.query('TILE_X == @tileX & TILE_Y == (@tileY+1)')
    check_right = board.query('TILE_X == (@tileX+1) & TILE_Y == @tileY')
    check_bottom = board.query('TILE_X == @tileX & TILE_Y == (@tileY-1)')
    check_left = board.query('TILE_X == (@tileX-1) & TILE_Y == @tileY')
    """
    print('center: ',str(check_center['TILE_CONFIG']))
    print('top: ',str(check_top['TILE_CONFIG']))
    print('right: ',str(check_right['TILE_CONFIG']))       #For troubleshooting
    print('bottom: ',str(check_bottom['TILE_CONFIG']))
    print('left: ',str(check_left['TILE_CONFIG']))
    """
    #Check Tile
    check1 = check_center.empty #check if spot is already taken
    check2 =  not (check_top.empty and check_right.empty and check_bottom.empty and check_left.empty) #check if next to existing tile
    check3 = (check_top.empty or str(check_top['TILE_CONFIG'])[12]==tile_inhand.rotate(rotation)[1]) & \
            (check_right.empty or str(check_right['TILE_CONFIG'])[15]==tile_inhand.rotate(rotation)[4]) & \
            (check_bottom.empty or str(check_bottom['TILE_CONFIG'])[6]==tile_inhand.rotate(rotation)[7]) & \
            (check_left.empty or str(check_left['TILE_CONFIG'])[9]==tile_inhand.rotate(rotation)[10]) #Check features line up
            
    if all([check1, check2, check3]):
        placement = pnd.DataFrame({'TILE_ID':tile_inhand.id, 'TILE_X':tileX, 'TILE_Y':tileY, 'TILE_CONFIG':tile_inhand.rotate(rotation), 'PLAYER_ID':player, 'MEEPLE':0}, index=[0])  
        #print('placement \n',placement)              
        newboard = board.append(placement, ignore_index=True)
        err = ""
        return(newboard,err)
    else:
        err1 = 'Spot empty: ' + str(check1)
        err2 = 'Next to existing: ' + str(check2)
        err3 = 'Features line up: ' + str(check3)
        err = [err1, err2, err3]
        return(board, err)
        
    """if check_center.empty: #check if spot is already taken
        if (check_top.empty and check_right.empty and check_bottom.empty and check_left.empty): #check if next to existing tile
            error_msg = 'Not next to existing tile'
            #print(error_msg)
            #board = board.to_json()
            return(board, error_msg)
        else:
            if (check_top.empty or str(check_top['TILE_CONFIG'])[12]==tile_inhand.rotate(rotation)[1]) & \
            (check_right.empty or str(check_right['TILE_CONFIG'])[15]==tile_inhand.rotate(rotation)[4]) & \
            (check_bottom.empty or str(check_bottom['TILE_CONFIG'])[6]==tile_inhand.rotate(rotation)[7]) & \
            (check_left.empty or str(check_left['TILE_CONFIG'])[9]==tile_inhand.rotate(rotation)[10]):        
                placement = pnd.DataFrame()                
                board = board.append(placement, ignore_index=True)
                #print(board)                
                #board = board.to_json()
                error_msg = ''
                return(board, error_msg)
            else:
                error_msg = 'Tile features do not line up'
                #print(error_msg)
                #board = board.to_json()
                return(board, error_msg)
    else:
        error_msg = 'Spot already taken'
        #print(error_msg)
        #board = board.to_json()
        return(board, error_msg)
"""
    