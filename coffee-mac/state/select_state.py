from state.vending_machine_state import VendingMachineState
from state.has_coin_state import insert_coin_state
class SelectState(VendingMachineState):
    
    def insert_coin(self, amount):
        print("please select a product first.")
    
    def select_product(self, name):
        if self.vending_machine.is_product_available(name):
            recipe = self.vending_machine.get_recipe(name)
            if recipe:
                if self.vending_machine.check_ingredient_availability(recipe):
                    self.vending_machine.selected_product = name
                    self.vending_machine.set_state(insert_coin_state(self.vending_machine))
                else:
                    print("Not enough ingredients available.")
                    return
            else:
                print(f"Recipe for {name} not found.")
                return

        else:
            print(f"Product {name} is not available. Please select another product.")
            return
    def dispense_product(self):
        print("please select a product first.")

    def return_money(self):
        print("please select a product first.")

    def no_ingredients(self):
        print("please select a product first.")