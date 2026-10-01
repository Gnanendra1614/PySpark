from pyspark.sql import SparkSession
import pandas as pd

spark = (
    SparkSession.builder
    .appName("ApplyInPandasFunction")
    .master("local[*]")
    .getOrCreate()
)

data = [
    (1, "Rahul", "IT", 75000),
    (2, "Karthik", "IT", 85000),
    (3, "Praveen", "HR", 55000),
    (4, "Manoj", "HR", 65000),
    (5, "Harish", "Finance", 90000),
    (6, "Naveen", "Finance", 70000)
]

columns = [
    "employee_id",
    "employee_name",
    "department",
    "salary"
]

df = spark.createDataFrame(data, columns)

print("Original DataFrame:")
df.show()

# Function to process each department
def calculate_bonus(pdf):
    pdf["bonus"] = pdf["salary"] * 0.10
    pdf["salary_with_bonus"] = pdf["salary"] + pdf["bonus"]
    return pdf

result = (
    df.groupBy("department")
    .applyInPandas(
        calculate_bonus,
        schema="""
            employee_id long,
            employee_name string,
            department string,
            salary long,
            bonus double,
            salary_with_bonus double
        """
    )
)

print("Result using applyInPandas:")
result.show()

spark.stop()