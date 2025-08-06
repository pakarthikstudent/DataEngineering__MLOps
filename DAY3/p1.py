from pyspark.sql import SparkSession

# Create or get a Spark session
spark = SparkSession.builder \
    .appName("BasicExample") \
    .getOrCreate()

# Check the Spark version
print("Spark version:", spark.version)