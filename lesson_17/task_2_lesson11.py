name_list = ["ШАЛАШ", "КАЗАК", "ДЕД", "ДОХОД", "13231"]


def check_name(sequence_of_names: list):
    checked_list = []
    for item in sequence_of_names:
        if item == item[::-1]:
            checked_list.append(item)
        else:
            print("You lose")
    return checked_list


print(check_name(name_list))