from state.vending_machine_state import VendingMachineState
from state.dispense_state import DispenseState

class HasCoinState(VendingMachineState):

    def insert_coin(self, amount):
        self.vending_machine.balance = self.vending_machine.balance + amount
        if self.vending_machine.isSufficient():
            self.vending_machine.set_state(DispenseState(self.vending_machine))
        else:
            remaining = self.vending_machine.get_remaining_amount()
            print(f"Balance: {self.vending_machine.balance}. Insert {remaining} more.")

    def select_product(self, name):
        print("Product already selected, please insert money now.")

    def dispense_product(self):
        print("Insufficient balance, please insert money first.")