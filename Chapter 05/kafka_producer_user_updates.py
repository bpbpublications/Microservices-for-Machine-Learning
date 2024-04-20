
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('user_updates', key=b'user123', value=b'New user registered')
