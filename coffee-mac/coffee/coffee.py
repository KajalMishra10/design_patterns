
from enums.coffee_type import CoffeeType


from abc import ABC


class Coffee(ABC):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.price

    def get_description(self):
        return self.name


class Cappuccino(Coffee):
    def __init__(self):
        super().__init__(CoffeeType.CAPPUCCINO, 80)

class Espresso(Coffee):

    def __init__(self):
        super().__init__(CoffeeType.ESPRESSO, 50)
