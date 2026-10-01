from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("PivotFunction")
    .master("local[*]")
    .getOrCreate()
)

data = [
    ("IT", 2024, 75000),
    ("IT", 2025, 80000),
    ("HR", 2024, 55000),
    ("HR", 2025, 60000),
    ("Finance", 2024, 85000),
    ("Finance", 2025, 90000)
]

df = spark.createDataFrame(
    data,
    ["department", "year", "salary"]
)

result = (
    df.groupBy("department")
    .pivot("year")
    .agg(F.sum("salary"))
)

result.show()

spark.stop()