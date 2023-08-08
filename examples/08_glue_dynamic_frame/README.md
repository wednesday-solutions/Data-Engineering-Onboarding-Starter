## Creating a Glue DynamicFrame

In this example, we will create a Glue dynamic frame using a Data Catalog as source. We will then convert the dynamic frame to a PySpark DataFrame and perform some transformations on it.

## Glue Dynamic Frame vs Spark DataFrame

A Glue dynamic frame is similar to a Spark DataFrame, except that each record is self-describing, so no schema is required initially. This makes it easier to deal with semi-structured data, such as JSON data. DynamicFrames are designed to provide maximum flexibility when dealing with messy data that may lack a declared schema.

On the other hand, Spark DataFrames are designed to provide a typed view of structured data, and structured data is the most common use case for Spark. Spark DataFrames are also more performant than DynamicFrames. Hence, you would typically convert a DynamicFrame to a Spark DataFrame as soon as possible in your ETL script.


```python
data_catalog = glue_context.create_dynamic_frame_from_catalog(
    database="data-engg-starter",         # Database name in Data Catalog
    table_name="survey_results_public",   # Table name in Data Catalog
    transformation_ctx="data_catalog",    # Transformation context
)
```

You will notice the `create_dynamic_frame_from_catalog()` method which is creating a dynamic frame from a Data Catalog. You may wonder what Data Catalog is?

When we are working locally, we can use a CSV file as source. But in production, we could be dealing with huge datasets which won't be a single file. In such cases, we can use a Data Catalog as source. A Data Catalog is a central repository of metadata about your data. Consider it as a database of your source data. Only difference is that it does not contain the actual data. Rather, it contains the metadata about your data like table definitions, schema, and other control information. You can use the Data Catalog as a source for your ETL jobs.

So, if you have 10 Million records across 100 CSV files, you can create a Data Catalog table with the schema of the CSV files. Then, you can use this table as source for your ETL jobs. This way, you don't have to worry about the location of the CSV files or the schema of the CSV files. You just need to know the name of the table in the Data Catalog.

Follow the onboarding document to learn more about Data Catalog.
