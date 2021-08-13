
import datetime

city = input("Enter name of your city: ")
amount_of_days = int(input("Enter the number of days for forecast: "))


def get_data():
    received_data = requests.get("https://api.openweathermap.org/data/2.5/forecast/daily?"
                                 f"q=Odesa&cnt=5&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8",
                                 params={"amount_of_days": amount_of_days, "city": city})
    return received_data.json()


def extracted_data() -> list:
    info_json = get_data()
    list_of_data = []
    for key in info_json["list"]:
        data_for_insert = []
        if len(str(key["dt"])) > 9:
            full_date = datetime.datetime.fromtimestamp(key["dt"])
            date = full_date.strftime("%d-%m-%Y")
            data_for_insert.append(date)
        data_for_insert.append(str(key["temp"]["day"]))
        data_for_insert.append(str(key["feels_like"]["day"]))
        data_for_insert.append(str(key["temp"]["night"]))
        list_of_data.append(data_for_insert)
    return list_of_data


def verified_name_for_file(data):
    insert_in_name = get_data()
    transform_date = datetime.datetime.fromtimestamp(insert_in_name['list'][0]["dt"])
    date = transform_date.strftime("%d-%m-%Y")
    verified_name = "".join(str(date) + "-" + str(insert_in_name["city"]["name"]) + "-" + str(insert_in_name["cnt"]))
    return verified_name


def save_to_file(filename):
    with open(f"{filename}-days-weather-forecast.txt", "w") as file:
        formatting_data = extracted_data()
        for day_data in formatting_data:
            file.write("         ".join(day_data) + "\n")


def main():
    data = get_data()
    file_name = verified_name_for_file(data)
    save_to_file(file_name)


main()