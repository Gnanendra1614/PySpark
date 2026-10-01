from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("SortFunction")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Rahul", 75000),
    (2, "Karthik", 55000),
    (3, "Praveen", 85000),
    (4, "Manoj", 65000)
]

df = spark.createDataFrame(
    data,
    ["employee_id", "employee_name", "salary"]
)

result = df.sort(F.col("salary").desc())

result.show()

spark.stop()