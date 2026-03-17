from product import Factory
from DarkStore import DarkStoreManager
from FillProduct import FillProductWeekly, FillService
from Cart import Cart
from DeliveryService import DeliveryService, DeliveryPartner
from OrderService import OrderService

# --- Setup ---

# dark store manager
manager = DarkStoreManager()

# create a store at (0, 0) with weekly fill strategy
store = manager.add_dark_store(x=0, y=0, fill_strategy=FillProductWeekly())

# create products
milk = Factory.create_product("P001", "Milk", 50, daily_demand=10)
bread = Factory.create_product("P002", "Bread", 40, daily_demand=5)

# add products to store
manager.add_product_to_store(store, milk, 100, fill_interval_days=7)
manager.add_product_to_store(store, bread, 50, fill_interval_days=7)

print("=== Inventory after stocking ===")
print(store.inventory_manager.get_inventory())

# --- Order Flow ---

# cart
cart = Cart(2, 3)
cart.add_item(milk, 2)
cart.add_item(bread, 1)

# delivery partners
partners = [DeliveryPartner("Raju"), DeliveryPartner("Shyam")]
delivery_service = DeliveryService(partners)

# order service
order_service = OrderService(manager, delivery_service)

# checkout
order = order_service.create_order(2, 3, cart.get_items())
print("\n=== Order Result ===")
print(order)

print("\n=== Inventory after order ===")
print(store.inventory_manager.get_inventory())

# --- Fill Service Demo ---
print("\n=== Refill via FillService ===")
fill_service = FillService()
fill_service.refill_all(milk, manager)

print("\n=== Inventory after refill ===")
print(store.inventory_manager.get_inventory())
