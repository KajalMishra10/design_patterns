class Persistent:
    def save():
        pass


class FilePersistent(Persistent):
    def __init__(self,filename):
        self.filename=filename
    
    def save(self, content):
        print(f"Saving content to file: {self.filename}")

class DatabasePersistent(Persistent):
    def __init__(self,connection_string):
        self.connection_string=connection_string
    
    def save(self, content):
        print(f"Saving content to database with connection: {self.connection_string}")
