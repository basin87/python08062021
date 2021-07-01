s = str(input("Напишите любые слова: "))
syms = len(s)
syms2 = (len(s) - s.count(' '))
words = (s.count(' ') + 1)

print("Колличество символов: ", syms2)
print("Колличество слов: ", words)
