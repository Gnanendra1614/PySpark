from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ReadCSV").master("local[*]").getOrCreate()

DATA_PATH = r"C:\Users\gnane\OneDrive - DIGGIBYTE TECHNOLOGIES PRIVATE LIMITED"

df = (
    spark.read.format("csv").option("header", True).option("inferSchema", True)
    .load(DATA_PATH + r"\DATA.csv")
)

df.printSchema()
df.show(truncate=False)

spark.stop()
# Practice: Reading CSV files with PySpark
