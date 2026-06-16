class LogSubject:
    def __init__(self):
        self.mp = {}

    def add_handler(self, level, handler):
        if level not in self.mp:
            self.mp[level] = []
        self.mp[level].append(handler)

    def notify_handlers(self, level, message):
        if level in self.mp:
            for handler in self.mp[level]:
                handler.print(message)