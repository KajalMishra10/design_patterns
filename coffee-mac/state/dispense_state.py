from state.vending_machine_state import VendingMachineState
from state.select_state import SelectState


class DispenseState(VendingMachineState):

    def insert_coin(self, amount):
        print("Please wait, already dispensing your coffee.")

    def select_product(self, name, addons=None):
        print("Please wait, already dispensing your coffee.")

    def dispense_product(self):
        vending_machine = self.vending_machine
        recipe = vending_machine.get_recipe(vending_machine.selected_product)
        
        vending_machine.deduct_ingredients(recipe)

        coffee = vending_machine.build_coffee()
        change = vending_machine.balance - coffee.get_cost()

        print(f"Dispensing: {coffee.get_description()} (Cost: {coffee.get_cost()})")
        if change > 0:
            print(f"Please collect your change: {change}")

        vending_machine.reset_selection()
        vending_machine.set_state(SelectState(vending_machine))
        return coffee
