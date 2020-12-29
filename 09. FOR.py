words = input("Введи товары:\t")

words = words.split(' ')
print(words)

for word in words:
    word1 = word[::-1].lower()
    if word.lower() == word1:
        print("Это палиндром")
    else:
        print("Это не палиндром")
