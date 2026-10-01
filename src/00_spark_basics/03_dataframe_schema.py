from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("DataFrameSchema")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Rahul", 75000),
    (2, "Karthik", 55000),
    (3, "Praveen", 85000),
    (4, "Manoj", 65000)
]

columns = ["employee_id", "employee_name", "salary"]

df = spark.createDataFrame(data, columns)

df.printSchema()

df.show()

spark.stop()