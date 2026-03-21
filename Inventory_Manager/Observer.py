from abc import ABC, abstractmethod


# --- Base Observer & Subject ---

class Observer(ABC):
    """Koi bhi jo events sunna chahta hai"""
    @abstractmethod
    def update(self, event_type, data):
        pass


class Subject:
    """Koi bhi jo events fire karta hai — isko inherit karo"""
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, event_type, data):
        for observer in self._observers:
            observer.update(event_type, data)


# --- Concrete Observers ---

class SMSNotifier(Observer):
    """User ko SMS bhejo jab order status change ho"""
    def update(self, event_type, data):
        if event_type == "ORDER_PLACED":
            print(f"[SMS] Order placed! Items: {data['items']}")
        elif event_type == "ORDER_DELIVERED":
            print(f"[SMS] Your order has been delivered!")


class EmailNotifier(Observer):
    """Admin ko email jab stock low ho"""
    def update(self, event_type, data):
        if event_type == "LOW_STOCK":
            print(f"[EMAIL] LOW STOCK ALERT: {data['product_name']} only {data['quantity']} left in store ({data['store']})")


class AutoRefillHandler(Observer):
    """Stock low hone pe auto refill trigger karo"""
    def update(self, event_type, data):
        if event_type == "LOW_STOCK":
            store = data["store"]
            product = data["product"]
            if store.fill_strategy:
                print(f"[AUTO-REFILL] Triggering refill for {product.name}")
                store.fill_strategy.fill(product, store)
