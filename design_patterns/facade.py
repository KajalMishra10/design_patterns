from fastapi import Depends


class Facade:
    def __init__(self):
        self.getElectricShock=GetElectricShock()
        self.makeSound=MakeSound()
        self.showLoadingScreen=ShowLoadingScreen()
        self.bam=Bam()

    def startComputer(self):
        self.getElectricShock.start()
        self.makeSound.start()
        self.showLoadingScreen.start()
        self.bam.start()



class GetElectricShock:
    def start(self):
        print("Ouch! Getting an electric shock!")

class MakeSound:
    def start(self):
        print("Making some sound!")

class ShowLoadingScreen:
    def start(self):
        print("Showing loading screen!")

class Bam:
    def start(self):
        print("Bam! Computer started!")

class Client:
    def main(self):
        facade=Facade()
        facade.startComputer()

client1=Client()
client1.main()