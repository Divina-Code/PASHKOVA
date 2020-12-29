print('Welcome to the game\n')  #приветствие
from random import randint as ri
from time import sleep as sl
sl(1)
print('*******************************')
user1 = ri(2,11)          #количество 'монет' у первого игрока в начале игры
user2 = ri(2,11)          #количество 'монет' у второго игрока в начале игры
user3 = ri(2,11)          #количество 'монет' у третьего игрока в начале игры

print('If you want continue to game write YES\nIf you want to complete game write NO \n')    #условие игры
sl(3)

game1= True
game2= True
game3= True

while game1 !=False or game2 !=False or game3 !=False:
    if game1 !=False:
        print('User 1, Your coins', user1)             #количество 'монет' у первого игрока
        ans1 = input('User 1, Do you want to continue?\n').upper()   #хочет ли игрок продолжить игру
        sl(1)
    if ans1=='YES':
        user1+=ri(2,11)
    if int(user1)==21:
        print('User 1, you collected 21 coins!\n')
        game1=False
    elif game1== True and (ans1=='NO' or user1>21):
        print('User 1, you left the game\n')
        game1 =False


    if game2 !=False:
        print('User 2, Your coins', user2)
        ans2 = input('User 2, Do you want to continue?\n').upper()
        sl(1)
    if ans2=='YES':
        user2+=ri(2,11)
    if int(user2)==21:
        print('User 2, you collected 21 coins!\n')
        game2=False
    elif game2== True and (ans2=='NO' or user2>21):
        print('User 2, you left the game\n')
        game2 =False


    if game3 !=False:
        print('User 3, Your coins', user3)
        ans3 = input('User 3, Do you want to continue?\n').upper()
        sl(1)
    if ans3=='YES':
        user3+=ri(2,11)
    if int(user3)==21:
        print('User 3, you collected 21 coins!\n')
        game3=False
    elif game3== True and (ans3=='NO' or user3>21):
        print('User 3, you left the game\n')
        game3 =False


print('Results of the game:\n')

sp=[user1, user2, user3]
u = 0

while u < len(sp):   #если колво монет больше 21, игрок проиграл
    if sp[u] > 21:
        print('User',u+1,', you LOST!')
    u += 1


y = max(filter(lambda x: x <= 21, sp))  #ищем максимальное колво монет, не превышающее 21

if user1<=21:
    if user1==y:
        print('User 1, you WIN!')    #если у игрока максимальное колво монет, не превышающее 21, этот игрок побеждает
if user2<=21:
    if user2==y:
        print('User 2, you WIN!')
if user3<=21:
    if user3==y:
        print('User 3, you WIN!')

sl(1)
print('\nThanks for playing!')

#проигравшим считаем игрока, набравшего более 21 монеты. Если игрок не набрал более 21 монеты, и не победил - проигравшим его не считаем
