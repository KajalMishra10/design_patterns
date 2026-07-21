from enum import Enum

class IngredientType(str, Enum):
    WATER = "water"
    MILK = "milk"
    COFFEE = "coffee"
    SUGAR = "sugar"