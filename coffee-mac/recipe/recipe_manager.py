
from enums.coffee_type import CoffeeType

class RecipeManager:
    
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def get_recipes(self):
        return self.recipes

    def find_recipe_by_name(self, coffee_type: CoffeeType):
        for recipe in self.recipes:
            if recipe.coffee == coffee_type:
                return recipe
        return None 