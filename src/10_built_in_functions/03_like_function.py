from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("LikeFunction")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Rahul", "Madanapalle"),
    (2, "Karthik", "Chittoor"),
    (3, "Praveen", "Tirupati"),
    (4, "Manoj", "Kadapa"),
    (5, "Harish", "Madanapalle")
]

df = spark.createDataFrame(
    data,
    ["employee_id", "employee_name", "city"]
)

result = df.filter(
    df["employee_name"].like("Ra%")
)

result.show()

spark.stop()