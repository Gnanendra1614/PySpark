from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Show and Collect") \
    .getOrCreate()

data = [
    (1, "Gnanendra", 22, 50000),
    (2, "Rahul", 23, 60000),
    (3, "Priya", 21, 45000),
    (4, "Anil", 24, 70000)
]

columns = ["id", "name", "age", "salary"]

df = spark.createDataFrame(data, columns)

# show()
print("Using show():")
df.show()

# show first 2 rows
print("First 2 rows:")
df.show(2)

# collect()
print("Using collect():")

rows = df.collect()

for row in rows:
    print(row)

spark.stop()