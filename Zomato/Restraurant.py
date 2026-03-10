class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Restaurant:
    def __init__(self,name):
        self.name = name
        self.menu = [MenuItem('rajma',200), MenuItem('chawal',250)]
        self.open=True

    def add_menu_item(self, name, price):
        item = MenuItem(name, price)
        self.menu.append(item)      

    def display_menu(self):
        print(f"Menu for {self.name}:")
        for item in self.menu:
            print(f"{item.name}: ${item.price:.2f}")
        return self.menu

    def remove_menu_item(self,name):
        for item in self.menu:
            if item.name==name:
                self.menu.remove(item)
                print(f"{name} has been removed from the menu.")
                return
            
    def canAddOrder(self):
        if not self.open:
            print("Sorry, the restaurant is closed. Cannot add order.")
            return False
        return True

        

class KingBurger(Restaurant):
    def __init__(self):
        super().__init__("King Burger")
        self.add_menu_item("Classic Burger", 5.99)
        self.add_menu_item("Cheese Burger", 6.99)
        self.add_menu_item("Bacon Burger", 7.99)

class PizzaPalace(Restaurant):
    def __init__(self):
        super().__init__("Pizza Palace")
        self.add_menu_item("Margherita Pizza", 8.99)
        self.add_menu_item("Pepperoni Pizza", 9.99)
        self.add_menu_item("Veggie Pizza", 10.99)

class Cart:
    #restaurant
    def __init__(self):
        self.items=[]
        self.total=0.0
        self.restaurant=None
        
    def addItem(self, item):
        self.items.append(item)
        self.total+=item.price
    def displayCart(self):        
        print("Cart Items:")
        for item in self.items:         
            print(f"{item.name}: ${item.price:.2f}")        
            print(f"Total: ${self.total:.2f}")  

    def clearCart(self):        
        self.items=[]
        self.total=0.0
    
    def ApplyCoupon(self,coupon):
        self.total=coupon.apply_coupon(self.total)
        

class RestaurantService:
        def __init__(self):
            self.restaurants = [KingBurger(), PizzaPalace()]
    
        def displayRestaurants(self):
            print("Available Restaurants:")
            for restaurant in self.restaurants:
                print(restaurant.name)
    
        def getRestaurantByName(self, name):
            for restaurant in self.restaurants:
                if restaurant.name == name:
                    return restaurant
            return None   
        
        def selectRestaurant(self,name,user):
            user.cart.restaurant=name        
        