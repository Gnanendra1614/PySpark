from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("DistinctFunction")
    .master("local[*]")
    .getOrCreate()
)

data = [
    ("IT",),
    ("HR",),
    ("IT",),
    ("Finance",),
    ("HR",)
]

df = spark.createDataFrame(
    data,
    ["department"]
)

result = df.distinct()

result.show()

spark.stop()