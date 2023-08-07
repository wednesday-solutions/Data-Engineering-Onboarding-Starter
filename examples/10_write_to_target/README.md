## Writing DynamicFiles to a Target

This example demonstrates how to write a DynamicFile to a target. In this example, we will write the DynamicFrame to an Amazon S3 bucket. We will use the `write_dynamic_frame` method from the `glue_context` class to write the DynamicFrame to the target.

### Implementation

AWS Glue `glue_context` class provides a method to write a DynamicFrame to a target. This method takes the following parameters:

- frame: The DynamicFrame to write to the target.
- connection_type: The type of connection to use to write the DynamicFrame to the target. This can be one of the following values:
    - `s3`: Write the DynamicFrame to an Amazon S3 bucket.
    - `glue`: Write the DynamicFrame to an AWS Glue Data Catalog table.
    - `dynamodb`: Write the DynamicFrame to an Amazon DynamoDB table.
    - `jdbc`: Write the DynamicFrame to a JDBC connection.
    - `custom`: Write the DynamicFrame to a custom connection.

- connection_options: A dictionary that contains the connection options. The connection options depend on the type of connection that you are using. For example, if you are using an Amazon S3 connection, you will need to provide the following options:

    - `path`: The path to the Amazon S3 bucket.
    - `partitionKeys`: A list of partition keys (optional)

```python
glue_context.write_dynamic_frame.from_options(
    frame=raw_data,
    connection_type="s3",
    connection_options={"path": "s3://sample-glue-wednesday/data/"},
    format="parquet",
)
```
