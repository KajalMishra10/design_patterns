
from post_observer import post_observer
from enums import EventType

class reputation_manager(post_observer):
    QUESTION_UPVOTE_REP = 5
    ANSWER_UPVOTE_REP = 10
    ACCEPTED_ANSWER_REP = 15
    DOWNVOTE_REP_PENALTY = -1  # Penalty for the voter
    POST_DOWNVOTED_REP_PENALTY = -2  # Penalty for the post author

    def __init__(self):
        self.user_reputation = {}

    def on_post_event(self,  event):
        user = event.get_actor()
        if event.get_type() == EventType.UPVOTE_QUESTION:
            user.add_reputation(self.QUESTION_UPVOTE_REP)
        elif event.get_type() == EventType.UPVOTE_ANSWER:
            user.add_reputation(self.ANSWER_UPVOTE_REP)
        elif event.get_type() == EventType.ACCEPT_ANSWER:
            user.add_reputation(self.ACCEPTED_ANSWER_REP)
        elif event.get_type() == EventType.DOWNVOTE_QUESTION or event.get_type() == EventType.DOWNVOTE_ANSWER:
            user.add_reputation(self.DOWNVOTE_REP_PENALTY)
            post_author = event.get_target_post().get_user()
            post_author.add_reputation(self.POST_DOWNVOTED_REP_PENALTY)
        