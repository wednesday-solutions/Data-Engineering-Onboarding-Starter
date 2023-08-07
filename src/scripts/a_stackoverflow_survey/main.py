from awsglue.context import GlueContext, DynamicFrame
from awsglue.job import Job
from awsglue.transforms import ApplyMapping
from pyspark.context import SparkContext
import pyspark.sql.functions as f

# Spark context setup
sc = SparkContext()

# Glue context setup
glueContext = GlueContext(sc)

# Start a job
job = Job(glueContext)
job.init("stackoverflow_survey")

# Read data from catalog and create a dynamic frame
data_catalog = glueContext.create_dynamic_frame.from_catalog(
    database="data-engg-starter",
    table_name="survey_results_public_csv",
    transformation_ctx="data_catalog",
)

# Apply mappings
raw_data: DynamicFrame = ApplyMapping.apply(
    frame=data_catalog,
    mappings=[
        ("remotework", "string", "remote_work", "string"),
        ("yearscode", "string", "coding_experience", "int"),
        ("country", "string", "country", "string"),
        ("age", "string", "age_group", "string"),
        ("opsysprofessional use", "string", "os", "string"),
        ("edlevel", "string", "education_level", "string"),
        ("Employment", "string", "employment_status", "string"),
        ("convertedcompyearly", "string", "yearly_compensation", "int"),
    ],
)

# Convert dynamic frame to PySpark dataframe
df = raw_data.toDF()

# PySpark script starts here
df = df.filter(f.col("country").eqNullSafe("India"))

job.commit()
