class DeliveryService:
    def __init__(self, partners):
        self.partners = partners

    def assign_partner(self):
        for partner in self.partners:
            if partner.available:
                partner.available = False
                return partner
        return None
    

class DeliveryPartner:
    def __init__(self, name):
        self.name = name
        self.available = True