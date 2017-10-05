#Astro Ohnuma
#10/5/17
#dotdemo.py - making some dots

from ggame import *

red = Color(0xFF0000,1)

dot = CircleAsset(20,LineStyle(1,red),red)

for j in range(15):#prints the row 10 times
    for i in range(25):#prints one row of dots
        Sprite(dot,(20 + 40*i,20 + 40*j))
App().run()

