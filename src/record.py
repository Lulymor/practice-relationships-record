class Record:
    def __init__(self, title, artist, year):
        self.title = title
        self.year = year
        self.artist = artist
    
    def get_title(self):
        return self.title.title()
    
    def get_artist(self):
        return self.artist
    
    def get_year(self):
        return self.year
    
    def get_songs(self):
        return self.songs
    
    def total_runtime(self):
        return sum([song.runtime for song in self.songs])
    
    def has_song(self, song):
        return song in self.songs
    
    def get_longest_song(self):
        longest = self.songs[0]
        for song in self.songs:
            if song.runtime > longest.runtime:
                longest = song
        return longest
        