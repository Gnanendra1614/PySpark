# PySpark Practice

A hands-on PySpark learning project covering file reading, DataFrame transformations, and joins using local PySpark.

## Project Structure

```text
PySpark_practice/
├── Data/
│   ├── departments.csv
│   └── employees.csv
│
├── src/
│   ├── 01_Reading_files/
│   │   ├── 01_read_csv.py
│   │   ├── 02_read_json.py
│   │   ├── 03_read_parquet.py
│   │   └── 04_read_delta.py
│   │
│   ├── 02_Basic_Transformations/
│   │   ├── 01_select.py
│   │   ├── 02_filter.py
│   │   ├── 03_where.py
│   │   ├── 04_withcolumn.py
│   │   ├── 05_when_otherwise.py
│   │   ├── 06_column_expressions.py
│   │   └── 07_aliases.py
│   │
│   └── 03_Joins/
│       ├── 01_inner_join.py
│       ├── 02_left_join.py
│       ├── 03_outer_join.py
│       ├── 04_semi_join.py
│       ├── 05_anti_join.py
│       ├── 06_join_condition.py
│       ├── 07_duplicate_columns.py
│       └── 08_null_values_in_joins.py
│
└── README.md


## About This Project

This repository contains my hands-on practice and learning journey with **PySpark** and **Apache Spark**.

The main objective of this project is to understand how PySpark is used for processing and transforming data using DataFrames. The project covers file reading, DataFrame transformations, conditional operations, and different types of joins.

I have organized each concept into separate Python files so that every topic can be practiced and understood independently.

## Project Objectives

- Understand the fundamentals of PySpark and Spark DataFrames.
- Practice reading different data formats.
- Perform DataFrame transformations and filtering.
- Create derived columns using PySpark functions.
- Apply conditional logic using `when()` and `otherwise()`.
- Understand and implement different types of joins.
- Handle duplicate columns after joins.
- Understand NULL values in joined DataFrames.
- Practice writing clean and reusable PySpark code.
- Maintain the learning work using Git and GitHub.

## What I Learned

Through this project, I practiced:

- Reading CSV, JSON, Parquet, and Delta files.
- Working with Spark DataFrames.
- Selecting and filtering data.
- Creating new columns using `withColumn()`.
- Applying conditional logic.
- Using column expressions and aliases.
- Performing Inner, Left, Full Outer, Semi, and Anti joins.
- Defining explicit join conditions.
- Handling duplicate columns.
- Handling NULL values.
- Running PySpark programs locally using `local[*]`.

## Data Used

The project uses sample employee and department datasets.

The `employees.csv` file contains:

- Employee ID
- Employee Name
- Department ID
- Salary
- City

The `departments.csv` file contains:

- Department ID
- Department Name

The common key between the two datasets is:

```text
department_id

