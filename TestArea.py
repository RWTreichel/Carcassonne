"""
Testing area for Carcassonne.py
"""
import Carcassonne as carc
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#First turn simulation
b1 = carc.StartGame()

g1 = carc.GetTile(b1[1])
p1 = carc.PlaceTile(g1[0],g1[1],b1[0],int(input('Enter X location: ')),int(input('Enter Y location: ')),input('Enter Rotate (0, 90, 180, or 270): '),1)
#Second turn
g2 = carc.GetTile(g1[0])
p2 = carc.PlaceTile(g2[0],g2[1],p1,int(input('Enter X location: ')),int(input('Enter Y location: ')),input('Enter Rotate (0, 90, 180, or 270): '),2)  
#Third turn
g3 = carc.GetTile(g2[0])
p3 = carc.PlaceTile(g3[0],g3[1],p2,int(input('Enter X location: ')),int(input('Enter Y location: ')),input('Enter Rotate (0, 90, 180, or 270): '),3)
#Fourth turn
g4 = carc.GetTile(g3[0])
p4 = carc.PlaceTile(g4[0],g4[1],p3,int(input('Enter X location: ')),int(input('Enter Y location: ')),input('Enter Rotate (0, 90, 180, or 270): '),4)
#Fifth turn
g5 = carc.GetTile(g4[0])
p5 = carc.PlaceTile(g5[0],g5[1],p4,int(input('Enter X location: ')),int(input('Enter Y location: ')),input('Enter Rotate (0, 90, 180, or 270): '),1)
#Sixth turn
g6 = carc.GetTile(g5[0])
p6 = carc.PlaceTile(g6[0],g6[1],p5,int(input('Enter X location: ')),int(input('Enter Y location: ')),input('Enter Rotate (0, 90, 180, or 270): '),2)

"""

plt.scatter(p6['TILE_X'],p6['TILE_Y'])


fig1 = plt.figure(1)
plt.scatter(p6['TILE_X'],p6['TILE_Y'])

fig2 = plt.figure(2)

plt.subplot(5,5,13)
plt.axis('off')
path1 = 'C:/Users/Justin/Box Sync/Python/Carcassonne/Graphics/Tiles/' + p1['FILENAME'][g1[1]] #define image path for chosen tile
img1 = mpimg.imread(path1) #define image object
imgplot = plt.imshow(img1) #show image
imgplot.axes.get_xaxis().set_visible(False)
imgplot.axes.get_yaxis().set_visible(False)

plt.subplot(5,5,14)
plt.axis('off')
path2 = 'C:/Users/Justin/Box Sync/Python/Carcassonne/Graphics/Tiles/' + p2['FILENAME'][g2[1]] #define image path for chosen tile
img2 = mpimg.imread(path2) #define image object
imgplot = plt.imshow(img2) #show image
imgplot.axes.get_xaxis().set_visible(False)
imgplot.axes.get_yaxis().set_visible(False)

plt.subplot(5,5,9)
plt.axis('off')
path3 = 'C:/Users/Justin/Box Sync/Python/Carcassonne/Graphics/Tiles/' + p3['FILENAME'][g3[1]] #define image path for chosen tile
img3 = mpimg.imread(path3) #define image object
imgplot = plt.imshow(img3) #show image
imgplot.axes.get_xaxis().set_visible(False)
imgplot.axes.get_yaxis().set_visible(False)

#plt.savefig('board.png', bbox_inches='tight')
"""