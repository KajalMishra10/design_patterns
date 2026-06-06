from inventory import Inventory
from coin import Coin
from item import Item
from states import VendingMachineState, IdleState


class VendingMachine:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False

        return cls._instance

    @classmethod
    def get_instance(cls) -> "VendingMachine":
        return cls()

    def __init__(self):
        if self._initialized:
            return

        self.inventory = Inventory()
        self.current_state = IdleState(self)
        self.balance = 0
        self.selected_item_code = None

        self._initialized = True
        
    def get_inventory(self) -> Inventory:
        return self.inventory

    def set_state(self, state: VendingMachineState):
        self.current_state = state

    def set_selected_item_code(self, code: str):
        self.selected_item_code = code

    def get_current_amount(self) -> int:
        return self.balance

    def add_to_current_amount(self, amount: int):
        self.balance += amount

    def get_selected_item(self) -> Item:
        return self.inventory.get_item(self.selected_item_code)

    def insert_coin(self, coin: Coin):
        self.current_state.insert_coin(coin)

    def select_item(self, code: str):
        self.current_state.select_item(code)

    def dispense(self):
        self.current_state.dispense()

    def refund(self):
        self.current_state.refund()

    def add_item(self, item: Item, quantity: int):
        self.inventory.add_item(item, quantity)
        return item
    
    def dispense_item(self) -> None:
        item = self.inventory.get_item(self.selected_item_code)
        if self.balance >= item.get_price():
            self.inventory.reduce_stock(self.selected_item_code)
            self.balance -= item.get_price()
            print(f"Dispensed: {item.get_name()}")
            if self.balance > 0:
                print(f"Returning change: {self.balance}")
        self.reset()
        self.set_state(IdleState(self))

    def reset(self) -> None:
        self.selected_item_code = None
        self.balance = 0

    
