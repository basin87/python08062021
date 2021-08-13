def splitted_string(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = result.split()
        return result
    return wrapper


@splitted_string
def users_input(some_string):
    users_data = input("Give me a string, please: ")
    return users_data


print(users_input(some_string="hello"))
