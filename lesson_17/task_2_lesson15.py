import re


def check_tel_number(tel_number: str) -> str:
    match = re.search(r'(\d{2})(\d{3})(\d{3})(\d{2})(\d{2})', tel_number)
    if match:
        return re.sub(r'(\d{2})(\d{3})(\d{3})(\d{2})(\d{2})', r'(+\1) \2-\3-\4-\5', tel_number)
    else:
        print('Failed to recognize number')


print(check_tel_number("380966664666"))