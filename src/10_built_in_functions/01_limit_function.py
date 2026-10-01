from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("LimitFunction")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Rahul", 75000),
    (2, "Karthik", 55000),
    (3, "Praveen", 85000),
    (4, "Manoj", 65000),
    (5, "Harish", 90000)
]

df = spark.createDataFrame(
    data,
    ["employee_id", "employee_name", "salary"]
)

result = df.limit(3)

result.show()

spark.stop()