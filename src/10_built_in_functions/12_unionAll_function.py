from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("UnionAllFunction")
    .master("local[*]")
    .getOrCreate()
)

data1 = [
    (1, "Rahul", 75000),
    (2, "Karthik", 55000)
]

data2 = [
    (3, "Praveen", 85000),
    (4, "Manoj", 65000)
]

columns = ["employee_id", "employee_name", "salary"]

df1 = spark.createDataFrame(data1, columns)
df2 = spark.createDataFrame(data2, columns)

result = df1.unionAll(df2)

result.show()

spark.stop()