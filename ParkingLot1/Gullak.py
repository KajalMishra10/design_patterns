class Gullak:
    def __init__(self):
        self.balance = 0

    def add_amount(self, amount):
        self.balance += amount
        print(f"Added {amount} to Gullak. Current balance: {self.balance}")

    def get_balance(self):
        return self.balance