class DiscountStrategy:
    def apply_discount(self, total_amount):
        pass

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, total_amount):
        return total_amount * (self.percentage / 100)
    
class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount):
        self.amount = amount

    def apply_discount(self, total_amount):
        return self.amount
    
