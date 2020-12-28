from random import randint as ri
from time import sleep
print('find the mystery number')
mysterynumber = ri(0, 100)
guessed = False
sleep(3)
while guessed != True:
    answer = int(input('the mystery number is '))
    if answer == mysterynumber:
        print('\nu are so lucky')
        guessed = True
    elif answer > mysterynumber:
        print('\nthe mystery number is smaller')
    else:
        print('\nthe mystery number is bigger')
print('u DID it!!!!!')

