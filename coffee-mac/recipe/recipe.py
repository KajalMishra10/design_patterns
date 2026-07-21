from enums.coffee_type import CoffeeType
from recipe.ingredient import RecipeIngredient 

class Recipe:
    def __init__(self, coffee: CoffeeType, ingredients: list[RecipeIngredient]):
        self.coffee = coffee
        self.ingredients = ingredients

    def display_recipe(self):
        print(f"Recipe: {self.coffee.value}")
        print("Ingredients:")

        for recipe_ingredient in self.ingredients:
            print(
                f"{recipe_ingredient.ingredient.name.value}: "
                f"{recipe_ingredient.quantity}"
            )