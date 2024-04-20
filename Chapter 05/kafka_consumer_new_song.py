
from kafka import KafkaConsumer

consumer = KafkaConsumer('new_song_added',
                         bootstrap_servers='localhost:9092')

for message in consumer:
    if message.value.decode('utf-8') == 'New song XYZ added':
        # Recommendation Service updates its model
        # Analytics Service logs the event
