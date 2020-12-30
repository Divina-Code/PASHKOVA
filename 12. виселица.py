print('Добро пожаловать в игру! ')
word  = 'АЛЛОТРОПИЯ'

letters = []
for a in word:
    letters.append("_")


print(' '.join(letters))

stop = False
lives = 10

while stop == False:
    answer = input("Введите букву или слово\n")

    if answer == word:
        for a in range(len(word)):
            letters[a] = word[a]
        print('Да! Вы угадали слово!')
        stop = True

    if answer != word:
        for i in range(len(word)):
            if answer == word[i]:
                letters[i] = word[i]

        if list(word) == letters:
            print('Да! Вы угадали слово!')
            stop = True

    if lives == 1:
        stop = True
        print('Вы проиграли! Попробуйте еще раз.')



    lives += -1

    print(''.join(letters))

    if stop == False:
        if lives > 4:
            print('У вас осталось', lives, 'попыток\n')
        elif 1<lives<4:
            print('У вас осталось', lives, 'попытки\n')
        else:
            print('У вас осталось', lives, 'попытка\n')

print('Спасибо за игру!')
