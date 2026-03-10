class JuiceMachine:
    def __init__(self):
        self.state = IdleState()

    def insert_coin(self,amount):
        self.state.coinInserted(self,amount)
    
    def select_juice(self,juice):
        self.state.juiceSelected(self,juice)
    
    def dispense_juice(self):
        self.state.juiceDispensed(self)

class State:
    def coinInserted(self, machine, amount):
        pass

    def juiceSelected(self, machine, juice):
        pass

    def juiceDispensed(self, machine):
        pass

class IdleState(State):
    def coinInserted(self, machine, amount):
        print(f"Coin inserted: {amount}")
        machine.state = HasCoinState()

    def juiceSelected(self, machine, juice):
        print("Please insert coin first.")

    def juiceDispensed(self, machine):
        print("Please insert coin and select juice first.")

class HasCoinState(State):
    def coinInserted(self, machine, amount):
        print("Coin already inserted. Please select juice.")

    def juiceSelected(self, machine, juice):
        print(f"Juice selected: {juice}")
        machine.state = DispensingState()

    def juiceDispensed(self, machine):
        print("Please select juice first.")     

class DispensingState(State):
    def coinInserted(self, machine, amount):
        print("Currently dispensing juice. Please wait.")

    def juiceSelected(self, machine, juice):
        print("Currently dispensing juice. Please wait.")

    def juiceDispensed(self, machine):
        print("Juice dispensed. Enjoy!")
        machine.state = IdleState()

JuiceMachine = JuiceMachine()
JuiceMachine.insert_coin(1)
JuiceMachine.select_juice("Orange")
JuiceMachine.dispense_juice()
JuiceMachine.dispense_juice()
JuiceMachine.insert_coin(1)
JuiceMachine.select_juice("Apple")
