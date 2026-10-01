from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = (
    SparkSession.builder
    .appName("MedallionArchitecture")
    .master("local[*]")
    .getOrCreate()
)

# -----------------------------
# BRONZE LAYER
# -----------------------------

data = [
    (1, "Rahul", "IT", 75000, "Madanapalle"),
    (2, "Karthik", "HR", 55000, "Chittoor"),
    (3, "Praveen", "Finance", 85000, "Tirupati"),
    (4, "Manoj", "Sales", 65000, "Kadapa"),
    (5, "Harish", "IT", 90000, "Pileru")
]

columns = [
    "employee_id",
    "employee_name",
    "department",
    "salary",
    "city"
]

bronze_df = spark.createDataFrame(data, columns)

print("===== BRONZE LAYER =====")
bronze_df.show()

# -----------------------------
# SILVER LAYER
# -----------------------------

silver_df = (
    bronze_df
    .dropDuplicates(["employee_id"])
    .withColumn(
        "employee_name",
        F.trim(F.col("employee_name"))
    )
    .withColumn(
        "department",
        F.trim(F.col("department"))
    )
    .withColumn(
        "salary",
        F.col("salary").cast("double")
    )
    .filter(F.col("employee_id").isNotNull())
)

print("===== SILVER LAYER =====")
silver_df.show()

# -----------------------------
# GOLD LAYER
# -----------------------------

gold_df = (
    silver_df
    .groupBy("department")
    .agg(
        F.count("employee_id").alias("employee_count"),
        F.sum("salary").alias("total_salary"),
        F.avg("salary").alias("average_salary"),
        F.max("salary").alias("maximum_salary"),
        F.min("salary").alias("minimum_salary")
    )
)

print("===== GOLD LAYER =====")
gold_df.show()

# -----------------------------
# WRITE GOLD DATA
# -----------------------------

gold_df.write \
    .mode("overwrite") \
    .parquet("output/gold_department_summary")

spark.stop()