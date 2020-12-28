from random import randint as ri
from time import sleep
game1 = False
game2 = False
game3 = False
guessed1 = False
guessed2 = False
guessed3 = False
player1 = ri(1, 10)
player2 = ri(1, 10)
player3 = ri(1, 10)
print(player1)
print(player2)
print(player3)
while game1 != True or game2 != True or game3 !=True:

    while guessed1 != True:
        do1 = input('take1 ')
        if do1 == 'yes' and player1 < 21:
            player1 += ri(1,10)
            print(player1)
        elif do1 == 'yes' and player1 > 21:
            player1 = 0
            game1 = True
            guessed1 = True
        else:
            guessed1 = True
            print(player1)
            print('the end for player1     ', player1, 'points')
            game1 = True
    while guessed2 != True:
        do2 = input('take2 ')
        if do2 == 'yes' and player2 < 21:
            player2 += ri(1,10)
            print(player2)
        elif do2 == 'yes' and player1 > 21:
            player2 = 0
            game2 = True
            guessed2 = True
        else:
            guessed2 = True
            print(player2)
            print('the end for player2     ', player2, 'points')
            game2 = True
    while guessed3 != True:
        do3 = input('take3 ')
        if do3 == 'yes' and player3 < 21:
            player3 += ri(1,10)
            print(player3)

        elif do3 == 'yes' and player1 > 21:
            player3 = 0
            game3 = True
            guessed3 = True
        else:
            guessed3 = True
            print(player3)
            print('the end for player3     ', player3, 'points')
            game3 = True
if player1 > player2 and player1 > player3 and player1 <= 21:
    print('and the winner is ')
    sleep(3)
    print('player1')
elif player2 > player1 and player2 > player3 and player2 <= 21:
    print('and the winner is ')
    sleep(3)
    print('player2')
elif player3 > player2 and player3 > player1 and player3 <= 21:
    print('and the winner is ')
    sleep(3)
    print('player3')

