from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("WithColumnRenamed")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Rahul", 75000),
    (2, "Karthik", 55000),
    (3, "Praveen", 85000)
]

df = spark.createDataFrame(
    data,
    ["employee_id", "employee_name", "salary"]
)

result = df.withColumnRenamed(
    "employee_name",
    "name"
)

result.show()

spark.stop()