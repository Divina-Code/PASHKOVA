word=input('Введите слово')
word1 = word[::-1].lower()
word=word.lower()
if word==word1:
    print ("Это палиндром")
else:
    print("Это не палиндром")

