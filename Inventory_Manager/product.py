class Product:
    def __init__(self, name, price, daily_demand=1, fill_strategy=None, fill_interval_days=1):
        self.name = name
        self.price = price
        self.daily_demand = daily_demand
        self.fill_strategy = fill_strategy
        self.fill_interval_days = fill_interval_days

class Factory:
    @staticmethod
    def create_product(name, price, daily_demand=1, fill_strategy=None, fill_interval_days=1):
        return Product(name, price, daily_demand, fill_strategy, fill_interval_days)


