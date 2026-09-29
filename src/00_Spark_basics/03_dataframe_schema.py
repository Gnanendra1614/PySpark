from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("DataFrame Schema") \
    .getOrCreate()

data = [
    (1, "Gnanendra", 22, 50000),
    (2, "Rahul", 23, 60000),
    (3, "Priya", 21, 45000),
    (4, "Anil", 24, 70000)
]

columns = ["id", "name", "age", "salary"]

df = spark.createDataFrame(data, columns)

# Display data
df.show()

# Display schema
df.printSchema()

# Display column names
print("Columns:", df.columns)

# Display data types
print("Data Types:", df.dtypes)

spark.stop()