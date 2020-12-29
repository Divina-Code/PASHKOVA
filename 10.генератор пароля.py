from random import  choice,shuffle

letters=list('abcdefghijklmnopqrstuvwxyz')
symb = list('!@#$%^&*()_+')
numeral = list('0123456789')

l = int(input('Сколько букв вы хотите в своем пароле?\n'))
n = int(input('Сколько цифр вы хотите в своем пароле?\n'))
s = int(input('Сколько спец символов вы хотите в своем пароле?\n'))


p1=''
p2=''
p3=''
pas=''
for i in range(l):
        p1 += choice(letters)

for y in range(n):
        p2 += choice(numeral)

for k in range(s):
        p3 += choice(symb)

pas=p1+p2+p3
lst = list(pas)
shuffle(lst)
print(''.join(lst))

