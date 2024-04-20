
import redis
import json
import time

# Connect to Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

def recommend_songs(user_id):
    # Simulate some heavy computation to generate recommendations
    time.sleep(2)
    return ["Song1", "Song2", "Song3"]

def get_recommendations_with_caching(user_id):
    # Use user_id as the cache key
    cache_key = f"recommendations:{user_id}"
    
    # Try to get cached result first
    cached_result = r.get(cache_key)
    if cached_result:
        print("Cache hit!")
        return json.loads(cached_result)
    
    # If not in cache, generate recommendations
    print("Cache miss!")
    recommendations = recommend_songs(user_id)
    
    # Store the result in cache for 1 hour
    r.setex(cache_key, 3600, json.dumps(recommendations))
    
    return recommendations

# Test the function
print(get_recommendations_with_caching("user123"))  # Cache miss!
print(get_recommendations_with_caching("user123"))  # Cache hit!
