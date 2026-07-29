from enums.coffee_type import CoffeeType
from recipe.recipe_manager import RecipeManager
from Inventary.inventary import Inventory
from state.select_state import SelectState
from addon.addon_manager import AddonManager
from addon.addon import Addon

class VendingMachine:
    def __init__(self):
        self.items = {}
        self.balance = 0
        self.recipe_manager = RecipeManager()
        self.inventory_manager = Inventory()
        self.addon_manager = AddonManager()
        self.current_state = SelectState(self)
        self.selected_product = None
        self.selected_addons = []
        

    def add_new_coffee(self, item_name, price, recipe):
        if item_name in self.items:
            self.recipe_manager.add_recipe(recipe)
            self.items[item_name]={"price": price}
        else:
            if item_name in [coffee.value for coffee in CoffeeType]:
                self.items[item_name] = {"price": price}
                self.recipe_manager.add_recipe(recipe)
                                        
            else:
                raise ValueError("Invalid coffee type")       
         
    def get_recipe(self, coffee_type: CoffeeType):
        return self.recipe_manager.find_recipe_by_name(coffee_type)

    def check_ingredient_availability(self, recipe):
        return self.inventory_manager.check_ingredient_availability(recipe)

    def is_product_available(self, item_name):
        return item_name in self.items 

    def validate_product(self,name):
        if self.is_product_available(name):
            recipe=self.get_recipe(name)
            if recipe:
                check=self.check_ingredient_availability(recipe)
                if check==False:
                    print("Not enough ingredients available.")
                    return False
                else: 
                    return True
            else:
                print(f"Recipe for {name} not found.")
                return False
        else:
            print(f"Product {name} is not available. Please select another product.")
            return False

    def validate_addons(self, addons):
        return self.addon_manager.validate_addons(addons)
    
    def get_total_price(self):
        product_price = self.items[self.selected_product]["price"]
        addon_price = self.addon_manager.get_total_addon_price(self.selected_addons)
        return product_price + addon_price

    def isSufficient(self):
        return self.balance >= self.get_total_price()

    def get_remaining_amount(self):
        return self.get_total_price() - self.balance
  
    def set_state(self, state):
        self.current_state=state

    def insert_money(self, amount):
        pass
     
    def select_item(self, item_name):
        pass

    def refund(self):
        refunded_amount = self.balance
        self.balance = 0
        return f"Refunded: {refunded_amount}"