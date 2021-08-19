name_list = ["Mother", "Father", "Brother", "Sister", "123", "234", "345", "Я", "!"]


def change_place(list_of_data, n):
    n = -n % len(list_of_data)
    return list_of_data[n:] + list_of_data[:n]


print(change_place(name_list, 6))