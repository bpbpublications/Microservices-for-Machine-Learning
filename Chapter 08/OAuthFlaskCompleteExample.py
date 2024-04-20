
from flask import Flask, redirect, request, session, url_for
import requests

app = Flask(__name__)
app.secret_key = 'YOUR_SECRET_KEY'  # Needed for session management
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'http://localhost:5000/callback'
AUTH_URL = 'https://authorization-server.com/oauth/authorize'
TOKEN_URL = 'https://authorization-server.com/oauth/token'

@app.route('/login')
def login():
    return redirect(f'{AUTH_URL}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code')

@app.route('/callback')
def callback():
    code = request.args.get('code')
    payload = {
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'redirect_uri': REDIRECT_URI
    }
    response = requests.post(TOKEN_URL, data=payload)
    token_info = response.json()
    session['token'] = token_info['access_token']
    return 'Logged in successfully!'

PROFILE_URL = 'https://authorization-server.com/user/profile'

@app.route('/profile')
def profile():
    headers = {'Authorization': f'Bearer {session["token"]}'}
    response = requests.get(PROFILE_URL, headers=headers)
    return response.json()
