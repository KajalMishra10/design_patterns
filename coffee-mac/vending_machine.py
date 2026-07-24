
from enums.coffee_type import CoffeeType
from recipe.recipe_manager import RecipeManager
from Inventary.inventary import Inventory
from state.select_state import SelectState

class VendingMachine:
    def __init__(self):
        self.items = {}
        self.balance = 0
        self.recipe_manager = RecipeManager()
        self.inventory_manager=Inventory()
        self.current_state=SelectState(self)

    def add_new_coffee(self, item_name, price, quantity):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            if item_name in [coffee.value for coffee in CoffeeType]:
                self.items[item_name] = {"price": price,
                                        "quantity": quantity}
            else:
                raise ValueError("Invalid coffee type")
    def get_recipe(self, coffee_type: CoffeeType):
        return self.recipe_manager.find_recipe_by_name(coffee_type)

    def check_ingredient_availability(self, recipe):
        return self.inventory_manager.check_ingredient_availability(recipe)

    def insert_money(self, amount):
        pass
     
    def select_item(self, item_name):
        pass
    
    def refund(self):
        refunded_amount = self.balance
        self.balance = 0
        return f"Refunded: {refunded_amount}"