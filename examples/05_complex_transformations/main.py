from pyspark.sql import SparkSession
import pyspark.sql.functions as f

sc = SparkSession.builder.appName("wednesday").getOrCreate()

survey_df = sc.read.parquet(
    "src/data/survey_results_public.parquet", header=True, inferSchema=True
)

customers_df = sc.read.csv("src/data/customers.csv", header=True, inferSchema=True)

# Join the two dataframes on customers(id) and survey_df(ResponseId)
joined_df = survey_df.join(
    customers_df, survey_df.ResponseId == customers_df.id, how="left"
)

columns_to_select = [
    "ResponseId",
    "Country",
    "first_name",
    "last_name",
    "email",
    "phone",
    "OrgSize",
    "PurchaseInfluence",
]

# Select the columns from the joined_df
selected_df = joined_df.select(columns_to_select)

# Filter the records where first_name & last_name is not null
selected_df = selected_df.filter(
    selected_df.first_name.isNotNull() & selected_df.last_name.isNotNull()
)

# Join the two columns first_name & last_name and create a new column name full_name
# and drop the first_name & last_name columns
selected_df = selected_df.withColumn(
    "full_name", f.concat(f.col("first_name"), f.lit(" "), f.col("last_name"))
).drop("first_name", "last_name")

# Validate the email column using regex
EMAIL_VALIDATION_REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
# Filter the records where email is not null and email matches the regex
selected_df = selected_df.filter(
    selected_df.email.isNotNull() & f.col("email").rlike(EMAIL_VALIDATION_REGEX)
)

selected_df.printSchema()
selected_df.show()
