def convertor_for_temperatures(amount_of_degrees: int, type_of_system: str):
    if type_of_system == "Celsius":
        value_kelvin = amount_of_degrees + 273.15
        value_fahrenheit = float(amount_of_degrees) * 9.0 / 5.0 + 32
        return value_kelvin, value_fahrenheit
    elif type_of_system == "Kelvin":
        value_celsius = amount_of_degrees - 273.15
        value_fahrenheit = value_celsius * 9.0/5.00 + 32
        return value_celsius, value_fahrenheit
    elif type_of_system == "Fahrenheit":
        value_celsius = (amount_of_degrees - 32) * 5.0/9.0
        value_kelvin = (amount_of_degrees - 32) * 5.0/9.0 + 273.15
        return value_celsius, value_kelvin
    else:
        print("You entered invalid value")