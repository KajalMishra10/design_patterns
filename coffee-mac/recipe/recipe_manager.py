
from enums.coffee_type import CoffeeType

class RecipeManager:
    
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, recipe):
        self.recipes[recipe.coffee]=recipe

    def get_recipes(self):
        return list(self.recipes.values())

    def find_recipe_by_name(self, coffee_type: CoffeeType):
        return self.recipes.get(coffee_type)