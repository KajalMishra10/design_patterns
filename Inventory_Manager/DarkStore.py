from Inventory import InventoryManagerFactory


class DarkStore:
    def __init__(self, inventory_manager, fill_strategy=None, x=0, y=0):
        self.inventory_manager = inventory_manager
        self.x = x
        self.y = y
        self.fill_strategy = fill_strategy

    def add_product_to_store(self, product, quantity, fill_interval_days):
        self.inventory_manager.add_product(product, quantity, fill_interval_days)

    def remove_product_from_store(self, product, quantity):
        self.inventory_manager.remove_product(product, quantity)
    
    def has_product(self, product, quantity):
        return self.inventory_manager.has_product(product, quantity)

    
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
    def __init__(self):
        # multiple stores manage karega
        self.dark_stores = []

    # ✅ 1. Create new store (Admin side)
    def add_dark_store(self, x, y,fill_strategy=None):
        inventory_manager = InventoryManagerFactory.create()
        store = DarkStore(inventory_manager, fill_strategy, x, y)
        self.dark_stores.append(store)
        return store

    # ✅ 2. Remove store
    def remove_dark_store(self, store):
        if store in self.dark_stores:
            self.dark_stores.remove(store)

    # ✅ 3. Get all stores
    def get_all_stores(self):
        return self.dark_stores

    # ✅ 4. Find nearest store (IMPORTANT 🔥)
    def find_nearest_store(self, user_x, user_y):
        if not self.dark_stores:
            return None

        return min(
            self.dark_stores,
            key=lambda store: ((store.x - user_x) ** 2 + (store.y - user_y) ** 2)
        )

    # ✅ 5. Add product to specific store
    def add_product_to_store(self, store, product, quantity, fill_interval_days):
        store.add_product_to_store(product, quantity, fill_interval_days)

    def remove_product_from_store(self, store, product, quantity):
        store.remove_product_from_store(product, quantity)

    