from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from coin import Coin

if TYPE_CHECKING:
    from .vending_machine import VendingMachine


class VendingMachineState(ABC):
    """Abstract base class for all vending machine states."""
    
    def __init__(self, machine: 'VendingMachine'):
        self.machine = machine
    
    @abstractmethod
    def insert_coin(self, coin: Coin):
        """Handle coin insertion."""
        pass
    
    @abstractmethod
    def select_item(self, code: str):
        """Handle item selection."""
        pass
    
    @abstractmethod
    def dispense(self):
        """Handle dispense request."""
        pass

    @abstractmethod
    def refund(self):
        """Handle refund request."""
        pass

class IdleState(VendingMachineState):
    """State when the machine is idle, waiting for user interaction."""
    
    def insert_coin(self, coin: Coin):
        print("Please select an item before inserting money.")
    
    def select_item(self, code: str):
        if not self.machine.get_inventory().is_available(code):
            print("Item not available.")
            return
        
        self.machine.set_selected_item_code(code)
        # Import here to avoid circular dependency
        from states import ItemSelectedState
        self.machine.set_state(ItemSelectedState(self.machine))
        print(f"Item selected: {code}")
    
    def dispense(self):
        print("Please insert coins and select an item before dispensing.")
    
    def refund(self):
        print("No coins to refund.")



class ItemSelectedState(VendingMachineState):
    """State when an item has been selected, waiting for coins."""
    
    def insert_coin(self, coin: Coin):
        self.machine.add_to_current_amount(coin.get_value())
        if self.machine.get_current_amount() >= self.machine.get_selected_item().get_price():
            # Import here to avoid circular dependency
            from states import HasMoneyState
            self.machine.set_state(HasMoneyState(self.machine))
        print(f"Inserted {coin.name}. Current amount: {self.machine.get_current_amount()} cents.")
    
    def select_item(self, code: str):
        print("Item already selected. Please insert coins or cancel.")
    
    def dispense(self):
        print("Please insert coins before dispensing.")
    
    def refund(self):
        print("Please insert coins before requesting a refund.")

class HasMoneyState(VendingMachineState):
    """State when enough money has been inserted, ready to dispense."""
    
    def insert_coin(self, coin: Coin):
        print("Already have enough money. ")
        self.machine.add_to_current_amount(coin.get_value())
        print(f"Inserted {coin.name}. Current amount: {self.machine.get_current_amount()} cents.")
    
    def select_item(self, code: str):
        print("Already have enough money. Please select an item or dispense.")
    
    def dispense(self):
        # Transition to the dispensing state and let it perform the dispense.
        from states import DispensingState
        self.machine.set_state(DispensingState(self.machine))
        self.machine.dispense()
        self.machine.dispense_item()

    def refund(self):
        print(f"Refunding: {self.machine.get_current_amount()} cents.")
        self.machine.reset()
        # Import here to avoid circular dependency
        from states import IdleState
        self.machine.set_state(IdleState(self.machine))

class DispensingState(VendingMachineState):
    """State when the machine is dispensing an item."""
    
    def insert_coin(self, coin: Coin):
        print("Currently dispensing. Please wait.")
    
    def select_item(self, code: str):
        print("Currently dispensing. Please wait.")
    
    def dispense(self):
        print("Dispensing item...")
        # dispense_item handles stock, change, reset, and the transition to Idle.
       
    
    def refund(self):
        print("Cannot refund while dispensing.")