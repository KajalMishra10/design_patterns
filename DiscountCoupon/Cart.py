
from CartItem import CartItem


class Cart:
    def __init__(self):
        self.items = []
        self.finalTotal = 0

    def add_item(self, product, quantity):
        cart_item = CartItem(product, quantity)
        self.items.append(cart_item)

    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items)

    def apply_discount(self, discount_amount):
        if self.finalTotal == 0:
            self.finalTotal = self.get_total_price()
        self.finalTotal -= discount_amount

    def __str__(self):
        cart_details = "\n".join(str(item) for item in self.items)
        total_price = self.get_total_price()
        final = self.finalTotal if self.finalTotal > 0 else total_price
        return f"Cart Items:\n{cart_details}\nTotal Price: ${total_price:.2f}\nFinal Total: ${final:.2f}"