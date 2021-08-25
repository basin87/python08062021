import random


class House:
    def __init__(self, house_id):
        self.id = house_id
        self.amount_of_people = random.randint(1, 100)


class Street:
    def __init__(self, street_id):
        self.list_of_houses = []
        self.street_id = street_id
        self.fill_up_street()

    def fill_up_street(self):
        for i in range(random.randint(5, 20)):
            self.list_of_houses.append(House(i))


class City:
    def __init__(self):
        self.list_of_streets = []
        self.fill_up_city()
        self.record_in_order()

    def fill_up_city(self):
        for i in range(random.randint(3, 10)):
            self.list_of_streets.append(Street(i))

    def record_in_order(self):
        with open('example_of_a_city.txt.txt', 'w') as file:
            self.population = 0
            name = ["House", "Population"]
            file.write(f'Street {name[0].rjust(30)} {name[1].rjust(45)}\n')
            for street in self.list_of_streets:
                for house in street.list_of_houses:
                    info_for_file = [f"Street {street.street_id}", f"House {house.id}", f"{house.amount_of_people}"]
                    file.write(f'{info_for_file[0]} {info_for_file[1].rjust(30)} {info_for_file[2].rjust(40)}\n')
                    self.population += house.amount_of_people


city_1 = City()