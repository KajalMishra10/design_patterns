from stack_overflow_service import stack_overflow_service
from Tag import Tag
from enums import VoteType
from search_strategy import (
    KeywordSearchStrategy,
    TagSearchStrategy,
    UserSearchStrategy,
)

# Create service
stack_overflow = stack_overflow_service()

# Register users
user1 = stack_overflow.register_user("Kajal")
user2 = stack_overflow.register_user("Abhi")

# Create tags
python_tag = Tag("python")
ai_tag = Tag("AI")

# Post question
question1 = stack_overflow.post_question(
    user1.get_id(),
    "Python Summary",
    "Python is hot topic in the market",
    [python_tag, ai_tag]
)

question2 = stack_overflow.post_question(
    user2.get_id(),
    "AI Future",
    "Artificial Intelligence is changing the world",
    [ai_tag]
)

# Post answers
answer1 = stack_overflow.post_answer(
    user2.get_id(),
    question1.get_id(),
    "Python is easy to learn and widely used."
)

answer2 = stack_overflow.post_answer(
    user1.get_id(),
    question2.get_id(),
    "AI will automate many tasks."
)

# Voting
question1.vote(user2, VoteType.UPVOTE)
answer1.vote(user1, VoteType.UPVOTE)

# Accept answer
stack_overflow.accept_answer(
    user1.get_id(),
    question1.get_id(),
    answer1.get_id()
)

# -----------------------------
# Search by keyword
# -----------------------------
print("\nSearch By Keyword: Python")

results = KeywordSearchStrategy("python").filter(
    list(stack_overflow.questions.values())
)

for q in results:
    print(f"{q.get_title()}")

# -----------------------------
# Search by Tag
# -----------------------------
print("\nSearch By Tag: AI")

results = TagSearchStrategy(ai_tag).filter(
    list(stack_overflow.questions.values())
)

for q in results:
    print(f"{q.get_title()}")

# -----------------------------
# Search by User
# -----------------------------
print("\nSearch By User: Kajal")

results = UserSearchStrategy(user1).filter(
    list(stack_overflow.questions.values())
)

for q in results:
    print(f"{q.get_title()}")

# -----------------------------
# Display reputation
# -----------------------------
print("\nUser Reputations")
print(f"{user1.get_name()} -> {user1.get_reputation()}")
print(f"{user2.get_name()} -> {user2.get_reputation()}")