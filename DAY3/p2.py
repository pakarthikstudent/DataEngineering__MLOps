# Creating a DataFrame from Python Data
# -----------------------------------------

import os
os.environ["PYSPARK_PYTHON"] = r"C:\Users\karth\AppData\Local\Programs\Python\Python310\python.exe"

from pyspark.sql import SparkSession

# Create or get a Spark session
spark = SparkSession.builder \
    .appName("BasicExample") \
    .getOrCreate()

# Check the Spark version
print("Spark version:", spark.version)


# Sample data (list of tuples)
data = [("Alice", 25), ("Bob", 30), ("Cathy", 22),("leo",55),("paul",34)]

# Define column names
columns = ["Name", "Age"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Show data
df.show()