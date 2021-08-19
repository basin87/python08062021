def hide_email(email) -> str:
    first_part, second_part = email.split("@")
    return first_part[:2] + '***@**' + second_part[-5:]


print(hide_email("somebody_email@gmail.com"))