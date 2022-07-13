from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F
from pyspark.sql.functions import regexp_extract
from functools import partial
import uuid 

if __name__ == "__main__": 
  

    spark = SparkSession.builder.appName("TwitterSink").getOrCreate()
    sc=spark

    hadoop_conf=sc._jsc.hadoopConfiguration()
    hadoop_conf.set("fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem")
    hadoop_conf.set("fs.s3a.endpoint","http://minio:9000")
    hadoop_conf.set("fs.s3a.access.key","minio")
    hadoop_conf.set("fs.s3a.secret.key","minio123")
    hadoop_conf.set("fs.s3a.path.style.access","True")


    socketDF = (spark.readStream.format("socket")
            .option("host", "twitter_socket")
            .option("port", 5556)
            .load()
            )

    tweet = socketDF.select(
       explode(
           split(socketDF.value, "<EOT>")
       ).alias("tweet"))


    tweet = tweet.na.replace('', None)
    tweet = tweet.na.drop()
    fields = partial(
        regexp_extract, str="tweet", pattern="^(.*)<@#\$>(.*)<@#\$>(.*)<@#\$>(.*)<@#\$>(.*)<@#\$>(.*)<@#\$>(.*)<@#\$>(.*)<@#\$>(.*)$"
    )
    parser_tw= tweet.select(
    fields(idx=1).alias("id"),
    fields(idx=2).alias("name"),
    fields(idx=3).alias("screen_name"),
    fields(idx=4).alias("text"),
    fields(idx=5).alias("followers_count"),
    fields(idx=6).alias("lang"),
    fields(idx=7).alias("created_at"),
    fields(idx=8).alias("timestamp_ms"),
    fields(idx=9).alias("tag")
    ) 
    parser_tw = parser_tw.na.drop(subset=["tag"])
    parser_tw = parser_tw.where(parser_tw.tag.isNotNull())
    query = (parser_tw.writeStream
             .queryName("tweets")
             .outputMode("append")
             .format("parquet") 
             .option("path", "s3a://tweets/")
             .option("checkpointLocation", f"./check/{str(uuid.uuid4())}")
             .partitionBy('tag')
             .trigger(processingTime='10 seconds').start()
             )
    query.awaitTermination()