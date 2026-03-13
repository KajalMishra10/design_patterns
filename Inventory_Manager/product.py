class Product:
    def __init__(self, name, price, daily_demand=1):
        self.name = name
        self.price = price
        self.daily_demand = daily_demand  # kitne units per day bikte hain


class Factory:
    @staticmethod
    def create_product(name, price, daily_demand=1):
        return Product(name, price, daily_demand)
    

