from Observer import Subject


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        pass
    def remove_item(self, product, quantity):
        pass

    def get_inventory(self):
        pass


class DBInventory(Inventory):
    def __init__(self, db_connection):
        super().__init__()
        self.db_connection = db_connection

    def add_item(self, product, quantity):
        # Code to add item to the database
        print(f"Adding {quantity} of {product.name} to database")

        if product.product_id not in self.items:
            self.items[product.product_id] = {"product": product, "quantity": 0}

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
    

class InventoryManager(Subject):
    LOW_STOCK_THRESHOLD = 10

    def __init__(self, inventory, dark_store=None):
        super().__init__()  # Subject ka __init__ — observers list ready
        self.inventory = inventory
        self.dark_store = dark_store  # for passing store info in alerts

    def add_product(self, product, quantity):
        self.inventory.add_item(product, quantity)

    def remove_product(self, product, quantity):
        self.inventory.remove_item(product, quantity)
        self._check_low_stock(product)

    def get_inventory(self):
        return self.inventory.get_inventory()

    def has_product(self, product, quantity):
        inventory = self.get_inventory()
        if product.product_id in inventory and inventory[product.product_id]["quantity"] >= quantity:
            return True
        return False

    def _check_low_stock(self, product):
        """Stock remove hone ke baad check karo — low hai toh observers ko batao"""
        inventory = self.inventory.items
        if product.product_id in inventory:
            qty = inventory[product.product_id]["quantity"]
            if qty <= self.LOW_STOCK_THRESHOLD:
                self.notify_observers("LOW_STOCK", {
                    "product": product,
                    "product_name": product.name,
                    "quantity": qty,
                    "store": self.dark_store,
                })

class InventoryManagerFactory:
    @staticmethod
    def create(db_connection=None, dark_store=None):
        inventory = DBInventory(db_connection)
        return InventoryManager(inventory, dark_store)