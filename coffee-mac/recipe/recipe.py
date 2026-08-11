from dataclasses import dataclass

from enums.coffee_type import CoffeeType
from recipe.ingredient import RecipeIngredient


@dataclass(frozen=True)
class Recipe:
    coffee: CoffeeType
    ingredients: tuple[RecipeIngredient, ...]

    def __post_init__(self):
        if not self.ingredients:
            raise ValueError("Recipe must contain at least one ingredient.")