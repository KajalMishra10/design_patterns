
from coffee.coffee import Espresso
from coffee.coffee import Cappuccino

class CoffeeFactory:
    def create_coffee(self, coffee_type):
        if coffee_type == "espresso":
            return Espresso()
        elif coffee_type == "cappuccino":
            return Cappuccino()
        else:
            raise ValueError(f"Unknown coffee type: {coffee_type}") 