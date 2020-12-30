from random import choice as ch

while True:  #вводим программу в бесконечный цикл
#вводим в игру слова
    list = ['soul', 'ball', 'net', 'game']
    word = ch(list)

    guessed = False  #отгадано ли слово(закончена ли игра)
    lives = 10  #кол-во жизней
    letters = []  #начальное кол-во символов в поле вывода(список)
#создаем основной цикл
    while not guessed:
    #создаем пустые места, сначала узнав, сколько букв в загадонном слове
        if letters.count('_') == 0:
            for a in word:
                letters.append('_')
            print(''.join(letters))
        answer = input('write down one letter or whole word ')  #вводим преполагаемую букву или слово
    #заменяем каждый пробел буквой
        lives -= 1  #отнимаем жизнь каждую попытку
        for a in range(len(word)):
            if answer == word[a]:
                letters[a] = word[a]
    #условие на победу, когда не остается пробелов
        print(''.join(letters))
        if letters.count('_') == 0:
            print('u won')
            guessed = True
    #условие на поражение, если кончаются жизни
        if lives == 0:
            print('u lost')
            guessed = True
    #условие на победу или поражение при вводе целого слова
        if len(answer) > 1:
            if answer == word:
                print('u won')
                guessed = True
            else:
                print('u lost')
                guessed = True
