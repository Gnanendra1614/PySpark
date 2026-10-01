<<<<<<< HEAD
# PySpark Practice

A structured PySpark learning and practice repository covering Spark fundamentals, file handling, transformations, joins, aggregations, window functions, advanced functions, nested data, UDFs, SCD, built-in functions, applyInPandas, and Medallion Architecture.

---

##  Project Overview

This repository contains hands-on PySpark programs created while learning Apache Spark and Data Engineering concepts.

The project follows a topic-by-topic approach, where each concept is implemented using a separate Python program for easy understanding and practice.

---

##  Technologies Used

- Python
- PySpark
- Apache Spark
- Pandas
- SQL
- Delta Lake
- Git & GitHub

---

#  Project Structure

```text
PySpark_practice
│
├── src
│   │
│   ├── 00_spark_basics
│   │   ├── 01_spark_session.py
│   │   ├── 02_create_dataframe.py
│   │   ├── 03_dataframe_schema.py
│   │   ├── 04_show_collect.py
│   │   └── 05_explicit_schema.py
│   │
│   ├── 01_reading_files
│   │   ├── 01_read_csv.py
│   │   ├── 02_read_json.py
│   │   ├── 03_read_parquet.py
│   │   └── 04_read_delta.py
│   │
│   ├── 01_writing_files
│   │   ├── 01_write_csv.py
│   │   ├── 02_write_json.py
│   │   ├── 03_write_parquet.py
│   │   └── 04_write_delta.py
│   │
│   ├── 02_basic_transformations
│   ├── 03_joins
│   ├── 04_aggregations
│   ├── 05_window_functions
│   ├── 06_advanced_functions
│   │
│   ├── 07_nested_data
│   │   ├── 01_arrays.py
│   │   ├── 02_structs.py
│   │   ├── 03_explode.py
│   │   ├── 04_from_json.py
│   │   ├── 05_nested_json_parsing.py
│   │   └── 06_accessing_nested_fields.py
│   │
│   ├── 08_udf
│   │   ├── 01_python_udf.py
│   │   ├── 02_udf_with_multiple_columns.py
│   │   ├── 03_udf_condition.py
│   │   └── 04_udf_vs_builtin.py
│   │
│   ├── 09_scd
│   │   ├── 01_type_1.py
│   │   ├── 02_type_2.py
│   │   └── 03_type_3.py
│   │
│   ├── 10_built_in_functions
│   │   ├── 01_limit_function.py
│   │   ├── 02_where_function.py
│   │   ├── 03_like_function.py
│   │   ├── 04_withColumnRenamed_function.py
│   │   ├── 05_drop_function.py
│   │   ├── 06_distinct_function.py
│   │   ├── 07_dropDuplicates_function.py
│   │   ├── 08_sort_function.py
│   │   ├── 09_fillna_function.py
│   │   ├── 10_dropna_function.py
│   │   ├── 11_union_function.py
│   │   ├── 12_unionAll_function.py
│   │   └── 13_pivot_function.py
│   │
│   ├── 11_applyinpandas
│   │   └── 01_applyinpandas_function.py
│   │
│   ├── 12_medallion_architeture
│   │   └── 01_medallion_architecture_implementation.py
│   │
│   └── data
│       ├── departments.csv
│       └── employees.csv
│
└── README.md
=======
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
>>>>>>> 710512d1ccdafe596179c8a0707b2bce8665d1ce
