from connectDevice import ConnectManager
import play
from song import randomStrategy, sequentialStrategy


class Orchestarator:
    def __init__(self):
        self.connected_device = None

    def connect_device(self, device):
        a = ConnectManager()
        self.connected_device=a.connect_device(device)
    
    
    def play_song(self,song):
        if self.connected_device:
            play.Play(song, "timestamp").play_song(self.connected_device)
        else:
            print("No device connected. Please connect a device to play the song.")

    def pause_song(self, song):
        if self.connected_device:
            play.Play(song, "timestamp").pause_song()
        else:
            print("No device connected. Please connect a device to pause the song.")

    def play_playlist(self, playlist, strategy):
        if not self.connected_device:
            print("No device connected. Please connect a device to play the playlist.")
            return
        songs = playlist.get_songs()
        if not songs:
            print("No songs in the playlist.")
            return
        for _ in range(len(songs)):
            song = strategy.return_song(playlist)
            self.play_song(song)

    
    def create_Strategy(self, strategy_type):
        if strategy_type == "random":
            return randomStrategy()
        elif strategy_type == "sequential":
            return sequentialStrategy()
        else:
            raise ValueError("Invalid strategy type")