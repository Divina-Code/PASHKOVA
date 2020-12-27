import random
number = random.randrange(-10, 10)
input(number)

isGuassed = False
while isGuassed != True:
    usernumber=input('Введите число')

    if int(usernumber)> number:
        print('Ваше число больше, попробуйте еще раз')
    elif int(usernumber)< number:
        print('Ваше число меньше, попробуйте еще раз')
    else:
        print('Вы угадали число')
        isGuassed = True

print('Спасибо за игру!')
