class FillProduct:
    """Base strategy for filling products in inventory"""
    def fill(self, product, dark_store):
        pass


class FillProductWeekly(FillProduct):
    """Weekly fill — 7 din ki demand ke hisaab se stock bharo"""
    def fill(self, product, dark_store):
        quantity = product.daily_demand * 7
        print(f"Weekly fill: {product.name} -> {quantity} units")
        dark_store.add_product_to_store(product, quantity)


class FillProductMonthly(FillProduct):
    """Monthly fill — 30 din ka stock ek baar mein bharo (bulk)"""
    def fill(self, product, dark_store):
        quantity = product.daily_demand * 30
        print(f"Monthly fill: {product.name} -> {quantity} units")
        dark_store.add_product_to_store(product, quantity)