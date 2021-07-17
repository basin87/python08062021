import json
import datetime


def convert_seconds(x):
    convert_time = datetime.timedelta(seconds=x)
    return convert_time


with open("acdc.json", "r") as file:
    file_dict = json.load(file)
    data_for_duration = file_dict["album"]["tracks"]["track"]


def parse_time(value):
    list_of_duration = []
    for item in data_for_duration:
        for x in item:
            list_of_duration.append(int(item.get("duration")))
            break

    overall_time_of_songs = sum(list_of_duration)
    return overall_time_of_songs


print("Total amount is " + str(parse_time(data_for_duration)) + " seconds")
print(f"Album duration is {convert_seconds(parse_time(data_for_duration))}")

