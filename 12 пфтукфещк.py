from random import shuffle
letters = list('qwertyuiopasdfghjklzxcvbnm')
symbols = list('@#%$^&*')
bletters = list('QWERTYUIOPASDFGHJKLZXCVBNM')
numbers = list('1234567890')
list = list(letters+ bletters+ symbols+ numbers)
shuffle(list)
print(''.join(list[0:8]))

