class Product:
    def __init__(self, product_id, name, price, daily_demand=0):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.daily_demand = daily_demand

class Factory:
    @staticmethod
    def create_product(product_id, name, price, daily_demand=0):
        return Product(product_id, name, price, daily_demand)


