
from flask import Flask, redirect, request, session
import requests

app = Flask(__name__)
CLIENT_ID = 'YOUR_CLIENT_ID'
REDIRECT_URI = 'http://localhost:5000/callback'
AUTH_URL = 'https://authorization-server.com/oauth/authorize'

@app.route('/login')
def login():
    return redirect(f'{AUTH_URL}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}')

PROFILE_URL = 'https://authorization-server.com/user/profile'

@app.route('/profile')
def profile():
    headers = {'Authorization': f'Bearer {session["token"]}'}
    response = requests.get(PROFILE_URL, headers=headers)
    return response.json()
