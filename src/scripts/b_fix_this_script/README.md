## Task 1: Fix this broken script

This script is broken. It is supposed to read data from Glue Data Catalog, create a DynamicFrame and apply some mappings
on it. Then, convert it to a Spark DataFrame, apply some transformations on the data. And write it to S3 as a Parquet
file. However, it is not working. Your task is to fix it.

### Instructions

1. Make changes to the `main.py` file to fix the script.
2. Fix the script and verify that it is working by running it locally.
3. Once you are satisfied with the results, Push the changes to github and merge your changes to the `main` branch.
4. Once your changes are merged your script will be deployed to AWS Glue.
5. Verify that your script is working in AWS Glue.
