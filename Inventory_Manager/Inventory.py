class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        pass
    def remove_item(self, item_name, quantity):
        pass

    def get_inventory(self):
        pass


class DBInventory(Inventory):
    def __init__(self, db_connection):
        super().__init__()
        self.db_connection = db_connection

    def add_item(self, item_name, quantity):
        # Code to add item to the database
        print(f"Adding {quantity} of {item_name} to the database.") 
        self.items[item_name] = self.items.get(item_name, 0) + quantity

    def remove_item(self, item_name, quantity):
        # Code to remove item from the database
        if item_name not in self.items:
            print(f"{item_name} not found in inventory.")
            return
        if self.items[item_name] < quantity:
            print(f"Not enough stock for {item_name}. Available: {self.items[item_name]}, Requested: {quantity}")
            return
        print(f"Removing {quantity} of {item_name} from the database.")
        self.items[item_name] -= quantity
        if self.items[item_name] == 0:
            del self.items[item_name]

    def get_inventory(self):
        # Code to retrieve inventory from the database
        print("Retrieving inventory from the database.")
        return self.items  
    

class InventoryManager:
    def __init__(self, inventory):
        self.inventory = inventory

    def add_product(self, product, quantity):
        self.inventory.add_item(product.name, quantity)

    def remove_product(self, product, quantity):
        self.inventory.remove_item(product.name, quantity)

    def get_inventory(self):
        return self.inventory.get_inventory()
