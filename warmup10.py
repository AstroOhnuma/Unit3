#Astro Ohnuma
#10/5/17
#warmup10.py - making wallpaper

from ggame import *

red = Color(0xFF0000,1)
tan = Color(0xFFB266,1)
blue = Color(0x0080FF,1)
black = Color(0x000000,1)

blackoutline = LineStyle(1,black)

roof = PolygonAsset([(0,60), (100,0), (200,60)], blackoutline, red)
house = RectangleAsset(180,100, blackoutline, tan)
window = RectangleAsset(40,40, blackoutline, blue)
window2 = RectangleAsset(40,40, blackoutline, blue)
door = RectangleAsset(40,60, blackoutline, red)

for j in range(15):
    for i in range(20):
        Sprite(roof)
        Sprite(house, (10+20*i,60+20*j))
        Sprite(window, (20+20*i,70+20*j))
        Sprite(window2, (140+20*i,70+20*j))
        Sprite(door, (80+20*i,100+20*j))
App().run()

