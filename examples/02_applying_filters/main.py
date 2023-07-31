# Step 1: Imports
# --------------------------------------------------------------------------------------- #
# Spark session is an entry point for a pyspark script, it allows you to create
# dataframes and performs transformations on it
from pyspark.sql.session import SparkSession

# sql.function provides basic utility functions like:
# - uppercase/lowercase, cast, date conversion, joins, etc.
import pyspark.sql.functions as f

# Step 2: Creating a dataframe
# --------------------------------------------------------------------------------------- #
# This starts the Spark cluster.
sc = SparkSession.builder.appName("wednesday").getOrCreate()

# Step 3: Importing data from CSV source
# --------------------------------------------------------------------------------------- #
# - When header=True, we tell pyspark that the source CSV contains a header row. So that, trow
#   Won't be considered as a data row.
# - When inferSchema=True, we tell pyspark to infer the data type of column automatically.
df = sc.read.csv("src/data/survey_results_public.csv", header=True, inferSchema=True)

# Step 4: Applying filters
# --------------------------------------------------------------------------------------- #
# Select only those rows where column `Country` is `Australia`
df = df.filter(f.col("Country").eqNullSafe("Australia"))
# Select only those rows where column `OpSysPersonal use` is `macOS`
df = df.filter(f.col("OpSysPersonal use").eqNullSafe("macOS"))

# Step 5: Print Dataframe on the console
# --------------------------------------------------------------------------------------- #
df.select("Country", "OpSysPersonal use").show()
