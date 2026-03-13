class FillProduct:
    """Base strategy for filling products in inventory"""
    def fill(self, product, inventory):
        pass


class FillProductWeekly(FillProduct):
    """Weekly fill — 7 din ki demand ke hisaab se stock bharo"""
    def fill(self, product, inventory):
        quantity = product.daily_demand * 7
        print(f"Weekly fill: {product.name} -> {quantity} units")
        inventory.add_item(product.name, quantity)


class FillProductMonthly(FillProduct):
    """Monthly fill — 30 din ka stock ek baar mein bharo (bulk)"""
    def fill(self, product, inventory):
        quantity = product.daily_demand * 30
        print(f"Monthly fill: {product.name} -> {quantity} units")
        inventory.add_item(product.name, quantity)


class FillProductThreshold(FillProduct):
    """Threshold fill — jab stock minimum se neeche ho tab hi bharo"""
    def __init__(self, min_threshold=10, restock_days=7):
        self.min_threshold = min_threshold
        self.restock_days = restock_days

    def fill(self, product, inventory):
        current_stock = inventory.get_inventory().get(product.name, 0)
        if current_stock < self.min_threshold:
            quantity = product.daily_demand * self.restock_days
            print(f"Threshold fill: {product.name} stock low ({current_stock}), adding {quantity} units")
            inventory.add_item(product.name, quantity)
        else:
            print(f"Threshold fill: {product.name} stock sufficient ({current_stock}), no fill needed")
