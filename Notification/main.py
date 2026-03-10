import notification
import observer
import SendNotification


list

notification1=notification.SimpleNotification()
notification2=notification.HTMLDecorator(notification1).prepare("Hello World")
print(notification2)



observable=observer.YouTube()
logger=SendNotification.Logger(observable)
#logger.update()
observable.AddObserver(logger)
observable.AddNotification(notification2)

notify=SendNotification.Notify(SendNotification.pushStrategy(),observable)
observable.AddObserver(notify)
observable.AddNotification(notification2)

#notify.update()
