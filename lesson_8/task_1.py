import argparse
import datetime
import json
import time


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This is program for converting currencies. "
                                                 "Default value USD to UAH just for convenience")
    parser.add_argument("currency_from")
    parser.add_argument("currency_to")
    parser.add_argument("amount")
    parser.add_argument("-sd", "--start_date")
    args = parser.parse_args()


def get_data(currency_from_exchange, currency_to_exchange, amount_of_money, start_date):
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    initial_list = [['date', 'from', 'to', 'amount', 'rate', 'result']]
    while start_date < datetime.datetime.now():
        received_data = requests.get("https://api.exchangerate.host/convert",
                                     params={"from": currency_from_exchange, "to": currency_to_exchange,
                                             "amount": amount_of_money, "date": start_date}).json()
        built_list = [received_data["date"], received_data["query"]["from"], received_data["query"]["to"],
                      received_data["query"]["amount"], received_data["info"]["rate"], received_data["result"]]
        initial_list.append(built_list)
        start_date = start_date + datetime.timedelta(days=1)
        time.sleep(1)
    for x in initial_list:
        print(x)


def parsing_symbols():
    with open("symbols.json", "r") as file:
        check_symbols = json.load(file)
        list_of_symbols = check_symbols["symbols"]
    if args.currency_from not in list_of_symbols:
        print("Sorry, you enter invalid currency to exchange from")
    if args.currency_to not in list_of_symbols:
        print("Sorry, you enter invalid currency to exchange to")


def main():
    parsing_symbols()
    get_data(args.currency_from, args.currency_to, args.amount, args.start_date)


main()