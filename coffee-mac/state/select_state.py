from state.vending_machine_state import VendingMachineState

class SelectState(VendingMachineState):
    
    def insert_coin(self, amount):
        print("please select a product first.")
    
    def select_product(self, name):
        if self.vending_machine.is_product_available(name):
            print(f"Product {name} selected. Dispensing product...")
            #self.vending_machine.dispense_product(name)
            recipe = self.vending_machine.recipe_manager.find_recipe_by_name(name)
            if recipe:
                if self.vending_machine.inventory.check_ingredient_availability(recipe):
                    print("All ingredients available. Dispensing product...")
                    #self.vending_machine.dispense_product(name)
                    self.vending_machine.set_state(self.vending_machine.insert_coin_state)
                else:
                    print("Not enough ingredients available.")
                    self.vending_machine.set_state(self.vending_machine.no_ingredients_state)
            else:
                print(f"Recipe for {name} not found.")
                self.vending_machine.set_state(self.vending_machine.no_ingredients_state)

        else:
            print(f"Product {name} is not available. Please select another product.")
            self.vending_machine.set_state(self.vending_machine.no_ingredients_state)

    def dispense_product(self):
        print("please select a product first.")

    def return_money(self):
        print("please select a product first.")

    def no_ingredients(self):
        print("please select a product first.")