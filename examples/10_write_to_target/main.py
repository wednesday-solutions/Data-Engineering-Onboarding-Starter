from awsglue.job import Job
from awsglue.context import GlueContext
from awsglue.transforms import ApplyMapping
from pyspark.context import SparkContext


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
    additional_options={},
)

raw_data = ApplyMapping.apply(
    frame=data_catalog,
    mappings=[
        ("country", "string", "Country", "string"),
        ("op_sys_personal_use", "string", "OpSysPersonal use", "string"),
    ],
    transformation_ctx="raw_data",
)

# Write to a S3 bucket
glue_context.write_dynamic_frame.from_options(
    frame=raw_data,
    connection_type="s3",
    connection_options={"path": "s3://sample-glue-wednesday/data/"},
    format="parquet",
)

job.commit()
