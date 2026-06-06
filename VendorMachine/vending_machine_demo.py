from vending_machine import VendingMachine
from coin import Coin
from item import Item
from states import IdleState, ItemSelectedState

class VendingMachineDemo:
    @staticmethod
    def main():
        vending_machine = VendingMachine.get_instance()
        # Add items to the vending machine
        vending_machine.add_item(Item("A1", "Soda", 150), 10)
        vending_machine.add_item(Item("B1", "Chips", 100), 5)   
        # Simulate user interactions
        vending_machine.select_item("A1")
        vending_machine.insert_coin(Coin.QUARTER)
        vending_machine.insert_coin(Coin.QUARTER)
        vending_machine.insert_coin(Coin.QUARTER)
        vending_machine.insert_coin(Coin.QUARTER)
        vending_machine.dispense()
        vending_machine.select_item("B1")
        vending_machine.insert_coin(Coin.QUARTER)
        vending_machine.insert_coin(Coin.QUARTER)
        vending_machine.insert_coin(Coin.QUARTER)
        vending_machine.insert_coin(Coin.QUARTER)
        vending_machine.dispense()
if __name__ == "__main__":    
    VendingMachineDemo.main()