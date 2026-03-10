import random

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        self.songs.remove(song)

    def get_songs(self):
        return self.songs
    

class PlaylistManager:
    def __init__(self):
        self.playlists = {}

    def create_playlist(self, name):
        if name not in self.playlists:
            self.playlists[name] = Playlist(name)
        else:
            print(f"Playlist '{name}' already exists.")

    def get_playlist(self, name):
        return self.playlists.get(name, None)

    def delete_playlist(self, name):
        if name in self.playlists:
            del self.playlists[name]
        else:
            print(f"Playlist '{name}' does not exist.")


class Strategy:
    def return_song(self, playlist):
        pass

class randomStrategy(Strategy):
    def return_song(self,playlist):
        return random.choice(playlist.get_songs())
        
    def next_song(self):
        print("Playing next song using Random Strategy.")

class sequentialStrategy(Strategy):
    def __init__(self):
        self.current_index = 0

    def return_song(self, playlist):
        songs = playlist.get_songs()
        if not songs:
            return None
        song = songs[self.current_index]
        self.current_index = (self.current_index + 1) % len(songs)
        return song
    
    def next_song(self):
        print("Playing next song using Sequential Strategy.")