import re
from pyspark.sql import SparkSession

sc = SparkSession.builder.appName("wednesday").getOrCreate()

df = sc.read.parquet(
    "src/data/survey_results_public.parquet", header=True, inferSchema=True
)

df = df.toDF(*[re.sub(r"[^\w]", "_", c) for c in df.columns])

df.write.parquet("src/data/survey_results_public.parquet")
