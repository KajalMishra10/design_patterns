class command:
    def execute(self):
        pass
    def undo(self):
        pass


class LightOnCommand(command):
    def __init__(self,light):
        self.light=light

    def execute(self):
        return self.light.on()
    
    def undo(self):
        return self.light.off()
    
class AirConditionerOnCommand(command):
    def __init__(self,air_conditioner):
        self.air_conditioner=air_conditioner

    def execute(self):
        return self.air_conditioner.on()
    
    def undo(self):
        return self.air_conditioner.off()
    


class Light:
    def on(self):
        print("Light is on")
    
    def off(self):
        print("Light is off")
    
class AirConditioner:
    def on(self):
        print("Air Conditioner is on")
    
    def off(self):
        print("Air Conditioner is off")
    

class RemoteControl:
    def __init__(self):
        self.list=[None] * 4
        self.visited= [False] * 4
    def AddCommand(self,command, i):
        self.list[i]=command
        self.visited[i]=False


    def RemoveCommand(self,command, i):
        self.list[i]=None
        self.visited[i]=False
        
    def RunButton(self,i):
        if(i>4):
            return 
        if(self.visited[i]==False):
            self.list[i].execute()
            self.visited[i]=True

        else:
            self.list[i].undo()
            self.visited[i]=False


light=Light()
air_conditioner=AirConditioner()
light_on_command=LightOnCommand(light)
air_conditioner_on_command=AirConditionerOnCommand(air_conditioner)

remote_control=RemoteControl()
remote_control.AddCommand(light_on_command,0)
remote_control.AddCommand(air_conditioner_on_command,1)
remote_control.RunButton(0)
remote_control.RunButton(1)
remote_control.RunButton(1)