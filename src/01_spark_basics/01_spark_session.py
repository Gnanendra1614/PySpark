from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("Spark Basics") \
    .getOrCreate()

print("Spark Session Created Successfully")

print("Spark Version:", spark.version)

# Stop Spark Session
spark.stop()