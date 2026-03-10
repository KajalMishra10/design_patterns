from Restraurant import Cart


class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.cart=Cart()    


class UserService:
    def __init__(self):
        self.users=[]

    def add_user(self,name,email):
        user=User(name,email)
        self.users.append(user)
        print(f"User {name} added successfully.")
        return user
    def get_user(self,email):
        for user in self.users:
            if user.email==email:
                return user
        print(f"No user found with email: {email}")
        return None
