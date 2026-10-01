from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("DropnaFunction")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Rahul", 75000),
    (2, "Karthik", None),
    (3, "Praveen", 85000),
    (4, None, 65000)
]

df = spark.createDataFrame(
    data,
    ["employee_id", "employee_name", "salary"]
)

result = df.dropna()

result.show()

spark.stop()