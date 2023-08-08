## Writing PySpark Scripts in AWS Glue

Until now, we have been writing PySpark scripts which are executed on a local machine. In this section, we will learn how to write PySpark scripts that can be executed on AWS Glue. AWS Glue is a fully managed ETL service that makes it easy to move data between different data stores, clean and transform data. Glue allows you to write ETL scripts in Python and Scala and execute them on a fully managed Spark environment.

- Pricing: You pay only for the resources used while your jobs are running. Based on how many DPUs you allocate to your job, AWS Glue will allocate the number of Spark executors and cores accordingly. You can choose between 2 DPUs and 100 DPUs. The default is 10 DPUs. The cost per DPU-Hour is `$0.44`. So, always remember to check the number of DPUs allocated to your job before running it.

- AWS Glue is serverless. You do not need to provision any Spark clusters or manage any Spark infrastructure. AWS Glue will automatically provision and scale the resources required to run your job.

- AWS Glue is fully managed. You do not need to worry about patching, upgrading, or maintaining any servers. You just need to select the version of Glue you want to use and AWS will take care of the rest. The current version of Glue is `4.0`.


## Modules

There are a few modules that are imported from the `awsglue` package. Let's take a look at them:

**SparkContext:** The `SparkContext` is responsible for managing the Spark cluster and its resources.

**GlueContext:** The `GlueContext` class provides an interface for interacting with AWS Glue services using Spark.

**Job:** An instance of the `Job` class is created and initialized using the Glue context. This job will represent the data transformation task performed by the script.
You need to initialize the job using the `init()` method and pass in the name of the job. When the job is complete, you need to commit it using the `commit()` method.

You will write all the transformation logic and the PySpark realted code between the `init()` and `commit()` methods of the job. See the example below.


```python
# Glue context setup
glue_context = GlueContext(spark_context)

# Spark session setup
spark_session = glue_context.spark_session

# Initialize glue job
job = Job(glue_context)
job.init("job-name")

.... PySpark Script Goes Here ....

job.commit()
```
