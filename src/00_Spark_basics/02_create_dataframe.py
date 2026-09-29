from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Create DataFrame") \
    .getOrCreate()

# Sample data
data = [
    (1, "Gnanendra", 22, 50000),
    (2, "Raju", 23, 60000),
    (3, "Sarath", 21, 45000),
    (4, "Dwaraka", 24, 70000)
]

# Column names
columns = ["id", "name", "age", "salary"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Display DataFrame
df.show()

spark.stop()