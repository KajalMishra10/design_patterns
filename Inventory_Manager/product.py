class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

class Factory:
    @staticmethod
    def create_product(product_id, name, price):
        return Product(product_id, name, price)


