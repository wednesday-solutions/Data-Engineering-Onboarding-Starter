## Apply Mappings to a DynamicFrame

In this example, we will apply mappings to a Glue DynamicFrame. This is useful when you want to change the schema of a DynamicFrame. For example, you may want to change the data type of a column or rename a column. Or if you want to change the data type of a column from string to a date or timestamp. This is a common use case when you are reading data from a database and the date or timestamp is stored as a string.

In many scenarios, you will notice that Glue Crawlers will not infer the correct data type for a column. For example, if you have a column that contains a date or timestamp, the crawler will infer the data type as string. This is because the crawler does not know the format of the date or timestamp. In this case, you will need to apply mappings to the DynamicFrame to change the data type of the column.

## Implementation

AWS Glue `transformations` class provides a method to apply mappings to a DynamicFrame. This method takes the following parameters:

- frame: The DynamicFrame to apply the mappings to.
- mappings: A list of tuples that contains the mapping information. Each tuple contains the following information:
    - `source`: The name of the source column.
    - `sourceType`: The data type of the source column.
    - `target`: The name of the target column.
    - `targetType`: The data type of the target column.
   ```json
    [
        ("source", "sourceType", "target", "targetType"),
        ("source", "sourceType", "target", "targetType"),
        ("source", "sourceType", "target", "targetType"),
    ]
    ```
- transformation_ctx: A unique string that is used to identify the transformation.


```python
df = ApplyMapping.apply(
    frame=data_catalog,
    mappings=[
        ("country", "string", "country", "string"),
        ("dob", "string", "os", "timestamp"),
        ("age", "string", "age", "int"),
    ],
    transformation_ctx="df",
)
```
