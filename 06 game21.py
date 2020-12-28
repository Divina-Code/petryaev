from random import randint as ri




guessed1 = False      #проиграл ли игрок 1
guessed2 = False      #проиграл ли игрок 2
guessed3 = False      #проиграл ли игрок 3
player1 = ri(1, 10)    #очки игрока 1
player2 = ri(1, 10)    #очки игрока 2
player3 = ri(1, 10)    #очки игрока 3
print(player1)
print(player2)
print(player3)



while guessed1 != True or guessed2 != True or guessed3 !=True:

    if guessed1 != True:
        do1 = input('take1 ')

        if do1 == 'yes' and player1 < 21:
            player1 += ri(1,10)
            print(player1)
            print('?'*100)
        elif do1 == 'yes' or do1 == 'no' and player1 > 21:
            player1 = 0
            guessed1 = True
            print('player1 has ', player1,'points')
            print('?'*100)
        else:
            guessed1 = True
            print(player1)
            print('the end for player1     ', player1, 'points')
            print('?'*100)




    if guessed2 != True:
        do2 = input('take2 ')

        if do2 == 'yes' and player2 < 21:
            player2 += ri(1,10)
            print(player2)
            print('?'*100)
        elif do2 == 'yes' or do2 == 'no' and player2 > 21:
            player2 = 0
            guessed2 = True
            print('player2 has ', player2,'points')
            print('?'*100)
        else:
            guessed2 = True
            print(player2)
            print('the end for player2     ', player2, 'points')
            print('?'*100)


    if guessed3 != True:
        do3 = input('take3 ')

        if do3 == 'yes' and player3 < 21:
            player3 += ri(1,10)
            print(player3)
            print('?'*100)

        elif do3 == 'yes' or do3 == 'no' and player3 > 21:
            player3 = 0
            guessed3 = True
            print('player3 has ', player3,'points')
            print('?'*100)
        else:
            guessed3 = True
            print(player3)
            print('the end for player3     ', player3, 'points')
            print('?'*100)




if player1 > player2 and player1 > player3 and player1 <= 21:
    print('and the winner is ')
    print('player1')
elif player2 > player1 and player2 > player3 and player2 <= 21:
    print('and the winner is ')
    print('player2')
elif player3 > player2 and player3 > player1 and player3 <= 21:
    print('and the winner is ')
    print('player3')
else:
    print('and it is a draw')

