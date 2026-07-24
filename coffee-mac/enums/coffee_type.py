from enum import Enum

class CoffeeType(str, Enum):
    ESPRESSO = "espresso"
    CAPPUCCINO = "cappuccino"
    LATTE = "latte"