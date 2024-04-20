
from flask import Flask, request, session, redirect
import requests

app = Flask(__name__)
app.secret_key = 'YOUR_SECRET_KEY'
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
PASSWORD_TOKEN_URL = 'https://authorization-server.com/oauth/token'

@app.route('/login_with_password', methods=['POST'])
def login_with_password():
    username = request.form.get('username')
    password = request.form.get('password')
    token_data = {
        'grant_type': 'password',
        'username': username,
        'password': password,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }
    response = requests.post(PASSWORD_TOKEN_URL, data=token_data)
    token_info = response.json()
    session['token'] = token_info['access_token']
    session['refresh_token'] = token_info['refresh_token']
    return 'Logged in!'
