class notification:
    def prepare(self,message):
        pass

class SimpleNotification(notification):
    def prepare(self,message):
        return message
    
class decorator(notification):
    def __init__(self,notification):
        self._notification = notification

    def prepare(self,message):
        pass

class HTMLDecorator(decorator):
    def __init__(self,notification):
        super().__init__(notification)
    def prepare(self,message):
        return "<html><body>" + self._notification.prepare(message) + "</body></html>"
    
class JSONDecorator(decorator):
    def __init__(self,notification):
        super().__init__(notification)
    def prepare(self,message):
        return '{"message": "' + self._notification.prepare(message) + '"}'
    


