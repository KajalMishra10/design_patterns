from enums.ingredient_type import IngredientType
from dataclasses import dataclass

@dataclass(frozen=True)
class Ingredient:
    def __init__(self, name: IngredientType):
        self.name = name

@dataclass(frozen=True)
class RecipeIngredient:
    def __init__(self, ingredient: Ingredient, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.ingredient = ingredient
        self.quantity = quantity

class InventoryIngredient:
    def __init__(self, ingredient: Ingredient, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        self.ingredient = ingredient
        self.quantity = quantity