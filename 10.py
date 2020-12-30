from random import choice, shuffle
words = ['community', 'navigation', 'aplication', 'camera']
word = choice(words).lower()
random = list(word)
shuffle(random)
print(random)

inprog = True
while inprog:
    choice = input('identify mystery word '+ ''.join(random)+ '\t')
    if choice == word:
        print('YES')
        word = choice(words).lower()
        shuffle(random)
        random = list(word)

    else:
        print('TRY AGAIN')




