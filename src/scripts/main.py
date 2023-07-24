"""
Getting started with PySpark
"""

from pyspark.sql.session import SparkSession

sc = SparkSession.builder.appName("wednesday").getOrCreate()

columns = ["name", "email", "role"]
data = [
    ("James", "james@gmail.com", "Developer"),
    ("John", "john@gmail.com", "Developer"),
]

df = sc.createDataFrame(data=data, schema=columns)

df.printSchema()
df.show()
