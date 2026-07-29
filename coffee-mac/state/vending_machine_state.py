from abc import ABC, abstractmethod

class VendingMachineState(ABC):

    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    @abstractmethod
    def insert_coin(self, amount):
        pass

    @abstractmethod
    def select_product(self, name, addons=None):
        pass

    @abstractmethod
    def dispense_product(self):
        pass