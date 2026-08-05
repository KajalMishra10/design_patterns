
from coffee.coffee import Espresso, Cappuccino
from enums.coffee_type import CoffeeType


class CoffeeFactory:

    _coffee_map = {
        CoffeeType.ESPRESSO: Espresso,
        CoffeeType.CAPPUCCINO: Cappuccino,
    }

    def create_coffee(self, coffee_type: CoffeeType):

        coffee_class = self._coffee_map.get(coffee_type)

        if coffee_class is None:
            raise ValueError(f"Unknown coffee type: {coffee_type}")

        return coffee_class()