from datetime import datetime
from uuid import uuid4


class BankAccount:
    def __init__(self, name_account: str, balance: float):
        self.uuid = uuid4 ()
        self.name_account = name_account
        self.balance = float ("{:.2f}".format (balance))
        self.transaction = []
        self.bank_commission = 0.99
        self.current_date = datetime.today ().strftime ('%d-%m-%Y')

    def deposit_funds(self, amount_of_funds: int):
        self.balance += amount_of_funds
        self.balance *= self.bank_commission
        self.transaction.append (["deposit", amount_of_funds, self.current_date])
        return self.balance + amount_of_funds

    def withdraw_funds(self, amount_of_funds: int):
        self.transaction.append (["credit", amount_of_funds, self.current_date])
        self.balance *= self.bank_commission
        return self.balance - amount_of_funds

    def get_balance(self):
        return self.balance


account_one = BankAccount("One", 10000)
