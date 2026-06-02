
from typing import Dict
import uuid

from content import Question, Answer
from User import User
from reputation_manager import reputation_manager

class stack_overflow_service:
    def __init__(self):
        self.users = {}
        self.questions: Dict[str, Question] = {}
        self.answers: Dict[str, Answer] = {}
        self.reputation_manager = reputation_manager()

    def register_user(self, name):
        user = User(name)
        self.users[user.get_id()] = user
        return user
    
    def post_question(self, user_id, title, body, tags):
        user = self.users.get(user_id)
        if not user:
            print("User not found.")
            return None
        question_id = str(uuid.uuid4())
        question = Question(title, body, user, question_id, tags)
        question.add_observer(self.reputation_manager)
        self.questions[question_id] = question
        return question
    
    def post_answer(self, user_id, question_id, body):
        user = self.users.get(user_id)
        if not user:
            print("User not found.")
            return None
        question = self.questions.get(question_id)
        if not question:
            print("Question not found.")
            return None
        answer_id = str(uuid.uuid4())
        answer = Answer("", body, user, answer_id, question)
        answer.add_observer(self.reputation_manager)
        self.answers[answer_id] = answer
        question.answers.append(answer)
        return answer
    
    def accept_answer(self, user_id, question_id, answer_id):
        user = self.users.get(user_id)
        if not user:
            print("User not found.")
            return
        question = self.questions.get(question_id)
        if not question:
            print("Question not found.")
            return
        answer = self.answers.get(answer_id)
        if not answer:
            print("Answer not found.")
            return
        question.accept_answer(answer)