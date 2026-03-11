class car:
    def __init__(self, name, speed, engine):
        self.name = name
        self.speed = speed
        self.engine = engine

    def move(self):
        pass

class suv(car):
    def __init__(self, name, speed, engine):
        super().__init__(name, speed,engine)

    def move(self):
        self.engine.start()
        print(f"{self.name} has a {self.engine} engine.")

class sedan(car):
    def __init__(self, name, speed, engine):
        super().__init__(name, speed,engine)

    def move(self):
        self.engine.start()
        print(f"{self.name} has a {self.engine} engine.")


class Engine:
    def __init__(self, type):
        self.type = type

    def start(self):
        pass

class ElectricEngine(Engine):
    def __init__(self):
        super().__init__("Electric")
    
    def start(self):
        print("Starting electric engine...")

class GasEngine(Engine):
    def __init__(self):
        super().__init__("Gas")

    def start(self):
        print("Starting gas engine...")


electric_engine = ElectricEngine()
gas_engine = GasEngine()
suv_car = suv("SUV Car", 120, electric_engine)
sedan_car = sedan("Sedan Car", 100, gas_engine)
suv_car.move()  
sedan_car.move()  
