class Robot:
    
    def __init__(self,walk,talk,fly):
        self.walk = walk
        self.talk = talk
        self.fly = fly

    def project(self):
        self.walk.walk()
        self.talk.talk()
        self.fly.fly()  

#abstract classes
class Walk:
    def walk(self):
        pass

class Talk:
    def talk(self):
        pass
class Fly:
    def fly(self):
        pass

#normal behavior classes
class NormalWalk(Walk):

    def walk(self):
        print("Normal walking")

class NormalTalk(Talk):

    def talk(self):
        print("Normal talking")

class NormalFly(Fly):

    def fly(self):
        print("Normal flying")

#super behavior classes
class SuperWalk(Walk):

    def walk(self):
        print("Super walking")

class SuperTalk(Talk):

    def talk(self):
        print("Super talking")

class SuperFly(Fly):

    def fly(self):
        print("Super flying")

#creating objects

class createBehavior:
     def create_Talk(self,behavior):
         if behavior=="normal":
                return NormalTalk()
         if behavior=="super":
                return SuperTalk()
     def create_Walk(self,behavior):         
          if behavior=="normal":
                return NormalWalk()        
          if behavior=="super":    
                return SuperWalk()
     def create_Fly(self,behavior):         
          if behavior=="normal":
                return NormalFly()        
          if behavior=="super":    
                return SuperFly()

factory = createBehavior()
normal_robot=Robot(factory.create_Walk("normal"),factory.create_Talk("normal"),factory.create_Fly("normal"))
super_robot=Robot(factory.create_Walk("super"),factory.create_Talk("super"),factory.create_Fly("super"))
normal_robot.project()
super_robot.project()
