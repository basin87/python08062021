#Задача №6**
x1 = int(input("Enter current X location : "))
y1 = int(input("Enter current Y location : "))
x2 = int(input("Enter the current location : "))
y2 = int(input("Enter the current location : "))

data_x = abs(x2 - x1)
data_y = abs(y2 - y1)

if data_x == 1 and data_y == 2 or data_x == 2 and data_y == 1:
    print("Yes, your move will be ok!")
else:
    print("Sorry, your position is wrong")