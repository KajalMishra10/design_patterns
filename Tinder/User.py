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
    
class  MatchService:
    def __init__(self):
        self.notification=Notification()
        self.swipe={}
    
    def swipe(self,user1,user2,direction):
        u1=user1.user_id
        u2=user2.user_id

    #store swipes
        self.swipe[(u1,u2)]=direction
        if direction=="right" and self.swipe[(u2,u1)]=="right":
            self.notification.notify(u1, "Its a match")
            self.notification.notify(u2, "It's a MATCH")
        else:
            self.notification.notify(u1, "No match yet ❌")


class userProfile:
    def __init__(self , name, age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        self.interests = []   
        self.location = None

    def setName(self,name):
        self.name=name

    def setAge(self,age):
        self.age=age

    def setGender(self,gender):
        self.gender=gender

    def setLocation(self,location):
        self.location=location

    def addInterest(self,Interest):
        self.interest.append(Interest)


class Gender:
    def __init__(self,gender):
        self.gender=gender

    def setGender(self,gender):
        self.gender=gender

class location:
    def __init__(self,loc):
        self.loc=loc

class Interest:
    def addInterest(self, interest):
        self.interests.append(interest)

class UserPreferences:
    def setMinAge(self,age):
        self.age=age
    
    def setMaxAge(self,age):
        self.age=age

    def gender(self,gender):
        self.gender=gender

    def maxDistance(self,dis):
        self.distance=dis





    