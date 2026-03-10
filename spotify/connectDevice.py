from devices import BlueToothSpeaker
from devices import SpeakerSystem


class ConnectDevice:
    def connect(self, device):
        pass
    def play_song(self, song):
        pass
class ConnectBluetoothDevice(ConnectDevice):
    def __init__(self):
        self.device = None
        
    def connect(self,device):
        self.device = device
        print(f"Connecting to Bluetooth device: {self.device}")
        return self.device
    
    def play_song(self, song):
        self.device.play_song(song)

class ConnectSpeakerSystem(ConnectDevice):
    def __init__(self):
        self.device = None

    def connect(self,device):
        self.device = device
        print(f"Connecting to Speaker System: {self.device}")
        return self.device
    def play_song(self, song):
        self.device.play_song(song)  
        
class ConnectManager:
    def __init__(self):
        self.connected_device = None

    def connect_device(self,device_type):
        self.connected_device = ConnectFactory.create_connect_device(device_type)
        return self.connected_device

    def getDevice(self):
        return self.connected_device


class ConnectFactory:
    @staticmethod
    def create_connect_device(device_type):
        if device_type == "bluetooth":
             adapter = ConnectBluetoothDevice()
             adapter.connect(BlueToothSpeaker("My Bluetooth Speaker"))
             return adapter
        elif device_type == "speaker_system":
             adapter = ConnectSpeakerSystem()
             adapter.connect(SpeakerSystem("My Speaker System"))
             return adapter
        else:
            raise ValueError("Invalid device type")