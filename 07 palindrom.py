oldword = input('write ur own word ')
newword = oldword[::-1].lower()
if oldword.lower() == newword:
    print('palindrom')
else:
    print('ne palindrom')

