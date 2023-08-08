## Apply Complex Transformations

In this example we will apply complex transformations on PySpark DataFrames.

## Joins

When working with multiple dataframes, we often need to combine them together. This is done using joins. There are
different types of joins, and we will look at some of them in this example.

The join function is available on the DataFrame API. It takes the following arguments:

- `dataframe`: The dataframe to join with
- `how`: The type of join to perform. The default is `inner`. Other options are `left`, `right`, and `outer`.

```python
joined_df = survey_df.join(customers_df, survey_df.ResponseId == customers_df.id, how="left")
```

## Regex Matching

Regular expressions are a powerful tool for matching patterns in text. There could be a scenario where we want to filter
out strings based on some Regular Expression pattern. We can do this using the `rlike` function.

```python
filtered_df = survey_df.filter(survey_df.Country.rlike("United States|India"))
```

## How to run the Script?

```bash
python examples/05_complex_transformations/main.py

# or if you are using docker run:
spark-submit examples/05_complex_transformations/main.py
```
