
# In Recommendation Service
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/recommendations')
def get_recommendation():
    user_id = '123'
    # Call the User Service to get user information
    response = requests.get(f'http://user-service:5000/users/{user_id}')
    user_info = response.json()
    # Process the recommendation based on user_info
    recommended_song = "Song A"
    return jsonify({'recommended_song': recommended_song})

if __name__ == '__main__':
    app.run(port=5001)
