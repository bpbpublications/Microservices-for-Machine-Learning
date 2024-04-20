
from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler

# Initialize a Spark session
spark = SparkSession.builder \
    .appName('MusicRecommendationBatchProcessing') \
    .getOrCreate()

# Read dataset from HDFS
hdfs_path = "hdfs://localhost:9000/hdfspath/to/user_behaviors.csv"
df = spark.read.csv(hdfs_path, header=True, inferSchema=True)

# Prepare data for ML model
feature_cols = ['listening_time', 'genre_preference', 'user_activity']
vec_assembler = VectorAssembler(inputCols=feature_cols, outputCol="features")
df_kmeans = vec_assembler.transform(df).select('user_id', 'features')

# Train k-means model
kmeans = KMeans().setK(3).setSeed(1)
model = kmeans.fit(df_kmeans)

# Make predictions
predictions = model.transform(df_kmeans)

# Generate recommendations
def get_batch_recommendations(df):
    popular_songs = {0: "SongA", 1: "SongB", 2: "SongC"}
    recommendations = []
    for row in df.rdd.collect():
        user_id = row['user_id']
        cluster = row['prediction']
        recommendations.append((user_id, popular_songs[cluster]))
    return recommendations

# Get recommendations
batch_recommendations = get_batch_recommendations(predictions)

# Save to HDFS
output_hdfs_path = "hdfs://localhost:9000/hdfspath/to/recommendations"
spark.createDataFrame(batch_recommendations, ["user_id", "song_id"]).write.csv(output_hdfs_path)
