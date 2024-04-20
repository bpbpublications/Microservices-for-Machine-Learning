
from delta.tables import DeltaTable
from pyspark.sql import SparkSession

# Initialize Spark session for Delta Lake operations
spark = SparkSession.builder.appName("DeltaLakeVersioning").config("spark.jars.packages", "io.delta:delta-core_2.12:1.0.0").getOrCreate()

# Initialize DeltaTable
delta_table = DeltaTable.forPath(spark, "/path/to/delta-table")

# Time-travel to version 1
df1 = spark.read.format("delta").option("versionAsOf", 1).load("/path/to/delta-table")

# Or via SQL
spark.sql("SELECT * FROM delta.`/path/to/delta-table@v1`")

# Writing Data to a Delta Table on HDFS
data = [("John", "Doe", 29), ("Jane", "Doe", 34)]
columns = ["first_name", "last_name", "age"]
df = spark.createDataFrame(data, columns)
df.write.format("delta").mode("overwrite").save("hdfs://namenode:port/path/to/delta-table")

# Write the DataFrame to a Delta table on S3
df.write.format("delta").mode("overwrite").save("s3a://your-bucket-name/path/to/delta-table")
