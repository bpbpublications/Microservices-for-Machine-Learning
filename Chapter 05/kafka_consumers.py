
from kafka import KafkaConsumer

# Consumer for user updates
consumer_user_updates = KafkaConsumer('user_updates',
                                      bootstrap_servers='localhost:9092')

for message in consumer_user_updates:
    print(f"Received user update message: {message.value.decode('utf-8')}")

# Consumer for new song added
consumer_new_song = KafkaConsumer('new_song_added',
                                  bootstrap_servers='localhost:9092')

for message in consumer_new_song:
    if message.value.decode('utf-8') == 'New song XYZ added':
        # Recommendation Service updates its model
        # Analytics Service logs the event
        print(f"Received new song message: {message.value.decode('utf-8')}")
