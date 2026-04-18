import threading

class Notification:
    _instance = None
    _lock = threading.Lock()   # 🔐 lock

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:   # critical section
                if cls._instance is None:   # double check
                    cls._instance = super(Notification, cls).__new__(cls)
                    cls._instance.observers = {}
                    cls._instance.message = ""
        return cls._instance
    
    def addObserver(self,user, observer):
        self.observers[user]=observer
        print('added observer')

    def removeObserver(self,user):
        if user in self.observers:
            del self.observers[user]
    
    def notify(self,user,message):
        self.message=message
        if user in self.observers:
            self.observers[user].update()
         
    def notifyAll(self,message):
        self.message=message
        for user, observer in self.observers.items():
            observer.update()
    
    def getMessage(self):
        return self.message

class Observer:
    def __init__(self):
        self.notification=Notification()

    def update(self):
        pass
        
class UserObserver(Observer):
    def update(self):
        message=self.notification.getMessage()
        print(message)
        return message
