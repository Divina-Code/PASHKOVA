Dict = { }
a = True
from random import choice
while True:
    a = True
    answer = input('Введите [1] если хотите ввести слово-перевод\nВведите [2] если хотите поиграть\n')
    if answer == "1":
        ans = input("Введите слово и его перевод").split()
        if len(ans) == 2:
            word = ans[0]
            translate = ans[1]
            if Dict.get(word) == None:
                Dict[word] = translate
    if answer == '2':
        s1 = True
        while a:
            if s1:
                s = choice(list(Dict.keys()))
            ans1 = input(f'Напишите перевод слова {s}')
            if Dict[s] == ans1:
                print('Да! Ты прав!')
                a = False
            else:
                print('Нет, попробуй еще раз')
                s1 = False
