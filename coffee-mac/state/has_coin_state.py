from state.vending_machine_state import VendingMachineState

class insert_coin_state(VendingMachineState):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self, amount):
        self.vending_machine.balance=self.vending_machine.balance+amount
         

    def select_product(self, name):
        print("product already selected please insert money now")

    def dispense_product(self):
            print("please insert money first.")