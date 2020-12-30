from random import choice as ch

dict = {}

guessed = False

while True:
    print('@' * 100)
    learn = input('what do u want to do? play or add words? ')

    if learn == 'add':
        add = input('write down two words(eng|rus) ').split()
        if len(add) == 2:
            engword = add[0]
            rusword = add[1]
            print(f'{engword} = {rusword}')

            if dict.get(engword) == None:
                dict[engword] = rusword
            else:
                print('!!!!this word is already in dictionary!!!!')

        if len(add) != 2:
            print('!!!!!write down one word in english and one in russian!!!!! ')

    if learn == 'play':
        print('?' * 100)
        while not guessed:
            p = ch(list(dict.keys()))
            answer = input(f'write down the translation for {p} ')
            if answer == dict[p]:
                print('!!!correct!!!')
                guessed = True
            else:
                print('try again')
