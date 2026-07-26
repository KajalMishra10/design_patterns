EXTRA_SUGAR_COST = 5
EXTRA_MILK_COST = 10


class CoffeeDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def get_cost(self):
        return self._coffee.get_cost()

    def get_description(self):
        return self._coffee.get_description()

class ExtraSugar(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self):
        return self._coffee.get_cost() + EXTRA_SUGAR_COST

    def get_description(self):
        return f"{self._coffee.get_description()}, Extra Sugar"

class ExtraMilk(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self):
        return self._coffee.get_cost() + EXTRA_MILK_COST

    def get_description(self):
        return f"{self._coffee.get_description()}, Extra Milk"


ADDON_DECORATORS = {
    "extra_sugar": ExtraSugar,
    "extra_milk": ExtraMilk,
}

ADDON_PRICES = {
    "extra_sugar": EXTRA_SUGAR_COST,
    "extra_milk": EXTRA_MILK_COST,
}