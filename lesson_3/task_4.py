# Задание №4
list_of_six = []
for elements in range(100, 202, 6):
    list_of_six.append(elements)
print("Список: ",list_of_six)
for num in list_of_six:
    if (num % 5)==0 and num <= 150:
        print("Число из списка,которое делится на 5 и не больше 150: ",num)
