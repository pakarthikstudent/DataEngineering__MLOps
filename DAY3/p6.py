import os
os.environ["PYSPARK_PYTHON"] = r"C:\Users\karth\AppData\Local\Programs\Python\Python310\python.exe"

# step 1: import pyspark modules and load Session class,explode and split functions

from pyspark.sql import SparkSession
from pyspark.sql.functions import explode,split

# step 2: create a spark session
spark = SparkSession.builder.appName("datastreaming").getOrCreate()
		
#step 3: read streaming data from a directory(project)
lines = spark.readStream.text("C:\\Users\\karth\\Karthik\\DATA\\SparkExamples\Demo")

#step 4: split lines into words
words = lines.select(explode(split(lines.value," ")).alias("word"))

#step 5: count the patterns(words)
wc = words.groupBy("word").count()

#step 6: start the streaming query and display results to console 
query = wc.writeStream.outputMode("complete").format("console").start()

#step 7: Running
#query.awaitTermination()



