
# Example using Apache Kafka for real-time data ingestion
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('user_interactions', b'user1,play,song1')
