class DeliveryAgent:
    def __init__(self, name):
        self.name = name

    def deliver(self, order):
        print(f"{self.name} is delivering {order}.")  
        


class DeliveryAgentAssignment:
    def __init__(self):
        self.agents = []

    def add_agent(self, name):
        agent = DeliveryAgent(name)
        self.agents.append(agent)
        print(f"Delivery agent {name} added successfully.")

    def assign_delivery(self, order):
        pass

class RandomDeliveryAgentAssignment(DeliveryAgentAssignment):
    def assign_delivery(self, order):
        if not self.agents:
            print("No delivery agents available to assign.")
            return
        import random
        agent = random.choice(self.agents)
        agent.deliver(order)


class RoundRobinDeliveryAgentAssignment(DeliveryAgentAssignment):
    def __init__(self):
        super().__init__()
        self.current_index = 0

    def assign_delivery(self, order):
        if not self.agents:
            print("No delivery agents available to assign.")
            return
        agent = self.agents[self.current_index]
        agent.deliver(order)
        self.current_index = (self.current_index + 1) % len(self.agents)

class DeliveryService:
    def __init__(self, assignment_strategy):
        self.assignment_strategy = assignment_strategy
        self.assignment_strategy.add_agent("kajal")   
        self.assignment_strategy.add_agent("abhi")   

    def assign_delivery(self, order):
        self.assignment_strategy.assign_delivery(order)

    def add_delivery_agent(self, name):
        self.assignment_strategy.add_agent(name)    
    
    def display_agents(self):
        print("Delivery Agents:")
        for agent in self.assignment_strategy.agents:
            print(f"- {agent.name}")

    def display_assignment_strategy(self):
        strategy_name = type(self.assignment_strategy).__name__
        print(f"Current delivery assignment strategy: {strategy_name}")
        