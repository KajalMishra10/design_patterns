class IDisplay:
    def display(self, data):
        raise NotImplementedError("Subclasses must implement this method.")
    
class RealDisplay(IDisplay):
    def display(self, data):
        print(f"Displaying: {data}")

class ProxyDisplay(IDisplay):
    def __init__(self):
        self.real_display = None

    def display(self, data):
        if self.real_display is None:
            self.real_display = RealDisplay()
        print("Proxy: Checking access before displaying.")
        self.real_display.display(data)
# Example usage
proxy = ProxyDisplay()
proxy.display("Hello, World!")