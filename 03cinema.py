print('hi, dude! nice to meet u in the online cinema')
name = input('what is ur name?   ')
year = int(input('what year were u born in?  '))
age = 2020-year
if age >= 18:
    print('oh,', str(name)+', i have smth for u! horror might be good for such a big guy')
elif age >= 16:
    print('action film is a good option for u')
elif age >= 13:
    print('comedy might be interesting for u,', name)
else:
    print('movie seems like a good option for u')
