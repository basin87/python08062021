def user_input():
    list_of_numbers = []
    while True:
        user_input = int(input("Enter number: "))
        if user_input == 0:
            break
        list_of_numbers.append(user_input)
    return list_of_numbers

def composition(list_of_numbers: list) -> int:
    n = int(input())
    mult = 1
    while n > 0:
        digit = n % 10
        mult *= digit
        n = n // 10
    return mult

def amount_of_entered_numbers(list_of_numbers: list) -> int:
    return len(list_of_numbers)

def sum_of_numbers(list_of_numbers: list) -> int:
    return sum(list_of_numbers)

def maximumnumber(list_of_numbers: list) -> int:
    our_list2=list_of_numbers.copy()
    max_value2=max(our_list2)
    max(our_list2)
    return max(our_list2)


def second_max_value(list_of_numbers: list) -> int:
    our_list = list_of_numbers.copy()
    max_value = max(our_list)
    our_list.pop(our_list.index(max_value))
    return max(our_list)

def main():
    list_of_numbers = user_input()
    functions_to_call = {'Number of elements: ': amount_of_entered_numbers,
                         'Second max value: ': second_max_value,
                         'Sum of elements: ': sum_of_numbers,
                         'Max number: ': maximumnumber,
                         'Composition: ': composition,
                         }
    for key, func in functions_to_call.items():
        print(key, func(list_of_numbers))

main()
