# Step 1: Import necessary libraries
from pyspark.sql.session import SparkSession

# Step 2: Initialize a SparkSession
sc = SparkSession.builder.appName("sample").getOrCreate()

# Now we have different ways to create a DataFrame:
## 1. From a source file (CSV, JSON, Parquet, etc.)
## 2. From a database (MySQL, PostgreSQL, etc.)
## 3. Specify the data & schema explicitly
## 4. Specify the data & schema explicitly, and infer the data type

# --------------------------- METHOD: 1 From a source file --------------------------- #

# Let's create a DataFrame from a CSV file
df1 = sc.read.csv("src/data/survey_results_public.csv", header=True, inferSchema=True)

# Similarly, we can create a DataFrame from a JSON or Parquet file:
# >>> df = sc.read.json("src/data/survey_results_public.json")
# >>> df = sc.read.parquet("src/data/survey_results_public.parquet")

# Print the schema of the DataFrame
df1.printSchema()

# ---------------------------- METHOD: 2 From a database ----------------------------- #

# Note: Make sure to update the database credentials below
df2 = (
    sc.read.format("jdbc")
    .option("url", "jdbc:postgresql://localhost:5432/data-engg")
    .option("dbtable", "survey_results_public")
    .option("user", "")  # Update the username
    .option("password", "")  # Update the password
    .load()
)

df2.printSchema()

# ------------------ METHOD: 3 Specify the data & schema explicitly ------------------ #
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

data = [
    (1, "John Doe", "Developer"),
    (2, "Jack Doe", "Manager"),
    (3, "Jane Doe", "Analyst"),
]

# Define the schema
defined_schema = StructType(
    [
        StructField("id", IntegerType(), True),
        StructField("name", StringType(), True),
        StructField("role", StringType(), True),
    ]
)

df3 = sc.createDataFrame(data=data, schema=defined_schema)

# Print the schema of the DataFrame
df3.printSchema()

# ----- METHOD: 4 Specify the data & schema explicitly, and infer the data type ------ #

inferred_schema = ["id", "name", "role"]

df4 = sc.createDataFrame(data=data, schema=inferred_schema)

# Print the schema of the DataFrame
df4.printSchema()
