class observable:
    def AddNotification(self, notification):
        pass
    def getNotification(self):
        pass
    def NotifyObserver(self):
        pass
    def AddObserver(self, observer):
        pass

class YouTube(observable):
    def __init__(self):
        self.observers=[]
        self.notification=None

    def AddNotification(self, notification):
        self.notification=notification
        self.NotifyObserver()

    def getNotification(self):
        return self.notification
    
    def NotifyObserver(self):
        for observer in self.observers:
            print("Notifying observer:", observer)
            observer.update()

    def AddObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)


class Observer:
    def __init__(self,observable):
        self.observable=observable
        
    def update(self):
        pass
        

