def int_numbers():
    a = int(input("Введите целое число A: "))
    b = int(input("Введите целое число B: "))
    if a < b:
        for i in range(a, b + 1):
            print(i)
    else:
        for i in range(a, b - 1, -1):
            print(i)
    return()
int_numbers()