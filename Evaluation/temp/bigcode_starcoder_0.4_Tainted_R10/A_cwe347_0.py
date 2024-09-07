'''


import sys
import os
import json
import time
import logging
import argparse

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, udf, collect_list, explode, lit, struct, array, when
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, IntegerType, DoubleType, BooleanType
from pyspark.sql.window import Window

from pyspark.ml import Pipeline, PipelineModel
from pyspark.ml.feature import Tokenizer, StopWordsRemover, HashingTF, IDF, StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression, NaiveBayes, RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

from azureml.core.run import Run

# Create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler(sys.stdout))

# Define parameters
parser = argparse.ArgumentParser()
parser.add_argument('--data_path',