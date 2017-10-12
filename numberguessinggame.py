#Astro Ohnuma
#10/4/17
#numbergeussinggame.py - geussing a number between 1 and 100
from random import randint
random = randint(1,100)
while True:
    num = int(input('Guess a number between 1 and 100: ')
    if num < random:
        print('Too low!')
    
