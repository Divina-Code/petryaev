print('hello, dude!')
name = input('what is ur name?    ')
print('nice to meet u,', name)
print('there are', len(str(name)), 'letters in ur name ')
year = int(input('what year were u born in?    '))
if len(str(year)) == 4:
    print('oh', year, 'was great')
    age = int(2020-year)
    print('u are already', age, '!')
else:
    print('oh, how can it be so? u were not born, yet, or u r so old? or u made a mistake? ')
