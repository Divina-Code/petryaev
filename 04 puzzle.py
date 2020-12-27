guessed = False

while guessed != True:
    puzzle = '\nЭта цифра просто чудо.\nУ нее родня повсюду.\nДаже в алфавите есть у нее сестра—близнец.\n'
    answer = input(puzzle)
    if answer == '3':
        print('BIG BRAINS TIIIME!!!!')
        guessed = True
    else:
        print('try again')
print('u did it')
