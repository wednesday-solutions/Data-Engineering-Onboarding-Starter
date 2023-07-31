from pyspark.sql.session import SparkSession
import pyspark.sql.functions as f

sc = SparkSession.builder.appName("wednesday").getOrCreate()

df = sc.read.csv("src/data/survey_results_public.csv", header=True, inferSchema=True)

# ------------------------------ PART 1 ------------------------------ #

# Lets rename the column `YearsCodePro` to `Experience`
df = df.withColumnRenamed("YearsCodePro", "Experience")

# Lets check the type of the column `Experience`
print(df.select("Experience").dtypes)
# The output should look like this: [('Experience', 'string')]
# The column `Experience` is of type string, but we want it to be of type integer,
# so we can do some calculations on it. Lets convert it to integer.

df = df.withColumn("Experience", f.col("Experience").cast("integer"))

# Lets check the type of the column `Experience` again
print(df.select("Experience").dtypes)
# The output should look like this: [('Experience', 'int')]

# ------------------------------ PART 2 ------------------------------ #

# Lets create a new column `IsSenior` which will be a boolean column.
# It will be true if the person has more than 10 years of experience, otherwise false.

df = df.withColumn("IsSenior", f.col("Experience") > 10)

df.select("Experience", "IsSenior").show(10)

# ------------------------------ PART 3 ------------------------------ #

# Lets create a new column `BlockchainInterest` which will be an integer column. It will be derived from the column `Blockchain`.
# This column will hold a value between 0 to 4, where:
# 0 - Very unfavorable
# 1 - Unfavorable
# 2 - Indifferent
# 3 - Favorable
# 4 - Very favorable

df = df.withColumn(
    "BlockchainInterest",
    f.when(f.col("Blockchain") == "Very unfavorable", 0)
    .when(f.col("Blockchain") == "Unfavorable", 1)
    .when(f.col("Blockchain") == "Indifferent", 2)
    .when(f.col("Blockchain") == "Favorable", 3)
    .when(f.col("Blockchain") == "Very favorable", 4),
)

df.select("Blockchain", "BlockchainInterest").show(10)
