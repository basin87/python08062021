#Задание №5
import random
random_number = random.randrange(1, 10)

attempt = 0
amount_of_attempts = 3
while amount_of_attempts > attempt:
    users_input = int(input("Enter a number in range from 1 till 10: "))
    attempt += 1
    if users_input == random_number:
        print("You won!")
    else:
        print("You lose!")