class Message:
    def __init__(self,user_id,timeStamp,chatRoomId,content):
        self.user_id=user_id
        self.timeStamp=timeStamp
        self.chatRoomId=chatRoomId
        self.content=content

class ChatRoom:
    def __init__(self,chat_id,user1,user2):
        self.chat_id=chat_id
        self.user1=user1
        self.user2=user2
        self.messages=[]
    
    def addMessages(self,message):
        if message.user_id not in self.users:
            raise Exception("User not part of this chat ❌")
        self.messages.append(message)

