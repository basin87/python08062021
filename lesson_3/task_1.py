# Задача №1
number3 = int(input("Введите трёхзначное число: "))
number1 = (number3 // 100)
number2 = ((number3 // 10) % 10)
number = (number3 % 10)
summa = (number1 + number2 + number)
print(number1, number2, number)
print(summa)
