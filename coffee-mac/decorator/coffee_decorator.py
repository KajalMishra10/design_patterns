from addon.addon import Addon


class CoffeeDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def get_cost(self):
        return self._coffee.get_cost()

    def get_description(self):
        return self._coffee.get_description()


class AddonDecorator(CoffeeDecorator):

    def __init__(self, coffee, addon: Addon):
        super().__init__(coffee)
        self._addon = addon

    def get_cost(self):
        return super().get_cost() + self._addon.price

    def get_description(self):
        return f"{super().get_description()}, {self._addon.name}"