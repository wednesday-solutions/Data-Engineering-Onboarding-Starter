# PySpark DataFrame


A PySpark DataFrame is a distributed collection of data organized into named columns. It is similar to a table in a relational database or a spreadsheet in Excel. DataFrames are designed to work in a distributed computing environment using Apache Spark. They can process large datasets across multiple nodes in a cluster, enabling scalable and parallel data processing. This makes them a good choice for working with big data.

## Methods of DataFrame Creation

### Method 1: From a Source File

This method creates a DataFrame by reading data from a source file (CSV, JSON, Parquet, etc.)

```python
# Using CSV source file
df = sc.read.csv("src/data/survey_results_public.csv", header=True, inferSchema=True)

# Using JSON source file
df = sc.read.json("src/data/survey_results_public.json")

# Using Parquet source file
df = sc.read.parquet("src/data/survey_results_public.parquet")

```

### Method 2: From a Database

This method creates a DataFrame by connecting to a database (e.g., MySQL, PostgreSQL) and loading data from a specified table using JDBC.

```python
df = (
    sc.read.format("jdbc")
    .option("url", "jdbc:postgresql://localhost:5432/data-engg")
    .option("dbtable", "your_table_name")
    .option("user", "your_db_username")
    .option("password", "your_db_password")
    .load()
)
```

### Method 3: Specify the Data & Schema Explicitly

This method manually specifies the data and schema to create a DataFrame. You need to define the data as a list of tuples and the schema using the `StructType` and `StructField` classes.

```python
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

data = [
    (1, "John Doe", "Developer"),
    (2, "Jack Doe", "Manager"),
    (3, "Jane Doe", "Analyst"),
]

# Define the schema
schema = StructType(
    [
        StructField("id", IntegerType(), True),
        StructField("name", StringType(), True),
        StructField("role", StringType(), True),
    ]
)

df = sc.createDataFrame(data=data, schema=schema)

```

### Method 4: Specify the Data & Schema Explicitly and Infer Data Types

This method is similar to Method 3, but instead of explicitly defining the data types in the schema, it infers the data types based on the provided data.

```python
data = [
    (1, "John Doe", "Developer"),
    (2, "Jack Doe", "Manager"),
    (3, "Jane Doe", "Analyst"),
]

schema = ["id", "name", "role"]

df = sc.createDataFrame(data=data, schema=schema)
```
