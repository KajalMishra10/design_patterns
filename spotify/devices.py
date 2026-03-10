class BlueToothSpeaker:
    def __init__(self, name):
        self.name = name

    def play_song(self, song):
        print(f"Playing '{song.title}' by {song.artist} on {self.name} Bluetooth Speaker.")

class SpeakerSystem:
    def __init__(self, name):
        self.name = name

    def play_song(self, song):
        print(f"Playing '{song.title}' by {song.artist} on {self.name} Speaker System.")