from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F

spark = SparkSession.builder.appName("TwitterSink").getOrCreate()
    # read the tweet data from socket
lines_df = spark.readStream.format("socket").option("host", "twitter_socket").option("port", "5556").load()

sc=spark

hadoop_conf=sc._jsc.hadoopConfiguration()
hadoop_conf.set("fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem")
hadoop_conf.set("fs.s3a.endpoint","http://minio:9000")
hadoop_conf.set("fs.s3a.access.key","minio")
hadoop_conf.set("fs.s3a.secret.key","minio123")
hadoop_conf.set("fs.s3a.path.style.access","True")

lines = spark.readStream.format("socket").option("host", "twitter_socket").option("port", 5556).load()
socketDF = spark.readStream.format("socket").option("host", "twitter_socket").option("port", 5556).load()
words = lines.select(
   explode(
       split(lines.value, " ")
   ).alias("word")
)

wordCounts = words.groupBy("word").count()
query = socketDF \
    .writeStream \
    .outputMode("append").format("parquet")\
    .option("path", "s3a://tweets-words/")\
    .option("checkpointLocation", "./check2")\
    .trigger(processingTime='3 seconds').start()


./spark/bin/spark-submit --master local[*] ./dags/job.py

parDF2=spark.read.parquet("s3a://tweets/")
parDF2.show(truncate=False)



./spark/bin/pyspark --master spark://spark-master:7077
sc=spark

hadoop_conf=sc._jsc.hadoopConfiguration()
hadoop_conf.set("fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem")
hadoop_conf.set("fs.s3a.endpoint","http://minio:9000")
hadoop_conf.set("fs.s3a.access.key","minio")
hadoop_conf.set("fs.s3a.secret.key","minio123")
hadoop_conf.set("fs.s3a.path.style.access","True")
#tweetSchema = StructType().add("name", "string").add("id", "string").add("texto", "string")

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F
from pyspark.sql.functions import regexp_extract
from functools import partial


socketDF = (spark.readStream.format("socket")
            .option("host", "twitter_socket")
            .option("port", 5556)
            .load()
            )

tweet = socketDF.select(
   explode(
       split(socketDF.value, "t_end")
   ).alias("tweet"))


fields = partial(
    regexp_extract, str="tweet", pattern="^(.*)<@#\$>(.*)<@#\$>(.*)<@#\$>(.*)<@#\$>(.*)<@#\$>(.*)<@#\$>(.*)<@#\$>(.*)$"
)
parser_tw= tweet.select(
    fields(idx=1).alias("id"),
    fields(idx=2).alias("name"),
    fields(idx=3).alias("screen_name"),
    fields(idx=4).alias("text"),
    fields(idx=5).alias("followers_count"),
    fields(idx=6).alias("lang"),
    fields(idx=7).alias("created_at"),
    fields(idx=8).alias("timestamp_ms")
)

query = (tweet.writeStream
      .format("console")
      .outputMode("append")

         .trigger(processingTime='10 seconds')
      .start()
         )

query = (socketDF.writeStream

         .outputMode("append")
      .format("console")

         .trigger(processingTime='10 seconds')
      .start()
         )


query = socketDF \
    .writeStream \
    .outputMode("append").format("parquet")\
    .option("path", "s3a://tweets-words/")\
    .option("checkpointLocation", "./check3")\
    .trigger(processingTime='3 seconds').start()




query = (socketDF.writeStream
      .format("console")
      .outputMode("append")
        .trigger(processingTime='10 seconds')
    .option("checkpointLocation", "./check")
      .start()  )

query = (socketDF
    .writeStream
    .format("json")
    .option("path", "/tweets-raw/")
    .option("checkpointLocation", "./check")
    .trigger(processingTime='3 seconds').start()
         )



query.awaitTermination()
query = (socketDF.writeStream.queryName("all_tweets")
             .outputMode("append").format("parquet")
             .option("path", "s3a://tweets/")
             .option("checkpointLocation", "./check")
             .trigger(processingTime='10 seconds').start()
             )
query.awaitTermination()
# from textblob import TextBlob
word_count_query = (counts_df.writeStream
                    .format("console")
                    .outputMode("complete")
                    .option("checkpointLocation", "chk-point-dir")
                    .start())





def parse_lines(lines):
    pass


if __name__ == '__main__':
    spark = SparkSession.builder.appName("TwitterSink").getOrCreate()
    # read the tweet data from socket
    lines = spark.readStream.format("socket").option("host", "0.0.0.0").option("port", 5555).load()
    # Preprocess the data
    words = parse_lines(lines)
    words = words.repartition(1)
    query = (lines.writeStream.queryName("all_tweets")
             .outputMode("append").format("parquet")
             .option("path", "s3a://tweets/raw")
             .option("fs.s3a.endpoint", "http://minio:9000")
             .option("fs.s3a.access.key", "minio")
             .option("fs.s3a.secret.key", "minio123")
             .option("fs.s3a.path.style.access", "true")
             .option("fs.s3a.connection.ssl.enabled", "false")
             .option("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
             .option("checkpointLocation", "./check")
             .trigger(processingTime='10 seconds').start()
             )
    query.awaitTermination()
