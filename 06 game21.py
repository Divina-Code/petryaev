from random import randint as ri
from time import sleep
guessed1 = False
guessed2 = False
guessed3 = False
player1 = ri(1, 10)
player2 = ri(1, 10)
player3 = ri(1, 10)
print(player1)
print(player2)
print(player3)

while guessed1 != True:
    do1 = input('take1 ')
    if do1 == 'yes' and player1 < 21:
        player1 += ri(1,10)
        print(player1)
    else:
        guessed1 = True
        print(player1)
        print('the end for player1     ', player1, 'points')
while guessed2 != True:
    do2 = input('take2 ')
    if do2 == 'yes' and player2 < 21:
        player2 += ri(1,10)
        print(player2)
    else:
        guessed2 = True
        print(player2)
        print('the end for player2     ', player2, 'points')
while guessed3 != True:
    do3 = input('take3 ')
    if do3 == 'yes' and player3 < 21:
        player3 += ri(1,10)
        print(player3)
    else:
        guessed3 = True
        print(player3)
        print('the end for player3     ', player3, 'points')
if player1 > player2 and player2 <= 21 and player1 > player3 and player3 <= 21 and player1 <= 21:
    print('and the winner is ')
    sleep(3)
    print('player1')
elif player2 > player1 and player1 <= 21 and player2 > player3 and player3 <= 21 and player2 <= 21:
    print('and the winner is ')
    sleep(3)
    print('player2')
elif player3 > player2 and player2 <= 21 and player3 > player1 and player1 <=21 and player3 <= 21:
    print('and the winner is ')
    sleep(3)
    print('player3')
else:
    print('we have no winners')
