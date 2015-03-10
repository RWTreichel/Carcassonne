"""
Testing area for Carcassonne.py
"""
import Carcassonne as carc
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

turn = 0
print("Turn " + str(turn))
start = carc.StartGame()
board = start[0]
tiles = start[1]
path = 'C:/Users/Justin/Box Sync/Python/Carcassonne/Graphics/Tiles/D.png' #define image path for chosen tile
#img = mpimg.imread(path) #define image object
#imgplot = plt.imshow(img) #show image
plt.axis('off')

turn = 1  
while turn < 5:
    print("Turn " + str(turn))
    pick = carc.GetTile(tiles)
    tiles = pick[0]
    tile_inhand = pick[1]
    path = 'C:/Users/Justin/Box Sync/Python/Carcassonne/Graphics/Tiles/' + tiles['FILENAME'][tile_inhand] #define image path for chosen tile   

    print(tiles[tiles.index==tile_inhand])
    rotate = input('Rotate Degrees (0, 90, 180, or 270):')
    if rotate == '0':
        new_config = tiles['TILE_CONFIG'][tile_inhand]
        print(new_config)

    elif rotate == '90':
        new_config = tiles['TILE_CONFIG'][tile_inhand][3] + tiles['TILE_CONFIG'][tile_inhand][0] + tiles['TILE_CONFIG'][tile_inhand][1] + tiles['TILE_CONFIG'][tile_inhand][2]
        print(new_config)

    elif rotate == '180':
        new_config = tiles['TILE_CONFIG'][tile_inhand][2] + tiles['TILE_CONFIG'][tile_inhand][3] + tiles['TILE_CONFIG'][tile_inhand][0] + tiles['TILE_CONFIG'][tile_inhand][1]
        print(new_config)

    elif rotate == '270':
        new_config = tiles['TILE_CONFIG'][tile_inhand][1] + tiles['TILE_CONFIG'][tile_inhand][2] + tiles['TILE_CONFIG'][tile_inhand][3] + tiles['TILE_CONFIG'][tile_inhand][0]
        print(new_config)

    else:
        print('Please Enter 0, 90, 180, or 270')
    

    turn = turn + 1

    


