isGuessed = False

while isGuessed != True:
    puzzle = "1 в степени 315 равно \n"
    answer = input(puzzle)

    if answer == '1':
        print('Да, Молодец!')
        isGuessed = True
    elif answer == '315':
        print('Нет, попался')
    else:
        print('Попробуй еще раз!')

print('Спасибо')
