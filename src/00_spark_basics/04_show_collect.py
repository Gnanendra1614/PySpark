from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("ShowCollect")
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

print("Using show():")
df.show()

print("Using collect():")

rows = df.collect()

for row in rows:
    print(row)

spark.stop()