temperature = int(input("Enter a temperature to convert:  "))
your_kind_of_temperature = input("Enter one of three type of measurers (Celsius, Kelvin, Fahrenheit): ")

#сделал_без_ретёрна_как_указано_по_заданию

def convertor_for_temperatures(amount_of_degrees: int, type_of_system: str):
    if type_of_system == "Celsius":
        value_kelvin = amount_of_degrees + 273.15
        value_fahrenheit = float(amount_of_degrees) * 9.0 / 5.0 + 32
        print(f"You temperature are {amount_of_degrees}°C, {value_kelvin} K, {value_fahrenheit} °F")
    elif type_of_system == "Kelvin":
        value_celsius = amount_of_degrees - 273.15
        value_fahrenheit = value_celsius * 9.0/5.00 + 32
        print(f"You temperature are {amount_of_degrees} K, {value_celsius} °C, {value_fahrenheit} °F")
    elif type_of_system == "Fahrenheit":
        value_celsius = (amount_of_degrees - 32) * 5.0/9.0
        value_kelvin = (amount_of_degrees - 32) * 5.0/9.0 + 273.15
        print(f"You temperature are {amount_of_degrees}°F, {value_celsius}°C, {value_kelvin} K")
    else:
        print("You entered invalid value")


convertor_for_temperatures(temperature, your_kind_of_temperature)