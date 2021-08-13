import argparse
import csv
import sys


def preparing_args_for_name():
    for key in list(args_dict):
        value = args_dict[key]
        if value is None or key == "o":
            del args_dict[key]
    return args_dict


def check_args(row):
    arguments_dict = {key: value for key, value in args_dict.items() if value is not None}
    if not arguments_dict:
        sys.exit(ValueError("You miss arguments for task"))
    map_dict = {
        "brand": "BRAND",
        "color": "COLOR",
        "year": "MAKE_YEAR",
        "fuel": "FUEL",
        "reg_num": "N_REG_NEW"
    }
    result = []
    for key, value in arguments_dict.items():
        if row[map_dict[key]] == value:
            result.append(True)
        else:
            result.append(False)
    return all(result)


def create_filename():
    current_list = []
    title = preparing_args_for_name()
    for key in title:
        value = title[key]
        if key == "o":
            continue
        else:
            current_list.append(value)
    args_for_name = "-".join(current_list)
    return f"{args_for_name}.csv"


def create_csv_file():
    result = []
    with open(args.o, "r+", encoding="utf-8") as File:
        csv_reader = csv.DictReader(File, delimiter=";")
        for row in csv_reader:
            if check_args(row):
                result.append(row)
    write_csv(result)


def write_csv(result):
    fieldnames = ["D_REG", "BRAND", "MODEL", "COLOR", "MAKE_YEAR", "FUEL", "N_REG_NEW"]
    with open(create_filename(), "w+", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, delimiter=" ", fieldnames=fieldnames,
                                extrasaction="ignore")
        writer.writeheader()
        for row in result:
            writer.writerow(row)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This is program for checking car number and all info"
                                                 "which car can consist")
    parser.add_argument("o")
    parser.add_argument("--brand")
    parser.add_argument("--color")
    parser.add_argument("--year")
    parser.add_argument("--fuel")
    parser.add_argument("--reg_num")
    args = parser.parse_args()
    args_dict = {"brand": args.brand, "color": args.color, "year": args.year,
                 "fuel": args.fuel, "reg_num": args.reg_num}
    # create_csv_file()
print(args.brand)