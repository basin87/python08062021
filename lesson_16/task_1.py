import csv
import argparse
from re import search


class CheckDataAirport:
    def __init__(self, iata_code=None, country=None, name=None):
        self.data = self.load_data()
        self.iata_code = iata_code
        self.country = country
        self.name = name

    def load_data(self):
        with open("airport-codes_csv.csv", "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            return [line for line in csv_reader]

    def check_iata_data(self):
        for line in self.data:
            if line["iata_code"] == self.iata_code.upper():
                return line
        raise AirportNotFoundError(self.iata_code, message="Airport not found")

    def check_country(self):
        country_airports = []
        for line in self.data:
            if line['iso_country'] == self.country:
                country_airports.append(line)
        if not country_airports:
            raise CountryNotFoundError(self.country, message="Country not found")
        return country_airports

    def check_name_of_airport(self):
        list_of_names = []
        for line in self.data:
            if search(self.name, line['name']):
                list_of_names.append(line['name'])
        if not list_of_names:
            raise AirportNotFoundError(self.name, message="Airport not found")
        return list_of_names

    def check_validation_iata_code(self):
        valid_code = self.iata_code.upper()
        if valid_code == self.iata_code:
            print("Valid code")
        else:
            raise IATACodeError


def check_amount_of_params():
    if len([row for row in vars(args).values() if row is not None]) > 1:
        raise MultipleOptionsError(message="Just one parameter is necessary")
    if not len([row for row in vars(args).values() if row is not None]):
        raise NoOptionsFoundError(message="Parameters not found")


class AirportNotFoundError(Exception):
    """Exception raised for errors in the input ident_code or name error."""

    def __init__(self, iata_data: str, message="Airport not found"):
        self.iata_data = iata_data
        self.message = f"{iata_data} - {message}"
        super().__init__(self.message)


class CountryNotFoundError(Exception):

    """Exception raised for errors for airport location (country)"""
    def __init__(self, country, message="Country not found"):
        self.country = country
        self.message = f"{country} - {message}"
        super().__init__(self.message)


class MultipleOptionsError(Exception):
    def __init__(self, message="Just one parameter is necessary"):
        self.message = message
        super().__init__(self.message)


class NoOptionsFoundError(Exception):
    def __init__(self, message="Parameters not found"):
        self.message = message
        super().__init__(self.message)


class IATACodeError(Exception):
    def __init__(self, iata_code, message="Not valid value"):
        self.iata_code = iata_code
        self.message = f"{iata_code} - {message}"
        super().__init__(self.message)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Checking data from airport")
    parser.add_argument("--iata_code", help="Three capital letter")
    parser.add_argument("--country", help="Name of a country")
    parser.add_argument("--name", help="Name of airport")
    args = parser.parse_args()
    check_amount_of_params()
    first_try = CheckDataAirport(name=args.name, country=args.country, iata_code=args.iata_code)


print(first_try.check_iata_data())
# print(first_try.check_country())
# print(first_try.check_name_of_airport())
first_try.check_validation_iata_code()