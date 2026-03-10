from orchestarator import Orchestarator
from song import Song, PlaylistManager

orchestarator=Orchestarator()
orchestarator.connect_device("bluetooth")
playlist_manager = PlaylistManager()

playlist_manager.create_playlist("My Playlist")
playlist = playlist_manager.get_playlist("My Playlist")
song1 = Song("Song 1", "Artist 1")
song2 = Song("Song 2", "Artist 2")  
playlist.add_song(song1)
playlist.add_song(song2)
orchestarator.play_playlist(playlist, orchestarator.create_Strategy("random"))
