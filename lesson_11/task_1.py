def write_file():
    with open("users_input.txt", 'w') as file:
        while True:
            line = input("Enter any text: ")
            if line == '':
                break
            file.write(line + '\n')


write_file()