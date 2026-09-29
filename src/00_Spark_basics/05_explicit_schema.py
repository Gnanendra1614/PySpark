from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    DoubleType
)

spark = SparkSession.builder \
    .appName("Explicit Schema") \
    .getOrCreate()

# Data
data = [
    (1, "Gnanendra", 22, 50000.0),
    (2, "Rahul", 23, 60000.0),
    (3, "Priya", 21, 45000.0),
    (4, "Anil", 24, 70000.0)
]

# Explicit schema
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("salary", DoubleType(), True)
])

# Create DataFrame using explicit schema
df = spark.createDataFrame(data, schema)

# Display data
df.show()

# Display schema
df.printSchema()

spark.stop()