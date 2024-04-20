
from flask import Flask
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.secret_key = 'YOUR_SECRET_KEY'
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
AUTH_URL = 'https://authorization-server.com/oauth/authorize'
TOKEN_URL = 'https://authorization-server.com/oauth/token'

oauth = OAuth(app)
authorization_server = oauth.remote_app(
    'AuthorizationServer',
    consumer_key=CLIENT_ID,
    consumer_secret=CLIENT_SECRET,
    request_token_params={'scope': 'user profile'},
    base_url='https://authorization-server.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url=TOKEN_URL,
    authorize_url=AUTH_URL,
)

@app.route('/login')
def login():
    return authorization_server.authorize(callback=url_for('callback'))
