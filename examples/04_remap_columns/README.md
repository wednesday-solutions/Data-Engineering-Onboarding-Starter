# Remap | Column Name Normalization

This documentation explains a PySpark script that reads data from a Parquet file, performs column name normalization, and writes the DataFrame back to a new Parquet file. The script leverages Apache Spark's DataFrame API to interact with distributed data and utilizes the `re` library for regular expression-based column name normalization.


## Script Explanation

```python
df = df.toDF(*[re.sub("[^\w]", "_", c) for c in df.columns])
```

### Why Normalize Column Names?

Column names are an important part of a DataFrame. They are used to identify and access the data in a DataFrame. Column names are also used to reference columns in SQL queries. Therefore, it is important to have consistent and meaningful column names. Also, many formats (e.g., Parquet, Avro) do not support special characters in column names. Therefore, it is a good practice to normalize column names before writing a DataFrame to a file or database.

## How to Run the script

```bash
python examples/04_remap_columns/remap_columns.py

# or if you are using docker run:
spark-submit examples/04_remap_columns/remap_columns.py
```
