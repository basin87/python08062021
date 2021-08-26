import re


def check_password(password):
    if re.fullmatch(r'[a-zA-Z0-9$#@+=-]{8,}', password):
        print("Valid password")
    else:
        print("You don't match the validation system!")


client_password = input("Enter a password: ")
check_validation_password(client_password)