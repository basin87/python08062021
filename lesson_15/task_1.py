import csv
import re


def check_number(number):
    match = re.findall(r"([А-ЯA-Z]){2}\d{4}[А-ЯA-Z]{2}", number)
    if match:
        print(f"It's a UA car plate, region is {ua_auto(number)}")
    else:
        print("Sorry, you aren't match the function!")


def ua_auto(number):
    with open("ua_auto.csv", "r+", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        region = " "
        for row in csv_reader:
            if row[1] == number[:2]:
                region = row[0]
        return region


def main():
    auto_plate = input("Enter UA number: ")
    ua_auto(auto_plate)
    check_number(auto_plate)


main()