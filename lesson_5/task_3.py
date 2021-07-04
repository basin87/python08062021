print ("1-треугольник, 2-квадрат")
figure = input ("Выберите фигуру: ")

def fig():
    if figure == '1':
        print ("Длины сторон треугольника:")
        a = float (input ("a = "))
        b = float (input ("b = "))
        c = float (input ("c = "))
        p = (a + b + c) / 2
        from math import sqrt
        s = sqrt(p * (p - a) * (p - b) * (p - c))
        print("Площадь: %.2f" % s)
    elif figure == '2':
        print("Длина сторон квадрата:")
        a = float(input ("a = "))
        print("Площадь: %.2f" % (a * a))
    else:
        print("Не правильный ввод.\nВыберите из списка, от 1 - 2")
    return
fig()
