
# Data Engineering Onboarding Starter

[![Data Engineering - Deploy to AWS Glue](https://github.com/wednesday-solutions/data-engg/actions/workflows/cd.yml/badge.svg)](https://github.com/wednesday-solutions/data-engg/actions/workflows/cd.yml) [![Data Engineering CI](https://github.com/wednesday-solutions/data-engg/actions/workflows/ci.yml/badge.svg)](https://github.com/wednesday-solutions/data-engg/actions/workflows/ci.yml)

## Prerequisites

1. [Python3 with PIP](https://www.python.org/downloads/)
2. [Install Java 8](https://www.oracle.com/in/java/technologies/downloads/#java8-mac)
3. [AWS CLI configured locally](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html)
4. [Docker](https://docs.docker.com/desktop/install/mac-install/) (Optional)

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
