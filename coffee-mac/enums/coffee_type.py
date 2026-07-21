from enum import Enum

class CoffeeType(str, Enum):
    ESPRESSO = "Espresso"
    CAPPUCCINO = "Cappuccino"
    LATTE = "Latte"