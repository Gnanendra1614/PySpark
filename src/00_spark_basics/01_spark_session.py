from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("SparkSessionPractice")
    .master("local[*]")
    .getOrCreate()
)

print("Spark Session Created Successfully")
print("Spark Version:", spark.version)

spark.stop()