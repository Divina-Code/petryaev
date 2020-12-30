from random import randint as ri
print('find the mystery number')
mysterynumber = ri(0, 100)
guessed = False
lives = 10
while guessed != True and lives != 0 :
    lives -= 1
    answer = int(input('the mystery number is '))
    if answer == mysterynumber:
            print('\nu are so lucky')
            guessed = True
    elif answer > mysterynumber:
            print('\nthe mystery number is smaller')
    else:
            print('\nthe mystery number is bigger')
print('The End')

