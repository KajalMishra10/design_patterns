class IObserver:
    def update(self, video):
        pass


class IObservable:
    def addObserver(self, observer):
        pass

    def removeObserver(self, observer):
        pass

    def notifyObservers(self):
        pass


class Youtube(IObservable):
    def __init__(self):
        self.observers = []   # subscribers list
        self.video = None
    
    def addObserver(self, observer):
        self.observers.append(observer)
    
    def removeObserver(self, observer):
        print('removed subscirbet')
        self.observers.remove(observer)

    def addVideo(self,video):
        print('video added')
        print(video )
        self.video=video
        self.notifyObservers()

    def notifyObservers(self):
        for observer in self.observers:
            observer.update()
    def getVideo(self):
        return self.video

class Subscriber(IObserver):
    def __init__(self,observable):
        self.observable=observable
    def update(self):
        print('received')
        self.observable.getVideo()


Utube=Youtube()
sub1=Subscriber(Utube)
sub2=Subscriber(Utube)
Utube.addObserver(sub1)
Utube.addObserver(sub2)

Utube.addVideo('Teri baaton me aise uljha jiya')
Utube.removeObserver(sub1)
Utube.addVideo('Lapaata Ladies')
