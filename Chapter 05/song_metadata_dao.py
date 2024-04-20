
class SongMetadataDao:
    def __init__(self):
        self.songs = [
            {'id': 1, 'title': 'Song A', 'artist': 'Artist 1'},
            {'id': 2, 'title': 'Song B', 'artist': 'Artist 2'},
        ]

    def get_song(self, song_id):
        return next((song for song in self.songs if song['id'] == song_id), None)
    