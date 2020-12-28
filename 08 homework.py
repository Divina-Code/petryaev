meme = False  #переменная, отвечающая за продолжительность цикла
productlist=[]  #список продуктов


while meme != True:
    answer = int(input('press 1, 2 or 3 '))
    if answer == 1:
        add = input('choose what do u want to add ')  #то, что нужно добавить в список
        productlist.append(add)
    elif answer == 2:
        dropout = int(input('choose number of what do u want to drop out '))  #номер того, что нужно убрать из списка
        productlist.pop(dropout)
    elif answer == 3:
        print(productlist)
    else:
        print('try again')


