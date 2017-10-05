#Astro Ohnuma
#10/5/17
#dotdemo.py - making some dots

from ggame import *

red = Color(0xFF0000,1)

dot = CircleAsset(20,LineStyle(1,red),red)

Sprite(dot)
App().run()

