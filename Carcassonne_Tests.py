"""
Carcassonne Game
Version 2 - Object oriented
TESTS

@author: Justin Divens
"""

import string
import random
import pandas as pnd
import numpy as np
import Carcassonne as carc

# ----------------------------------------------------------------------        
#   Test 1 - Check Tile object creation
# ---------------------------------------------------------------------- 
def Test1():
    test1=[]
    print('Starting... Test 1 - Check Tile object creation')
    #create random test tile object
    rand_id = random.choice(range(72))
    rand_type = random.choice(string.ascii_uppercase)
    configs = ['CCC','FFF','FRF']
    rand_config = ''.join(random.choice(configs) for x in range(4))
    rand_filename = random.choice(string.ascii_uppercase)+'.png'
    test_tile = carc.Tile(rand_id, rand_type, rand_config, rand_filename)
    
    #check if object type = Tile    
    test1.append([type(test_tile) == carc.Tile])
    #check tile object attributes for type, length, and value
    test1.append([type(test_tile.id) is int])
    test1.append([test_tile.id == rand_id])
    
    test1.append([type(test_tile.type) is str])
    test1.append([test_tile.type == rand_type])
    
    test1.append([type(test_tile.config) is str])
    test1.append([len(test_tile.config)==12])
    test1.append([test_tile.config == rand_config])
    
    test1.append([type(test_tile.filename) is str])
    test1.append([test_tile.filename == rand_filename])
    
    test1.append([type(test_tile.status) is int])
    
    print(str(len(test1)) + ' tests completed')
    if all(test1):
        print('All tests pass')
    else:
        errs = len([elem for elem in test1 if elem==False])
        print(str(errs) + ' tests failed')
        print(test1)
    
# ----------------------------------------------------------------------        
#   Test 2 - Check Tile Rotate function
# ---------------------------------------------------------------------- 
def Test2():
    test2 = []
    print('-------------------------------------------------------------')
    print('Starting... Test 2 - Check tile rotate function')
    #create random test tile object
    rand_id = random.choice(range(72))
    rand_type = random.choice(string.ascii_uppercase)
    rand_config = 'TTTRRRBBBLLL'
    rand_filename = random.choice(string.ascii_uppercase)+'.png'
    test_tile = carc.Tile(rand_id, rand_type, rand_config, rand_filename)
    #print('original: ' + str(test_tile.config))
    
    zero = test_tile.rotate('0')
    test2.append(zero == 'TTTRRRBBBLLL')
    #print('rotate 0: ' + str(test_tile.config))
    
    test_tile = carc.Tile(rand_id, rand_type, rand_config, rand_filename)
    ninety = test_tile.rotate('90')
    test2.append(ninety == 'LLLTTTRRRBBB')
    #print('rotate 90: ' + str(test_tile.config))
    
    test_tile = carc.Tile(rand_id, rand_type, rand_config, rand_filename)
    oneeighty = test_tile.rotate('180')
    test2.append(oneeighty == 'BBBLLLTTTRRR')
    #print('rotate 180: ' + str(test_tile.config))
    
    test_tile = carc.Tile(rand_id, rand_type, rand_config, rand_filename)
    twoseventy = test_tile.rotate('270')
    test2.append(twoseventy == 'RRRBBBLLLTTT')
    #print('rotate 270: ' + str(test_tile.config))
    
    print(str(len(test2)) + ' tests completed')
    if all(test2):
        print('All tests pass')
    else:
        errs = len([elem for elem in test2 if elem==False])
        print(str(errs) + ' tests failed')
        print(test2)
    
# ----------------------------------------------------------------------        
#   Test 3 - 'Next to' placement checks
# ----------------------------------------------------------------------     
def Test3():
    test3 = []
    print('-------------------------------------------------------------')
    print('Starting... Test 3 - \'Next to\' placement checks')
    #Create tiles, place them, check for errors
    board_start = pnd.DataFrame({'TILE_ID':'0','TILE_X':0,'TILE_Y':0,'TILE_CONFIG':'CCCFRFFFFFRF','PLAYER_ID':'START','MEEPLE':'0'}, index=[0])
    
    #tile_center = pnd.DataFrame({'TILE_ID':'1','TILE_X':0,'TILE_Y':0,'TILE_CONFIG':'CCCCCCCCCCCC','PLAYER_ID':'p1','MEEPLE':'0'}, index=[0])
    tile_center = carc.Tile(1, 'test', 'CCCCCCCCCCCC', 'testfile.png')
    place_center = carc.PlaceTile(tile_center, board_start, 0, 0, '0', 'p1')
    test3.append(len(place_center[1]) != 0)    
    
    #tile_top = pnd.DataFrame({'TILE_ID':'1','TILE_X':0,'TILE_Y':1,'TILE_CONFIG':'FFFFRFCCCFRF','PLAYER_ID':'p1','MEEPLE':'0'}, index=[0])
    tile_top = carc.Tile(1, 'test', 'FFFFRFCCCFRF', 'testfile.png')
    place_top = carc.PlaceTile(tile_top, board_start, 0, 1, '0', 'p1')    
    test3.append(place_top[1] == "")
    
    #tile_right = pnd.DataFrame({'TILE_ID':'1','TILE_X':1,'TILE_Y':0,'TILE_CONFIG':'FFFFRFFFFFRF','PLAYER_ID':'p1','MEEPLE':'0'}, index=[0])
    tile_right = carc.Tile(1, 'test', 'FFFFRFFFFFRF', 'testfile.png')
    place_right = carc.PlaceTile(tile_right, board_start, 1, 0, '0', 'p1')  
    test3.append(place_right[1] == "")
    
    #tile_bottom = pnd.DataFrame({'TILE_ID':'1','TILE_X':0,'TILE_Y':-1,'TILE_CONFIG':'FFFFRFFFFFRF','PLAYER_ID':'p1','MEEPLE':'0'}, index=[0])
    tile_bottom = carc.Tile(1, 'test', 'FFFFRFFFFFRF', 'testfile.png')
    place_bottom = carc.PlaceTile(tile_bottom, board_start, 0, -1, '0', 'p1') 
    test3.append(place_bottom[1] == "")
    
    #tile_left = pnd.DataFrame({'TILE_ID':'1','TILE_X':-1,'TILE_Y':0,'TILE_CONFIG':'FFFFRFFFFFRF','PLAYER_ID':'p1','MEEPLE':'0'}, index=[0])
    tile_left = carc.Tile(1, 'test', 'FFFFRFFFFFRF', 'testfile.png')
    place_left = carc.PlaceTile(tile_left, board_start, -1, 0, '0', 'p1')
    test3.append(place_left[1] == "")
    
    print(str(len(test3)) + ' tests completed')
    if all(test3):
        print('All tests pass')
    else:
        errs = len([elem for elem in test3 if elem==False])
        print(str(errs) + ' tests failed')
        print(test3)
        
# ----------------------------------------------------------------------        
#   Test 4 - Check features line up
# ----------------------------------------------------------------------     
def Test4():
    test4 = []
    print('-------------------------------------------------------------')
    print('Starting... Test 4 - Check features line up')        
        
    # Add tests here
     
    print(str(len(test4)) + ' tests completed')
    if all(test4):
        print('All tests pass')
    else:
        errs = len([elem for elem in test4 if elem==False])
        print(str(errs) + ' tests failed')
        print(test4) 
        
        
        
        
    
Test1()
Test2()
Test3()
Test4()

