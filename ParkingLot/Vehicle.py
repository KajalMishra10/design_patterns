class Vehicle:
    def __init__(self, type, number):
        self.type = type
        self.number = number
        
    def get_info(self):
        return f"{self.type} - {self.number}"