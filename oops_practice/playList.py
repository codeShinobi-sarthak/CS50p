class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __str__(self):
        return f"'{self.title}' by {self.artist}"
    
    def __repr__(self):
        return f"Song(title={self.title}, artist={self.artist})"
    
class Playlist:
    def __init__(self, name, songs=None):
        self.name = name
        self._songs = songs if songs is not None else []

    def add_song(self, song):
        self._songs.append(song)

    def __str__(self):
        return f"Playlist: {self.name}, Songs: {len(self._songs)}"

    def __repr__(self):
        return f"Playlist(name={self.name}, songs={self._songs})"

    def __len__(self):
        return len(self._songs)
        
    @staticmethod
    def is_valid_song(song):
        if isinstance(song, Song):
            return True
        
        return False
    
    @classmethod
    def from_artist(cls, artist_name, all_songs):
        pl = Playlist(f"{artist_name} Essentials", [])
        for song in all_songs:
            if cls.is_valid_song(song) and song.artist == artist_name:
                pl._songs.append(song)
        return pl
    

# Create some song objects
song1 = Song("Bohemian Rhapsody", "Queen")
song2 = Song("Stairway to Heaven", "Led Zeppelin")
song3 = Song("Another One Bites the Dust", "Queen")

# Test the static method
print(f"Is song1 valid? {Playlist.is_valid_song(song1)}")

# Create a Playlist and add songs
my_playlist = Playlist("Rock Classics")
my_playlist.add_song(song1)
my_playlist.add_song(song2)

# Test len() and print() (which use our dunder methods)
print(f"My playlist has {len(my_playlist)} songs.")
print(my_playlist)

# Test the class method factory
all_songs = [song1, song2, song3]
queen_playlist = Playlist.from_artist("Queen", all_songs)

# Check the new playlist
print("\n--- Queen Essentials Playlist ---")
print(queen_playlist)
print(f"It has {len(queen_playlist)} songs.")