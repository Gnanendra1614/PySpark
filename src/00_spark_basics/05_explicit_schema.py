from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    DoubleType
)

spark = (
    SparkSession.builder
    .appName("ExplicitSchema")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Rahul", 75000.0),
    (2, "Karthik", 55000.0),
    (3, "Praveen", 85000.0),
    (4, "Manoj", 65000.0)
]

schema = StructType([
    StructField("employee_id", IntegerType(), True),
    StructField("employee_name", StringType(), True),
    StructField("salary", DoubleType(), True)
])

df = spark.createDataFrame(data, schema)

df.printSchema()

df.show()

spark.stop()