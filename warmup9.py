#Astro Ohnuma
#10/4/17
#warmup9.py - Capitalizing vowels in a word

word = input('Enter a word: ')
for ch in word:
    if ch in 'aeiouAEIOU':
        print(ch.upper())
    else:
        print(ch.lower())

