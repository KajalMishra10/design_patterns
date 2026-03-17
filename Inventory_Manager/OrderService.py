class Order:
    def __init__(self, user_location, items, store, delivery_partner):
        self.user_location = user_location
        self.items = items
        self.store = store
        self.delivery_partner = delivery_partner

    def __repr__(self):
        item_names = ", ".join(f"{item.product.name} x{item.quantity}" for item in self.items)
        return f"Order({item_names}, partner={self.delivery_partner.name})"


class OrderService:
    def __init__(self, store_manager, delivery_service):
        self.store_manager = store_manager
        self.delivery_service = delivery_service

    def create_order(self, user_x, user_y, cart_items):

        # 1 nearest store
        store = self.store_manager.find_nearest_store(user_x, user_y)

        if not store:
            return "No store available"

        # 2 inventory check
        for item in cart_items:
            if not store.has_product(item.product, item.quantity):
                return f"{item.product.name} not available"

        # 3 assign delivery partner BEFORE removing inventory
        partner = self.delivery_service.assign_partner()

        if not partner:
            return "No delivery partner available"

        # 4 remove inventory (safe now — partner confirmed)
        for item in cart_items:
            store.remove_product_from_store(item.product, item.quantity)

        # 5 create order
        order = Order((user_x, user_y), cart_items, store, partner)

        return order
