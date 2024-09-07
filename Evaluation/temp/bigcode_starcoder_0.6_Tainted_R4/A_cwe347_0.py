'''


from pyspark import SparkContext, SparkConf
import json
import re
import requests
import time

from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *

# create SparkContext
conf = SparkConf().setAppName("Yelp Reviews Analysis")
sc = SparkContext(conf=conf)

# create sqlContext
sqlContext = SparkSession(sc)

# get data from S3
# data = sqlContext.read.format("com.databricks.spark.csv").option("header", "true").option("inferSchema", "true").load("s3://yelp-data-shared-labs18/yelp_academic_dataset_review.csv")

# data = sqlContext.read.format("com.databricks.spark.csv").option("header", "true").option("inferSchema", "true").load("s3://yelp-data-shared-labs18/yelp_academic_dataset_business.csv")

# data = sqlContext.read.format("com.databricks.spark.csv").option