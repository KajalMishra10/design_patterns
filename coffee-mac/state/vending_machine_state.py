class VendingMachineState:
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine

    def insert_coin(self, amount):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def select_product(self, product_code):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def dispense_product(self):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def return_money(self):
        raise NotImplementedError("This method should be overridden in subclasses.")
    
    def no_ingredients(self):
        raise NotImplementedError("This method should be overridden in subclasses.")



