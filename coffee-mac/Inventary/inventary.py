from enums.ingredient_type import IngredientType
from recipe.ingredient import Ingredient, InventoryIngredient
from recipe.recipe import Recipe


class Inventory:
    def __init__(self):
        self.ingredients: dict[IngredientType, InventoryIngredient] = {}

    def add_ingredient(self, ingredient: IngredientType, quantity: int):
        if ingredient in self.ingredients:
            self.ingredients[ingredient].quantity += quantity
        else:
            ingredient_obj = Ingredient(ingredient)
            self.ingredients[ingredient] = InventoryIngredient(
                ingredient_obj, quantity
            )

    def remove_ingredient(self, ingredient: IngredientType, quantity: int):
        if ingredient not in self.ingredients:
            raise ValueError(f"{ingredient.value} not found in inventory.")

        inventory_ingredient = self.ingredients[ingredient]

        if inventory_ingredient.quantity < quantity:
            raise ValueError(f"Not enough {ingredient.value} in inventory.")

        inventory_ingredient.quantity -= quantity

        if inventory_ingredient.quantity == 0:
            del self.ingredients[ingredient]

    def get_quantity(self, ingredient: IngredientType) -> int:
        if ingredient not in self.ingredients:
            return 0

        return self.ingredients[ingredient].quantity
    
    def check_ingredient_availability(self, recipe: Recipe) -> bool:
        for recipe_ingredient in recipe.ingredients:
            ingredient = recipe_ingredient.ingredient.name
            required_quantity = recipe_ingredient.quantity

            if ingredient not in self.ingredients:
                return False

            inventory_ingredient = self.ingredients[ingredient]
            if inventory_ingredient.quantity < required_quantity:
                return False

        return True