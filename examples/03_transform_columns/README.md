# Data Manipulation and Column Creation

This is a PySpark script that performs data manipulation and creates new columns based on specific conditions. PySpark is a powerful framework for distributed data processing, and this script uses it to work with a CSV file containing survey results.

## 1. Renaming and Type Conversion

In this part of the script, we read a CSV file containing survey data using PySpark's `SparkSession`. The CSV file must have a header, and the script will infer the schema to determine column data types.

We have a column named "YearsCodePro," which represents the number of years of professional coding experience for each respondent. To make our analysis easier, we rename this column to "Experience" using the `withColumnRenamed` function.

Next, we check the data type of the "Experience" column to ensure it is indeed of type string. We use the `select` method along with `dtypes` to print the data type information.

Then, we convert the "Experience" column to an integer type using the withColumn function and `cast` method. This will allow us to perform numerical calculations on this column in later parts of the script.

## 2. Creating a Boolean Column

In this part, we create a new column called "IsSenior." This column will indicate whether a person is a senior developer based on their professional coding experience.

We use the `withColumn` function again to create this new column. We compare the "Experience" column with the value 10 using the greater than (`>`) operator. If a person has more than 10 years of experience, the "IsSenior" column will be set to `True`, otherwise `False`.

Finally, we display the first 10 rows of the "Experience" and "IsSenior" columns to see the results.

## 3. Creating an Integer Column based on Mapping

In this part, we create a new column called "BlockchainInterest" based on the "Blockchain" column in the dataset. The "BlockchainInterest" column will represent the respondent's interest in blockchain technology on a scale of 0 to 4.

We use the `withColumn` function along with `when` and `otherwise` functions to map the values in the "Blockchain" column to corresponding integer values in the "BlockchainInterest" column. The mapping is as follows:

- Very unfavorable -> 0
- Unfavorable -> 1
- Indifferent -> 2
- Favorable -> 3
- Very favorable -> 4

The `when` function is used to specify the conditions for mapping, and the `otherwise` function is used to provide a default value (0 in this case) if none of the conditions match.

Finally, we display the first 10 rows of the "Blockchain" and "BlockchainInterest" columns to see the results of the mapping.

## How to run the Script?

```bash
$ sparksubmit examples/03_transform_columns/main.py

# or if you are using docker
$ spark-submit examples/03_transform_columns/main.py
```
