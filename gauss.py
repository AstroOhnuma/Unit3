#Astro Ohnuma
#9/29/17
#gauss.py - using a loop to add up all the numbers from 1 to 100

num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
num3 = int(input('Enter the difference you want between each term: '))
total = 0
for i in range(num1,num2+1,num3):
    total += i
print('The sum of the numbers from',num1,'to',num2,'is',total)
