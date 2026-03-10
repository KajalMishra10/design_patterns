class Burger:
    def __init__(self,name):
        self.name = name

class ChickenBurger(Burger):
    def __init__(self):
        super().__init__("Chicken Burger")
    
class ChickenCheeseBurger(Burger):
    def __init__(self):
        super().__init__("Chicken Cheese Burger")

class VegBurger(Burger):
    def __init__(self):
        super().__init__("Veg Burger")

class VegCheeseBurger(Burger):
    def __init__(self):
        super().__init__("Veg Cheese Burger")


#gralic bread
class GralicBread():
    def __init__(self,name="Gralic Bread"):
        self.name = name

class ButterGralicBread(GralicBread):
    def __init__(self):
        super().__init__("Butter Gralic Bread")

class ChickenGralicBread(GralicBread):
    def __init__(self):
        super().__init__("Chicken Gralic Bread")
        


class Factory:
    def create_burger(self,burger_type):
        pass
class VegBurgerFactory(Factory):
    def create_burger(self,burger_type):
        if burger_type=="veg":  
            return VegBurger()
        if burger_type=="veg_cheese":
            return VegCheeseBurger()
        
    def create_bread(self,bread_type):
        if bread_type=="gralic":
            return GralicBread()
        if bread_type=="butter_gralic":
            return ButterGralicBread()
      
    
class ChickenBurgerFactory(Factory):
    def create_burger(self,burger_type):
        if burger_type=="chicken":
            return ChickenBurger()
        if burger_type=="chicken_cheese":
            return ChickenCheeseBurger()
        
    def create_bread(self,bread_type):
        if bread_type=="chicken_gralic":
            return ChickenGralicBread()
        

vegFactory=VegBurgerFactory()

print(vegFactory.create_burger("veg").name)
print(vegFactory.create_bread("gralic").name)

chickenFactory=ChickenBurgerFactory()
print(chickenFactory.create_burger("chicken_cheese").name)
print(chickenFactory.create_bread("chicken_gralic").name)