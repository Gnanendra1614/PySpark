PySpark Practice Repository

A comprehensive collection of PySpark scripts designed to help data engineers, data scientists, and developers learn and practice PySpark concepts—ranging from basic DataFrame operations to advanced Data Lakehouse implementations (Medallion Architecture, SCD Types, Window Functions, and Pandas API on Spark).

Repository Structure

PySpark_practice/
└── src/
    ├── 00_spark_basics/            # SparkSession creation, DataFrame initialization, schemas
    ├── 01_reading_files/           # Reading CSV, JSON, Parquet, Delta
    ├── 01_writing_files/           # Writing CSV, JSON, Parquet, Delta
    ├── 02_basic_transformations/   # select, filter, where, withColumn, when/otherwise, aliases
    ├── 03_joins/                   # Inner, Left, Outer, Semi, Anti joins, duplicate handling
    ├── 04_aggregations/            # groupBy, sum, avg, count, min/max, multiple aggregations
    ├── 05_window_functions/        # row_number, rank, dense_rank, lag, lead, running totals
    ├── 06_advanced_functions/      # String, numeric, date-time, and array functions
    ├── 07_nested_data/             # Arrays, Structs, explode, from_json, nested JSON parsing
    ├── 08_udf/                     # Python UDFs, multi-column UDFs, UDFs vs built-in functions
    ├── 09_scd/                     # Slowly Changing Dimensions (Type 1, Type 2, Type 3)
    ├── 10_built_in_functions/      # limit, drop, distinct, dropDuplicates, fillna, union, pivot
    ├── 11_applyinpandas/           # PySpark applyInPandas execution
    ├── 12_medallion_architeture/   # Medallion Architecture (Bronze, Silver, Gold layers)
    └── data/                       # Sample datasets (employees.csv, departments.csv)
