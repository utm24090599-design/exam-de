from song import Song, parse_duration

#Maxima duración del CD
MAX_TIME = 80.0

class AudioCD:
    def __init__(self):
        self.songs = []

    def total_duration(self):
        return sum(song.duration for song in self.songs)

    def add_song(self, name, artist, duration_value):
        duration = parse_duration(duration_value)

        if self.total_duration() + duration > MAX_TIME:
            raise ValueError("Se exceden los 80 minutos del CD")

        song = Song(name, artist, duration)
        self.songs.append(song)
