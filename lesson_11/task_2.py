name_list = ["ШАЛАШ", "КАЗАК", "ДЕД", "ДОХОД", "13231"]


def checkname(sequence_of_names):
    for item in sequence_of_names:
        if item == item[::-1]:
            print("Palindrome")
        else:
            print("Not palindrome")


checkname(name_list)