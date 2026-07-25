from state.vending_machine_state import VendingMachineState
from state.has_coin_state import insert_coin_state
class SelectState(VendingMachineState):
    
    def insert_coin(self, amount):
        print("please select a product first.")
    
    def select_product(self, name):
        valid=self.vending_machine.validate_product(name)
        if valid==True:
            self.vending_machine.selected_product = name
            self.vending_machine.set_state(insert_coin_state(self.vending_machine))
        
    def dispense_product(self):
        print("please select a product first.")

   