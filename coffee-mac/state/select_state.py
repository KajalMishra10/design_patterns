from state.vending_machine_state import VendingMachineState
from state.has_coin_state import HasCoinState

class SelectState(VendingMachineState):

    def insert_coin(self, amount):
        print("Please select a product first.")

    def select_product(self, name, addons=None):
        valid = self.vending_machine.validate_product(name)
        if valid:
            self.vending_machine.selected_product = name
            self.vending_machine.selected_addons = addons or []
            self.vending_machine.set_state(HasCoinState(self.vending_machine))

    def dispense_product(self):
        print("Please select a product first.")