
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock User database
import mysql.connector

class UserDao:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',
            database='your_database'
        )
        self.cursor = self.conn.cursor()
        
    def add_user(self, username, password):
        sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
        val = (username, password)
        self.cursor.execute(sql, val)
        self.conn.commit()
    
    def check_user(self, username, password):
        sql = "SELECT password FROM users WHERE username=%s"
        val = (username, )
        self.cursor.execute(sql, val)
        result = self.cursor.fetchone()
        
        if result and result[0] == password:
            return True
        return False

userDao = UserDao()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']
    userDao.add_user(username, password)
    return jsonify({'status': 'registered'})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    if userDao.check_user(username, password):
        return jsonify({'status': 'logged in'})
    else:
        return jsonify({'status': 'login failed'}), 401
