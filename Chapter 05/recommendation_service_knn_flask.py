
from flask import Flask, jsonify, request
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

app = Flask(__name__)

userPreferencesDao = UserPreferencesDao()
songMetadataDao = SongMetadataDao()
recommendationLogDao = RecommendationLogDao()
externalRecommender = ExternalRecommender()

# Sample KNN model for demonstration
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(np.array([[0, 1], [1, 0], [1, 1], [0, 0]]), np.array([1, 2, 1, 2]))

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_id = data['user_id']
    user_data = np.array([data['features']])
    
    # Use KNN model for recommendation
    song_id = knn.predict(user_data)[0]
    
    # Log the recommendation
    recommendationLogDao.add_log(user_id, song_id)
    
    # Get song metadata
    song = songMetadataDao.get_song(song_id)
    
    return jsonify({'recommendation': song})

@app.route('/recommend/external', methods=['GET'])
def recommend_external():
    user_id = request.args.get('user_id')
    
    # Call external recommendation service
    recommendation = externalRecommender.get_recommendation(user_id)
    
    # Log the recommendation
    recommendationLogDao.add_log(user_id, recommendation['id'])
    
    return jsonify({'recommendation': recommendation})

if __name__ == '__main__':
    app.run(port=5005)
