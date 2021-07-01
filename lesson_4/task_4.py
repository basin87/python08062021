def ladder():
    n= int(input("Введите целое число <=9: "))
    for index in range(1, n+1):
        for index2 in range(1, index+1):
            print(index2, end="")
        print()
ladder()
