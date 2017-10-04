#Astro Ohnuma
#10/4/17
#betteradditiongamedemo.py - ask addition problems till user gets 5

from random import randint

numcorrect = 0
while numcorrect <5:
    num1 = randint(-10,10)
    num2 = randint(-10,10)
    question = 'What is'+str(num1)+'+'+str(num2)+'?'
    answer = int(input(question))
    break
