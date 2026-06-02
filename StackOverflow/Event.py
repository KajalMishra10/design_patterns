class Event:
    def __init__(self, Event_type, user, post):
        self.type = Event_type
        self.user = user
        self.post = post

    def get_type(self) :
        return self.type

    def get_actor(self) :
        return self.user

    def get_target_post(self) :
        return self.post