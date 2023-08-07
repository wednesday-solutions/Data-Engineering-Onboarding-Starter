from awsglue.job import Job
from awsglue.context import GlueContext
from pyspark.context import SparkContext
import pyspark.sql.functions as f

# Spark context setup
sc = SparkContext()

# Glue context setup
glue_context = GlueContext(sc)

# Spark session setup
spark_session = glue_context.spark_session

# Initialize glue job
job = Job(glue_context)
job.init("sample")

df = spark_session.read.csv(
    "src/data/survey_results_public.csv", header=True, inferSchema=True
)

df = df.filter(f.col("Country").eqNullSafe("Australia"))
df = df.filter(f.col("OpSysPersonal use").eqNullSafe("macOS"))

df.select("Country", "OpSysPersonal use").show()

job.commit()
