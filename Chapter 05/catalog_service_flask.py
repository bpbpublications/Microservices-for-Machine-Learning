
from flask import Flask, jsonify, request

app = Flask(__name__)

import mysql.connector

class CatalogDao:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',
            database='your_database'
        )
        self.cursor = self.conn.cursor()

    def get_songs(self):
        sql = "SELECT * FROM songs"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_song_by_id(self, song_id):
        sql = "SELECT * FROM songs WHERE id=%s"
        val = (song_id, )
        self.cursor.execute(sql, val)
        return self.cursor.fetchone()

catalog_dao = CatalogDao()

@app.route('/songs', methods=['GET'])
def get_songs():
    return jsonify({'songs': catalog_dao.get_songs()})

@app.route('/songs/<song_id>', methods=['GET'])
def get_song_by_id(song_id):
    song = catalog_dao.get_song_by_id(song_id)
    if song:
        return jsonify({'song': song})
    else:
        return jsonify({'message': 'Song not found'}), 404
