## PySpark Data Filtering

This PySpark script demonstrates how to use PySpark to filter and analyze data from a CSV file. The script reads survey data from a CSV file, applies filters to extract specific information, and displays the results on the console.

## Script Overview

### The script performs the following steps:

**Step 1: Imports:** We import the required modules from PySpark, which allow us to create a SparkSession and access DataFrame functions.

**Step 2: Creating a DataFrame:** We start the Spark cluster by creating a SparkSession. The SparkSession is an entry point to interact with the Spark cluster and perform operations on data.

**Step 3: Importing Data from CSV Source:** We read the data from the CSV file using the read.csv() method. By specifying options like `header=True` and `inferSchema=True`, we inform PySpark that the CSV file contains a header row and that it should automatically infer the data types of the columns.

**Step 4: Applying Filters:** We apply two filters to the DataFrame to narrow down the data. First, we keep only the rows where the "Country" column is "Australia". Then, we further filter the DataFrame to retain only the rows where the "OpSysPersonal use" column is "macOS". These filters help us focus on specific data points of interest.

**Step 5: Print DataFrame on the Console:** Finally, we display the filtered DataFrame with the selected columns "Country" and "OpSysPersonal use" using the show() method. The results will be shown on the console.

## How to run the Script?

```bash
$ sparksubmit examples/02_applying_filters/main.py

# or if you are using docker
$ spark-submit examples/02_applying_filters/main.py
```
