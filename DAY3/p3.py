import os
os.environ["PYSPARK_PYTHON"] = r"C:\Users\karth\AppData\Local\Programs\Python\Python310\python.exe"

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField,StringType


# Create or get a Spark session
spark = SparkSession.builder \
    .appName("BasicExample") \
    .getOrCreate()

d1 = [(101,"Raj","sales",1000),(102,"Leo","prod",2000)]
df = spark.createDataFrame(d1)
df.show()

print(df.printSchema())


myschema=StructType([StructField('empid',StringType(),True),
	    StructField('empname',StringType(),True),
	    StructField('empdept',StringType(),True),
	    StructField('ecost',StringType(),True)])


df2 = spark.createDataFrame(data=d1,schema=myschema)
print(df2.printSchema())

