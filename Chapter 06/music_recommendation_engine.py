
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.sql.functions import col
from pyspark.ml.regression import LinearRegression

# Initialize Spark Session
spark = SparkSession.builder.appName("MusicRecommendationEngine").getOrCreate()

# Read Data
data = spark.read.csv("path_to_your_data", header=True, inferSchema=True)

# ALS Model Initialization and Fitting
als = ALS(maxIter=5, regParam=0.01, userCol="userId", itemCol="musicId", ratingCol="rating")
model_als = als.fit(data)

# Generate ALS Recommendations
recommendations_als = model_als.recommendForAllUsers(10)
recommendations_als.show()

# Data Preparation and Feature Engineering
df = spark.read.format("parquet").load("hdfs://namenode:port/path/to/data")
cleaned_df = df.filter(col("user_id").isNotNull())
transformed_df = cleaned_df.withColumn("new_feature", col("existing_feature") * 2)

# Linear Regression Model Training
lr = LinearRegression(featuresCol='features', labelCol='label')
model_lr = lr.fit(transformed_df)

# Save the Model
model_lr.save("hdfs://namenode:port/path/to/model")
