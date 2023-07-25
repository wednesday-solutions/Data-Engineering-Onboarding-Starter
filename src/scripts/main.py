from pyspark.sql.session import SparkSession
import pyspark.sql.functions as F

sc = SparkSession.builder.appName("wednesday").getOrCreate()

df = sc.read.csv("src/data/survey_results_public.csv", header=True, inferSchema=True)

# Filter records where DevType contains "Developer, front-end"
df = df.filter(F.col("DevType").contacins("Developer, front-end"))

df.show()
