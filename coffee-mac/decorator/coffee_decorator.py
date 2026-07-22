class CoffeeDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def get_cost(self):
        return self._coffee.get_cost()

    def get_description(self):
        return self._coffee.get_description()
    
class ExtraSugar(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self):
        return self._coffee.get_cost() + 5

    def get_description(self):
        return f"{self._coffee.get_description()}, Extra Sugar"
    
class ExtraMilk(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self):
        return self._coffee.get_cost() + 10

    def get_description(self):
        return f"{self._coffee.get_description()}, Extra Milk"