from product import Factory
from DarkStore import DarkStoreManager
from FillProduct import FillProductWeekly
from Cart import Cart
from DeliveryService import DeliveryService, DeliveryPartner
from OrderService import OrderService
from Observer import SMSNotifier, EmailNotifier, AutoRefillHandler

# --- Setup ---

# dark store manager
manager = DarkStoreManager()

# create observers
sms = SMSNotifier()
email = EmailNotifier()
auto_refill = AutoRefillHandler()

# create a store at (0, 0) with weekly fill strategy + observers attached
store = manager.add_dark_store(
    x=0, y=0,
    fill_strategy=FillProductWeekly(),
    observers=[sms, email, auto_refill]
)

# create products
milk = Factory.create_product("P001", "Milk", 50, daily_demand=10)
bread = Factory.create_product("P002", "Bread", 40, daily_demand=5)

# add products to store (bread ka stock low rakha hai — observer trigger hoga)
manager.add_product_to_store(store, milk, 100)
manager.add_product_to_store(store, bread, 12)

print("=== Inventory after stocking ===")
print(store.inventory_manager.get_inventory())

# --- Order Flow ---

# cart
cart = Cart(2, 3)
cart.add_item(milk, 2)
cart.add_item(bread, 3)

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

# --- State Pattern Demo ---
print("\n=== State Transitions ===")

# PLACED → CONFIRMED
order.confirm()
print(order)

# CONFIRMED → DISPATCHED
order.dispatch()
print(order)

# DISPATCHED → cancel nahi hoga!
order.cancel()

# DISPATCHED → DELIVERED
order.deliver()
print(order)

# DELIVERED → ab kuch nahi hoga
order.cancel()
order.confirm()

