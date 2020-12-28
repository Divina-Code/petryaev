print('find the mystery number')
guessed = False
while guessed != True:
    answer =int(input('the mystery number is '))
    if answer == 40:
        print('\nu are so lucky')
        guessed = True
    elif answer > 40:
        print('\nthe mystery number is smaller')
    else:
        print('\nthe mystery number is bigger')
print('u DID it!!!!!')


