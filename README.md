<img align="left" src="https://github.com/wednesday-solutions/Data-Engineering-Onboarding-Starter/assets/105773536/5acdca39-663f-45bb-8f0c-45677a1cedeb" width="480" height="540" />

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

## 

```bash
├── Makefile
├── Pipfile
├── README.md
├── automation
│   ├── deploy_glue_job.sh
├── examples
│   ├── 01_pyspark_dataframe
│   │   ├── README.md
│   │   └── main.py
│   ├── 02_applying_filters
│   │   ├── README.md
│   │   └── main.py
│   ├── 03_transform_columns
│   │   ├── README.md
│   │   └── main.py
│   ├── 04_remap_columns
│   │   ├── README.md
│   │   └── main.py
│   ├── 05_complex_transformations
│   │   ├── README.md
│   │   └── main.py
│   ├── 06_write_dataframe
│   │   ├── README.md
│   │   └── main.py
│   ├── 07_pyspark_in_glue_jobs
│   │   ├── README.md
│   │   └── main.py
│   ├── 08_glue_dynamic_frame
│   │   ├── README.md
│   │   └── main.py
│   ├── 09_apply_mappings
│   │   ├── README.md
│   │   └── main.py
│   └── 10_write_to_target
│       ├── README.md
│       └── main.py
└── src
    ├── data
    │   ├── customers.csv
    │   ├── survey_results_public.csv
    │   ├── survey_results_public.parquet
    ├── scripts
    │   ├── a_stackoverflow_survey
    │   │   └── main.py
    │   ├── b_fix_this_script
    │   │   ├── README.md
    │   │   └── main.py
    │   └── c_top_spotify_tracks
    │       └── README.md
    ├── tests
    └── utils

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
