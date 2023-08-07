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

data_catalog = glue_context.create_dynamic_frame_from_catalog(
    database="data-engg-starter",
    table_name="survey_results_public",
    transformation_ctx="data_catalog",
)

df = data_catalog.toDF()

df = df.filter(f.col("Country").eqNullSafe("Australia"))
df = df.filter(f.col("OpSysPersonal use").eqNullSafe("macOS"))

df.select("Country", "OpSysPersonal use").show()

job.commit()
