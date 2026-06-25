class TrafficLight:
    def __init__(self, id, state):
        self.id = id
        self.color = state

    def change_state(self, new_state):
        self.color = new_state

    def get_state(self):
        return self.color
    