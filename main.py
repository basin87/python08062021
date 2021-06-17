#Задание №1
privet = input("Введите Ваше имя: ")
print("Hello, " +privet,"!")

#Задание №2
intnumber=int(input("Please enter an integer number: "))
nextnumber= intnumber + 1
prenumber= intnumber - 1
print("The next number for the number", intnumber, "is", nextnumber)
print("The previous number for the number", intnumber, "is", prenumber)

#Задание №3
v=int(input("Введите скорость велосипедиста: "))
t=int(input("Введите время через которое остановится велосипедист: "))
dlina=100
if v>0:
    ostanovka = abs(dlina - (v * t))
    print ("Вася движется в положительном направлении")
if v<0:
    print("Вася движется в отрицательном направлении")
    ostanovka = abs(dlina-(v*t))
print("и остановился на:", ostanovka,"км")

#Задание №4
year=int(input("Введите год: "))
if year%4==0 and year%100!=0 or year%400==0:
    print("YES")
else:
    print("NO")

#Задание №5
x=int(input("Введите число: "))
if x>0:
    print("sign(x)=1")
elif x==0:
    print("sign(x)=0")
else:
    print("sign(x)=-1")


#Задание #6*
x=abs(float(input("Введите значение для поиска в списке: ")))
a=[10,20,30,40,50,60,70,80,90,100]
for y in [a]:
    if x in y:
        print("Число", x,"присутствует в списке")
    else:
        print("Число", x,"отсутствует в списке")


#Задание №7**
number=int(input("Укажите желаемое кол-во звёздочек: "))
print ("*" * number)
