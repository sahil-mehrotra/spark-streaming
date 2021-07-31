from pyspark import SparkContext

from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession

spark = SparkSession.builder.master("spark://spark:7077").getOrCreate()

df = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "broker:29092").option("startingOffsets",
                                                                                               "earliest").option(
    "subscribe", "policy").load()

query = df.selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)").writeStream.format('console').start()

query.awaitTermination
