from pyspark.sql import SparkSession

sc = SparkSession.builder.appName("wednesday").getOrCreate()

df = sc.read.parquet("src/data/survey_results_public.parquet")

# ---------- Write the dataframe to a PostgreSQL table ---------- #

# JDBC: Java Database Connectivity
# JDBC URL format: jdbc:postgresql://<host>:<port>/<database>

# Batch size: number of rows to be written per batch
# mode="append": append the dataframe to the existing table

# Write method on the dataframe allows us to write the dataframe to a database table
df.write.jdbc(
    url="jdbc:postgresql://localhost:5432/data-engg",
    table="survey_results_public",
    mode="append",
    properties={
        "user": "your_username",
        "password": "your_password",
        "driver": "org.postgresql.Driver",
        "batchsize": "10000",
    },
)
