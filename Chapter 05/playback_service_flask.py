
from flask import Flask, send_file

app = Flask(__name__)

class PlaybackDao:
    def get_song_file(self, song_id):
        # In a real application, you would fetch the song file based on the ID
        return 'some_song.mp3'

playbackDao = PlaybackDao()

@app.route('/play/<song_id>', methods=['GET'])
def play_song(song_id):
    song_file = playbackDao.get_song_file(song_id)
    return send_file(song_file, as_attachment=True)
