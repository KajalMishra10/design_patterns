class Play:
    def __init__(self, song, timestamp):
        self.song = song
        self.timestamp = timestamp

    def play_song(self, device):    
        device.play_song(self.song) 

    def pause_song(self):
        print(f"Pausing '{self.song.title}' by {self.song.artist}.")



