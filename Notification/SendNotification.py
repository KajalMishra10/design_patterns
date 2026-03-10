class SendNotification:
    def update():
        pass

class Logger(SendNotification):
    def __init__(self, observable):
        self.observable = observable
    def update(self):
        A=self.observable.getNotification()
        print("Notification sent to logger",A)

class Notify:
    def __init__(self, strategy, observable):
        self.list = []  
        self.list.append(strategy)
        self.observable = observable
        print("Notify object created with strategy:", strategy)

    def update(self):
        A=self.observable.getNotification()
        for strategy in self.list:
            return strategy.Send(A)



class Strategy():
    def Send(self,message):
        pass

class pushStrategy(Strategy):
    def Send(self,message):
        print("Sending notification using push strategy")
        return message +'on mobile'
    
class EmailStrategy(Strategy):
    def Send(self,message):
        return message+'on email'