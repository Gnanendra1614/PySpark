from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("DropDuplicatesFunction")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Rahul", "IT"),
    (2, "Karthik", "HR"),
    (1, "Rahul", "IT"),
    (3, "Praveen", "Finance"),
    (2, "Karthik", "HR")
]

df = spark.createDataFrame(
    data,
    ["employee_id", "employee_name", "department"]
)

result = df.dropDuplicates()

result.show()

spark.stop()