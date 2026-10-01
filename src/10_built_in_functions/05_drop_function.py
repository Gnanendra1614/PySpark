from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("DropFunction")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Rahul", 75000, "IT"),
    (2, "Karthik", 55000, "HR"),
    (3, "Praveen", 85000, "Finance")
]

df = spark.createDataFrame(
    data,
    ["employee_id", "employee_name", "salary", "department"]
)

result = df.drop("department")

result.show()

spark.stop()