
from kafka import KafkaProducer
import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType, StructField, StringType

# Kafka Producer for simulating user interactions
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

interaction = {
    'userID': 'user123',
    'songID': 'songXYZ',
    'interactionType': 'like'
}

producer.send('user_interactions', value=interaction)
producer.close()

# Spark Session initialization for Structured Streaming
spark = SparkSession.builder.appName("MusicRecommendationStream").getOrCreate()

# Schema definition for the incoming data
schema = StructType([
    StructField("userID", StringType(), True),
    StructField("songID", StringType(), True),
    StructField("interactionType", StringType(), True)
])

# Read the Kafka Stream
raw_stream = spark     .readStream     .format("kafka")     .option("kafka.bootstrap.servers", "localhost:9092")     .option("subscribe", "user_interactions")     .load()

# Deserialize the JSON data
json_stream = raw_stream     .selectExpr("CAST(value AS STRING)")     .select(from_json("value", schema).alias("data"))     .select("data.*")

# Perform some transformation to update recommendation model
interaction_count = json_stream.groupBy("songID", "interactionType").count()

# Writing the stream output to the console
query = interaction_count     .writeStream     .outputMode("complete")     .format("console")     .start()

query.awaitTermination()
