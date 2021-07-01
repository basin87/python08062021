def is_prime(number):
    if number % 2 == 0 and number != 2:
        return False
    if number == 0 or number == 1:
        return False
    for n in range(3, number):
        if number % n == 0:
            return False
    return True
n = int(input('Введите число от 0 до 1000: '))
print(is_prime(n))