#Задание №5
#№1 попытка
import random
player1=int(input("Попытка №1.Введите число от 1 до 10: "))
player2=random.randint(0,10)
print(player1,player2)
if player1>player2 or player1<player2:
    print("You lose!")
else:
    print("You win!")
#№2 попытка
player3=int(input("Попытка №2.Введите число от 1 до 10: "))
player4=random.randint(0,10)
print(player3,player4)
if player3>player4 or player3<player4:
    print("You lose!")
else:
    print("You win!")
#№3 попытка
player5=int(input("Попытка №3.Введите число от 1 до 10: "))
player6=random.randint(0,10)
print(player5,player6)
if player5>player6 or player5<player6:
    print("You lose!")
else:
    print("You win!")
