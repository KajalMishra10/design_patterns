from stack_overflow_service import stack_overflow_service
from User import User
from Tag import Tag
stackOverflow=stack_overflow_service()

user1=stackOverflow.register_user('Kajal')
user2=stackOverflow.register_user('Abhi')

question1=stackOverflow.post_question()
