from awsglue.job import Job
from awsglue.context import GlueContext
from pyspark.context import SparkContext

# Spark context setup
sc = SparkContext()

# Glue context setup
glue_context = GlueContext(sc)

# Initialize glue job
job = Job(glue_context)
job.init("sample")

# Create dynamicframe from


# commit job
job.commit()
