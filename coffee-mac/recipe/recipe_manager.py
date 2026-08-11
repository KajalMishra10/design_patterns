from recipe.recipe import Recipe
from enums.coffee_type import CoffeeType


class RecipeManager:

    def __init__(self):
        self._recipes: dict[CoffeeType, Recipe] = {}

    def add_recipe(self, recipe: Recipe) -> None:
        self._recipes[recipe.coffee] = recipe

    def get_recipe(self, coffee_type: CoffeeType) -> Recipe:
        if coffee_type not in self._recipes:
            raise ValueError(
                f"Recipe for {coffee_type.value} not found."
            )

        return self._recipes[coffee_type]

    def get_all_recipes(self) -> list[Recipe]:
        return list(self._recipes.values())