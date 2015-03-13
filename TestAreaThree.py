# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:03:33 2015

@author: Justin
"""

import Carcassonne as carc
import pandas as pnd
import numpy as np


board = pnd.DataFrame({'TILE_ID':'0','TILE_X':0,'TILE_Y':0,'TILE_CONFIG':'CRFR','PLAYER_ID':'START','MEEPLE':'0'}, index=[0])
board = board.append({'TILE_ID':'49','TILE_X':0,'TILE_Y':1,'TILE_CONFIG':'RCCC','PLAYER_ID':'p1','MEEPLE':'CB'}, ignore_index=True)
board = board.append({'TILE_ID':'54','TILE_X':1,'TILE_Y':0,'TILE_CONFIG':'FRFR','PLAYER_ID':'p2','MEEPLE':'RL'}, ignore_index=True)
board = board.append({'TILE_ID':'33','TILE_X':1,'TILE_Y':1,'TILE_CONFIG':'CFFC','PLAYER_ID':'p3','MEEPLE':'false'}, ignore_index=True)
print(board)

config = np.array([[0,0,'C','R','F','R'],[0,1,'R','C','C','C'],[1,0,'F','R','F','R'],[1,1,'C','F','F','C']])
print(config)

