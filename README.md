<img align="left" src="https://github-production-user-asset-6210df.s3.amazonaws.com/105773536/269245524-c4fefc57-ebfe-4f1b-87ba-e4e4fc2bc745.png" width="480" height="540" />

<div>
  <a href="https://www.wednesday.is?utm_source=gthb&utm_medium=repo&utm_campaign=react-template" align="left" style="margin-left: 0;">
    <img src="https://uploads-ssl.webflow.com/5ee36ce1473112550f1e1739/5f5879492fafecdb3e5b0e75_wednesday_logo.svg">
  </a>
  <p>
    <h1 align="left">Data Engineering Onboarding Starter
    </h1>
  </p>

  <p>
An immersive data engineering journey awaits you in this comprehensive starter kit, featuring a curated list of resources, tools, and best practices to help you get started with data engineering. This starter kit is designed to help you learn the basics of data engineering and get you up and running with your first data engineering project.
  </p>

---

  <p>
    <h4>
      Expert teams of digital product strategists, developers, and designers.
    </h4>
  </p>

  <div>
    <a href="https://www.wednesday.is/contact-us?utm_source=gthb&utm_medium=repo&utm_campaign=serverless" target="_blank">
      <img src="https://uploads-ssl.webflow.com/5ee36ce1473112550f1e1739/5f6ae88b9005f9ed382fb2a5_button_get_in_touch.svg" width="121" height="34">
    </a>
    <a href="https://github.com/wednesday-solutions/" target="_blank">
      <img src="https://uploads-ssl.webflow.com/5ee36ce1473112550f1e1739/5f6ae88bb1958c3253756c39_button_follow_on_github.svg" width="168" height="34">
    </a>
  </div>

---

[![Data Engineering - Deploy to AWS Glue](https://github.com/wednesday-solutions/data-engg/actions/workflows/cd.yml/badge.svg)](https://github.com/wednesday-solutions/data-engg/actions/workflows/cd.yml) [![Data Engineering CI](https://github.com/wednesday-solutions/data-engg/actions/workflows/ci.yml/badge.svg)](https://github.com/wednesday-solutions/data-engg/actions/workflows/ci.yml)

---

## Prerequisites

1. [Python3 with PIP](https://www.python.org/downloads/)
2. [Install Java 8](https://www.oracle.com/in/java/technologies/downloads/#java8-mac)
3. [AWS CLI configured locally](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
4. [Docker](https://docs.docker.com/desktop/install/mac-install/) (Optional)

## Folder Structure

```
├── Makefile                                   | -> Allows you to run commands for setup, test, lint, etc
├── README.md                                  | -> Documentation for the project setup and usage
│
├── automation                                 | -> Contains scripts to automate deployment and testing
│   └── deploy_glue_job.sh                     | -> Script to deploy or update glue job
│
├── examples                                   | -> Contains example scripts to demonstrate pyspark features
│   ├── 01_pyspark_dataframe                   | -> Create a DataFrame by reading data from a source (CSV, Parquet Database, etc)
│   │   ├── README.md                             | -> Contains instructions to run the example
│   │   └── main.py                               | -> Example script to read csv file and write to parquet
│   ├── 02_applying_filters                    | -> Apply filters on a dataframe
│   │   ├── README.md                             | -> Contains instructions to run the example
│   │   └── main.py                               | -> Example script to apply filters on dataframe
│   ├── 03_transform_columns                   | -> Transform columns & manipulate data in a dataframe
│   │   ├── README.md                             | -> Contains instructions to run the example
│   │   └── main.py                               | -> Example script to transform columns
│   ├── 04_remap_columns                       | -> Normalise columns in a dataframe
│   │   ├── README.md                             | -> Contains instructions to run the example
│   │   └── main.py                               | -> Example script to normalise columns in a dataframe
│   ├── 05_complex_transformations             | -> Perform complex transformations on a dataframe
│   │   ├── README.md                             | -> Contains instructions to run the example
│   │   └── main.py                               | -> Example script to perform some complex transformations
│   ├── 06_write_dataframe                     | -> Write a dataframe to a target
│   │   ├── README.md                             | -> Contains instructions to run the example
│   │   └── main.py                               | -> Example script to write dataframe to parquet or RDBMS Database
│   ├── 07_pyspark_in_glue_jobs                | -> Examples of using PySpark in AWS Glue Jobs
│   │   ├── README.md                             | -> Contains instructions to run the example
│   │   └── main.py                               | -> Example script to run pyspark script in glue job
│   ├── 08_glue_dynamic_frame                  | -> Create a DynamicFrame by reading data from a data catalog
│   │   ├── README.md                             | -> Contains instructions to run the example
│   │   └── main.py                               | -> Example script to create a dynamic frame from a data catalog
│   ├── 09_apply_mappings                      | -> Apply mappings on a dynamic frame (change column names, data types, etc)
│   │   ├── README.md                             | -> Contains instructions to run the example
│   │   └── main.py                               | -> Example script to apply mappings on dynamic frame
│   └── 10_write_to_target                     | -> Write a dynamic frame to a target (CSV, Parquet, Database, etc)
│       ├── README.md                             | -> Contains instructions to run the example
│       └── main.py                               | -> Example script to write dynamic frame to parquet and store in S3
│
└── src                                        | -> Contains all the source code for the onboarding exercise
    ├── data                                   | -> Contains data files for the onboarding exercise
    │   ├── customers.csv                         | -> Customer Dataset CSV file
    │   ├── survey_results_public.csv             | -> Stackoverflow Survey CSV file
    │   └── survey_results_public.parquet         | -> Stackoverflow Survey Parquet file
    │
    └── scripts                                | -> Contains all the glue scripts exercise
        ├── a_stackoverflow_survey                | -> A sample glue script to read, apply mappings, transform data
        │   └── main.py
        ├── b_fix_this_script                     | -> A broken glue script for you to fix
        │   ├── README.md
        │   └── main.py
        └── c_top_spotify_tracks                  | -> A task for you to complete. Best of luck!
            └── README.md

```

---

## Setup

**Step 1:** Clone this repository and install required packages

```bash
$ make install
```

**Step 2:** Clone AWS Glue Python Lib

AWS Glue libraries are not available on via PIP. Hence, we need to install it manually.

```bash
# Clone the master branch for Glue 4.0
$ git clone https://github.com/awslabs/aws-glue-libs.git

$ export AWS_GLUE_HOME=$(pwd)/aws-glue-libs
```

**Step 3:** Install Apache Maven

```bash
$ curl https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-common/apache-maven-3.6.0-bin.tar.gz -o apache-maven-3.6.0-bin.tar.gz

$ tar -xvf apache-maven-3.6.0-bin.tar.gz

$ ln -s apache-maven-3.6.0-bin maven

$ export MAVEN_HOME=$(pwd)/maven
```

**Step 3:** Install Apache Spark

```bash
$ curl https://aws-glue-etl-artifacts.s3.amazonaws.com/glue-4.0/spark-3.3.0-amzn-1-bin-3.3.3-amzn-0.tgz -o spark-3.3.0-amzn-1-bin-3.3.3-amzn-0.tgz

$ tar -xvf spark-3.3.0-amzn-1-bin-3.3.3-amzn-0.tgz

$ ln -s spark-3.3.0-amzn-1-bin-3.3.3-amzn-0 spark

$ export SPARK_HOME=$(pwd)/spark
```

**Step 4:** Export Paths

```bash
$ export PATH=$PATH:$SPARK_HOME/bin:$MAVEN_HOME/bin:$AWS_GLUE_HOME/bin
```

verify installation by running

`mvn --version`

`pyspark --version`

**Step 5:** Download Glue ETL .jar files

```bash
$ cd $AWS_GLUE_HOME

$ mvn install dependency:copy-dependencies

$ cp $AWS_GLUE_HOME/jarsv1/AWSGlue*.jar $SPARK_HOME/jars/

$ cp $AWS_GLUE_HOME/jarsv1/aws*.jar $SPARK_HOME/jars/
```

**After this step you should be able to execute**
**`gluepyspark`, `gluepytest`, `gluesparksubmit`**
**from shell**

#### References:

- [Run Glue Jobs Locally | AWS Docs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-libraries.html)
- [Setup AWS glue locally with PySpark](https://medium.com/@divs.sheth/setup-aws-glue-locally-using-pycharm-ce-visual-studio-code-d948e5cf1b59)

#### Frequent Errors:

`tools.jar` error
solution: [YouTube](https://www.youtube.com/watch?v=W8gsavSbOcw&ab_channel=JustAnotherDangHowToChannel)

## Run Locally Using

```
$ gluesparksubmit src/scripts/main.py
```

---

## Run Tests

**To run all test suites run:**

```bash
$ make test
```

**To geneate html coverage report run:**

```bash
$ python3 -m coverage html
```
