print('find the mystery number')
guessed = False
while guessed != True:
    answer =input('the mystery number is ')
    if answer == '40':
        print('u are so lucky')
        guessed = True
    elif answer > '40':
        print('the number is smaller')
    else:
        print('the number is bigger')
print('u DID it')


