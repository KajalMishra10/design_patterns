class DarkStore:
    def __init__(self, inventory_manager, fill_strategy=None, x=0, y=0):
        self.inventory_manager = inventory_manager
        self.fill_strategy = fill_strategy
        self.x = x
        self.y = y

    def add_product_to_store(self, product, quantity):
        self.inventory_manager.add_product(product, quantity)

    def remove_product_from_store(self, product, quantity):
        self.inventory_manager.remove_product(product, quantity)

    def get_store_inventory(self):
        return self.inventory_manager.get_inventory()

    def set_fill_strategy(self, fill_strategy):
        """Runtime pe strategy change karo"""
        self.fill_strategy = fill_strategy

    def fill_product(self, product):
        """Current strategy se product bharo"""
        if self.fill_strategy:
            self.fill_strategy.fill(product, self.inventory_manager.inventory)
        else:
            print("No fill strategy set!")
    
    def location(self, x, y):
        # Code to determine the location of the dark store
        self.x = x
        self.y = y
        print(f"The dark store is located at coordinates ({x}, {y}).")

    def delivery_time(self, customer_x, customer_y):
        # Code to calculate delivery time based on distance
        distance = ((customer_x - self.x) ** 2 + (customer_y - self.y) ** 2) ** 0.5
        if distance < 5:
            return "15 minutes"
        elif distance < 10:
            return "30 minutes"
        else:
            return "45 minutes or more"
        

class DarkStoreManager:
    def __init__(self, dark_store):
        self.dark_store = dark_store

    def manage_inventory(self, product, quantity):
        self.dark_store.add_product_to_store(product, quantity)

    def manage_location(self, x, y):
        self.dark_store.location(x, y)

    def manage_delivery_time(self, customer_x, customer_y):
        return self.dark_store.delivery_time(customer_x, customer_y)
    

