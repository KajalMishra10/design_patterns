from Notification import UserObserver,Notification
class User:
    def __init__(self,user_id):
        self.notificationOb=UserObserver()
        self.history={}
        self.notification=Notification()
        self.user_id=user_id
        self.notification.addObserver(user_id, self.notificationOb)


    def AddPerferences(self,preference):
        self.UserPreference=preference

    def AddProfile(self,userProfile):
        self.userProfile=userProfile
        
    def AddGender(self,gender):
        self.gender=gender

    def Swipe(self,swipe,other_user):
        other_id = other_user.user_id

        self.history[other_id] = swipe

        if swipe == "right" and other_user.history.get(self.user_id) == "right":
            self.notification.notify(self.user_id, "It's a MATCH 🎉")
            self.notification.notify(other_id, "It's a MATCH 🎉")
        else:
            self.notification.notify(self.user_id, "No match yet ❌")

    def swipeHistory(self,swipe,user_id):
        self.history[user_id]=swipe
    


    