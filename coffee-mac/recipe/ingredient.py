from enums.ingredient_type import IngredientType

class Ingredient:
    def __init__(self, name: IngredientType):
        self.name = name


class RecipeIngredient:
    def __init__(self, ingredient: Ingredient, quantity: int):
        self.ingredient = ingredient
        self.quantity = quantity


class InventoryIngredient:
    def __init__(self, ingredient: Ingredient, quantity: int):
        self.ingredient = ingredient
        self.quantity = quantity