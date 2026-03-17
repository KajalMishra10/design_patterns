class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class Cart:
    def __init__(self, user_x, user_y):
        self.user_x = user_x
        self.user_y = user_y
        self.items = []

    def add_item(self, product, quantity):
        self.items.append(CartItem(product, quantity))

    def get_items(self):
        return self.items