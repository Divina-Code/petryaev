
from random import randint as ri

code = str(ri(100, 999))

guessed = False

rightnumbers = 0

rightplaced = 0

while not guessed:
    print('@'*100)
    rightnumbers = 0
    choice = input('identify 3-signs number----')
    if len(choice) != 3 or not choice.isdigit():
        print('it is not a 3-signs number or a number at all')
    elif choice == code:
        print('u won')
        guessed = True
    else:
        for a in code:
            if a in choice:
                rightnumbers += 1
        for b in range(3):
            if choice[b] == code[b]:
                rightplaced += 1

    print('u identify', rightnumbers, 'numbers\n', rightplaced, 'of them is|are correcty placed')





