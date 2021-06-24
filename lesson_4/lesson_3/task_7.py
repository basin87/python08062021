#Задание №7**
number=int(input("Введите любое число: "))
faktorial = 1
for item in range(1,number+1):
    faktorial*=item
print(f"Факториал числа \'{number}':",faktorial)

