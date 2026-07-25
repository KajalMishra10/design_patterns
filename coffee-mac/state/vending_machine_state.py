class VendingMachineState:
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self, amount):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def select_product(self, name):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def dispense_product(self):
        raise NotImplementedError("This method should be overridden in subclasses.")