print('Today is beautiful day to go shopping!\n')
shopping = []

stop=True

while stop !=False:
    answer = input("You want to add product to list[1], delete[2], see whole list[3] or complete the list[0]\n ")

    if answer == '1':
            product = str(input("What to add in list?"))
            shopping.append(product)                     #добавить продукт в список

    if answer == '2':
            product = str(input('What do yju want to remove?'))
            shopping.remove(product)                     #удалить продукт из списока
    if answer == '3':
            print(shopping)                            #показать весь список
    if answer == '0':
        stop = False               #завершить список

print('Have a nice day!')
