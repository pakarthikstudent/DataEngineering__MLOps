import os
os.environ["PYSPARK_PYTHON"] = r"C:\Users\karth\AppData\Local\Programs\Python\Python310\python.exe"

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,StringType


# Create or get a Spark session
spark = SparkSession.builder \
    .appName("CacheExample") \
    .getOrCreate()


## With Caching
## ----------------

dataset = [(var,) for var in range(1,100000)]

df = spark.createDataFrame(dataset,["number"])

# define a transformation
even_filters = df.filter(df.number % 2 == 0) # filter even numbers

even_filters.cache() # Cache it

import time

start = time.time()

print("Avg 1 :",even_filters.agg({"number":"avg"}).collect()) # action

print("Time taken(1st time):",time.time() - start)

start = time.time()

print("Avg 2 :",even_filters.agg({"number":"avg"}).collect()) # action

print("Time taken(2nd time):",time.time() - start)

time.sleep(5)
print("Done!!!!")