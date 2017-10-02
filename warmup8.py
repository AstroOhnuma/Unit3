#Astro Ohnuma
#10/2/17
#warmup8.py - Find the sum of all positive integers less than 100,000 that are divisble by 3, 10, and 17
total = 0
for i in range(1,100001):
    if i%3==0 and i%10==0 and i%17==0:
        total+= i
print(total)