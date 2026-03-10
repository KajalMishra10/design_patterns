from Content import BoldTextContent, TextContent
from Persistent import DatabasePersistent, FilePersistent


class DocumentEditor:
    def __init__(self, document):
        self.document = document
    def addText(self , command):
        command.execute()
    def addImage(self, command):        
        command.execute()
    def save(self, option):
        if option=="file":
            persistent=FilePersistent("document.txt")
            persistent.save(self.document.render())
        if option=="database":
            persistent=DatabasePersistent("db_connection_string")
            persistent.save(self.document.render())
            print("Saving to database...")  
    
    def boldText(self, command):
        command.execute()
       

       