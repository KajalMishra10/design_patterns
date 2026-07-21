from recipe.ingredient import Ingredient, InventoryIngredient


class Inventory:
    def __init__(self):
        self.ingredients: dict[Ingredient, InventoryIngredient] = {}

    def add_ingredient(self, ingredient: Ingredient, quantity: int):
        if ingredient in self.ingredients:
            self.ingredients[ingredient].quantity += quantity
        else:
            self.ingredients[ingredient] = InventoryIngredient(
                ingredient, quantity
            )

    def remove_ingredient(self, ingredient: Ingredient, quantity: int):
        if ingredient not in self.ingredients:
            raise ValueError(f"{ingredient.name.value} not found in inventory.")

        inventory_ingredient = self.ingredients[ingredient]

        if inventory_ingredient.quantity < quantity:
            raise ValueError(f"Not enough {ingredient.name.value} in inventory.")

        inventory_ingredient.quantity -= quantity

        if inventory_ingredient.quantity == 0:
            del self.ingredients[ingredient]

    def get_quantity(self, ingredient: Ingredient) -> int:
        if ingredient not in self.ingredients:
            return 0

        return self.ingredients[ingredient].quantity