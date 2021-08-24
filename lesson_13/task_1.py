import csv
from dataclasses import dataclass


class Store:
    """Basic operations of store"""

    def __init__(self):
        self.data = []
        self.balance = 0
        self.sell_list = []

    def add_product(self, line, amount_of_times=5):
        self.data.extend([Product(line["Наименование"], line["Тип"], line["Цена"]) for _ in range(amount_of_times)])
        return self.data

    def import_products(self):
        with open("inventory.csv", "r+", encoding="UTF-8") as file:
            csv_reader = csv.DictReader(file)
            next(csv_reader)
            for line in csv_reader:
                self.add_product(line)
        return self.data

    def return_products(self, kind_of_product: str = " ") -> list:
        list_of_products = []
        for line in self.data:
            if line.kind_of_product == kind_of_product:
                list_of_products.append(line)
            if line.kind_of_product != kind_of_product:
                list_of_products.append(line)
        return list_of_products

    def overall_sum(self):
        sum_ = 0
        for line in self.data:
            sum_ += int(line.price)
        return sum_

    def sell_product(self, name):
        product_index = 0
        for i, line in enumerate(self.data):
            if line.name == name:
                product_index = i
                self.balance += int(line.price)
        if product_index != 0:
            self.data.pop(product_index)
        else:
            print("No such product in a store")

    def get_balance(self):
        return self.balance


@dataclass
class Product:
    """Description of product"""
    name: str
    kind_of_product: str
    price: int

    def __str__(self):
        return f"{self.name} - {self.kind_of_product}; price: {self.price} grn"

    def __repr__(self):
        return self.__str__()


# prod = Product('Earl Grey', 'tea', 25)
one = Store()
one.import_products()
print(one.overall_sum())
one.sell_product("Earl Grey")
print(one.get_balance())