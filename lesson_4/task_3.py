def int_numbers(a,b):

    if a < b:
        for i in range(a, b + 1):
            yield i
    else:
        for i in range(a, b - 1, -1):
            yield i

a1 = int(input("Введите целое число A: "))
b1 = int(input("Введите целое число B: "))
for num in int_numbers(a1,b1):
    print(num)