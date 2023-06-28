slovo = input('Введите слово:  ')
turn = slovo[::-1]
if slovo == turn:
    print('True')
else:
    print('False')
