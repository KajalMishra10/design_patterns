
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity, fill_interval_days):
        pass
    def remove_item(self, product, quantity):
        pass

    def get_inventory(self):
        pass


class DBInventory(Inventory):
    def __init__(self, db_connection):
        super().__init__()
        self.db_connection = db_connection

    def add_item(self, product, quantity,fill_interval_days):
        # Code to add item to the database
        print(f"Adding {quantity} of {product.name} to database")

        if product.product_id not in self.items:
            self.items[product.product_id] = {"product": product, "quantity": 0, "fill_interval_days": fill_interval_days}

        self.items[product.product_id]["quantity"] += quantity
        
    def remove_item(self, product, quantity):
        # Code to remove item from the database
        if product.product_id not in self.items:
            print(f"{product.name} not found in inventory.")
            return
        if self.items[product.product_id]["quantity"] < quantity:
            print(f"Not enough stock for {product.name}. Available: {self.items[product.product_id]['quantity']}, Requested: {quantity}")
            return
        print(f"Removing {quantity} of {product.name} from the database.")
        self.items[product.product_id]["quantity"] -= quantity
        if self.items[product.product_id]["quantity"] == 0:
            del self.items[product.product_id]

    def get_inventory(self):
        # Code to retrieve inventory from the database
        print("Retrieving inventory from the database.")
        return self.items  
    

class InventoryManager:
    def __init__(self, inventory):
        self.inventory = inventory

    def add_product(self, product, quantity, fill_interval_days):
        self.inventory.add_item(product, quantity, fill_interval_days)

    def remove_product(self, product, quantity):
        self.inventory.remove_item(product, quantity)

    def get_inventory(self):
        return self.inventory.get_inventory()
