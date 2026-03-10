class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler
    
    def handle(self, request):
        pass

class thousands_handler(Handler):
    def handle(self, request):
        if request >= 1000:
            print(f"Handling {request} in thousands handler")
        elif self.next_handler:
            self.next_handler.handle(request)

class hundreds_handler(Handler):
    def handle(self, request):
        if request >= 100:
            print(f"Handling {request} in hundreds handler")
        elif self.next_handler:
            self.next_handler.handle(request)

# Example usage
thousands = thousands_handler()
hundreds = hundreds_handler()
thousands.set_next(hundreds)
thousands.handle(1500)  # Output: Handling 1500 in thousands handler
thousands.handle(500)   # Output: Handling 500 in hundreds handler