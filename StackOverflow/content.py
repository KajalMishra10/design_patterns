from enums import VoteType, EventType
from typing import Dict, List, Optional
from post_observer import PostObserver
from Event import Event
import uuid
from Tag import Tag

class content:
    def __init__(self, title, body,user,id):
        self.title = title
        self.body = body
        self.user = user
        self.id = id

    def display(self):
        print(f"Title: {self.title}")
        print(f"Body: {self.body}")
        print(f"User: {self.user}")

    def get_id(self):
        return self.id
    
    def get_title(self):
        return self.title
    
    def get_body(self):
        return self.body
    
    def get_user(self):
        return self.user
    

class Post(content):
    def __init__(self, title, body,user,id):
        super().__init__(title, body,user,id)
        self.votes = 0
        self.voters: Dict[str, VoteType] = {}
        self.comments = List['Comment'] = []
        self.observers = List['PostObserver'] = []
    
    def add_observer(self, observer: PostObserver):
        self.observers.append(observer)

    def notify_observers(self, event: 'Event'):
        for observer in self.observers:
            observer.on_post_event(self, event)

    def add_comment(self, comment):
        self.comments.append(comment)

    def vote(self,user, vote_type: VoteType):
        user_id = user.get_id()
        if self.voters.get(user_id)==vote_type:
            print("User has already voted.")
            return
        
        #self.voters[user.get_id()] = vote_type
        score_change=0
        if user_id in self.voters:
            previous_vote = self.voters[user_id]
            if previous_vote == VoteType.UPVOTE:
                score_change -= 2
            elif previous_vote == VoteType.DOWNVOTE:
                score_change += 2

        else:
            if vote_type == VoteType.UPVOTE:
                score_change += 1
            elif vote_type == VoteType.DOWNVOTE:
                score_change -= 1

        self.votes += score_change
        self.voters[user_id] = vote_type
        if isinstance(self, Question):
            event_type = EventType.UPVOTE_QUESTION if vote_type == VoteType.UPVOTE else EventType.DOWNVOTE_QUESTION
        else:
            event_type = EventType.UPVOTE_ANSWER if vote_type == VoteType.UPVOTE else EventType.DOWNVOTE_ANSWER

        self.notify_observers(Event(event_type, user, self))

    def get_votes(self):
        return self.votes
    
    def get_user(self):
        return self.user
    

class Question(Post):
    def __init__(self, title, body,user,id,tags:set[Tag]):
        super().__init__(title, body,user,id)
        self.answers = List['Answer'] = []
        self.tags = tags
        self.accepted_answer: Optional['Answer'] = None
        
    def add_answer(self, answer):
        self.answers.append(answer)

    def get_answers(self):
        return self.answers
    
    def get_tags(self):
        return self.tags
    
    def accept_answer(self, answer):
        if self.user.get_id() != answer.get_user().get_id() and self.accepted_answer is None:
            self.accepted_answer = answer
            answer.set_accepted(True)

        self.notify_observers(Event(EventType.ACCEPT_ANSWER, self.user, answer))

class Answer(Post):
    def __init__(self, title, body,user,id):
        super().__init__(title, body,user,id)
        self.is_accepted = False

    def set_accepted(self, accepted: bool):
        self.is_accepted = accepted

    def get_is_accepted(self):
        return self.is_accepted
    
class Comment(content):
    def __init__(self, body: str, user):
        super().__init__(str(uuid.uuid4()), body, user)