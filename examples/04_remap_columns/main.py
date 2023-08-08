import re
from pyspark.sql import SparkSession

sc = SparkSession.builder.appName("wednesday").getOrCreate()

df = sc.read.parquet(
    "src/data/survey_results_public.parquet", header=True, inferSchema=True
)

# Remove non-word characters from column names and replace them with underscores
# (eg: "Hobby??" -> "Hobby__", "Open Source" -> "Open_Source")
df = df.toDF(*[re.sub(r"[^\w]", "_", c) for c in df.columns])

# Save the dataframe as parquet
df.write.parquet("src/data/updated_survey_results_public.parquet")
