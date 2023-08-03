# Write DataFrame to a Database Table

This documentation explains a PySpark script that demonstrates reading data from a Parquet file and writing it to a PostgreSQL table using JDBC (Java Database Connectivity). The script leverages Apache Spark's DataFrame API to interact with distributed data and showcases the seamless integration of Spark with external databases.

## Prerequisites

1. PostgreSQL installed and accessible.

## Script Explanation

```python
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
```

The script will read the data from the "survey_results_public.parquet" file, and then write it to the specified PostgreSQL table named "survey_results_public" in "data-engg" database using "append" mode. The data will be appended to the existing data in the table.

Learn more about JDBC here: https://www.javatpoint.com/java-jdbc

## How to Run the script

```bash
python examples/06_write_dataframe/write_dataframe.py

# or if you are using docker run:
spark-submit examples/06_write_dataframe/write_dataframe.py
```
