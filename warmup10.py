#Astro Ohnuma
#10/5/17
#warmup10.py - making wallpaper

from ggame import *

red = Color(0xFF0000,1)

dot = CircleAsset(20,LineStyle(1,red),red)
triangle = PolygonAsset([(20,20), (30,10), (40,20)],LineStyle(1,red),red)

for j in range(15):#prints the row 10 times
    for i in range(20):#prints one row of dots
        Sprite(dot,(20 + 50*i,20 + 50*j))
Sprite(triangle)
App().run()

