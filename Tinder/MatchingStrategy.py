class MatchStrategy:
    def __init__(self,next=None):
        self.next=next

    def addNext(self,next):
        self.next = next
        return next
    def match(self,user1,user2):
        pass
    
class LocationStrategy(MatchStrategy):
    def __init__(self,next=None):
        self.next=next

   
    def match(self,user1,user2):
        if(self.next):
            matching=self.next.match(user1,user2)
            if(matching==False):
                return matching
        l1=user1.userProfile.location
        l2=user2.userProfile.location
        if(l1==l2):
            return True

class InterestStrategy(MatchStrategy):
    def __init__(self,next=None):
        self.next=next

   

    def match(self,user1,user2):
        if(self.next):
            matching=self.next.match(user1,user2)
            if(matching==False):
                return matching
            
        i1 = set(user1.userProfile.interests)
        i2 = set(user2.userProfile.interests)

        common = i1.intersection(i2)

        if not common:
            return False
        return True
        


