class Handler:
    def print(self, message):
        raise NotImplementedError("Subclasses must implement this method")
    

class fileHandler(Handler):
    def print(self, message):
        with open("log.txt", "a") as log_file:
            log_file.write(message + "\n")


class consoleHandler(Handler):
    def print(self, message):
        print(message)