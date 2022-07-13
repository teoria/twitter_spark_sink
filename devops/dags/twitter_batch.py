
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F
from pyspark.sql.functions import regexp_extract
from functools import partial

sc=spark 
hadoop_conf=sc._jsc.hadoopConfiguration()
hadoop_conf.set("fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem")
hadoop_conf.set("fs.s3a.endpoint","http://minio:9000")
hadoop_conf.set("fs.s3a.access.key","V42FCGRVMK24JJ8DHUYG")
hadoop_conf.set("fs.s3a.secret.key","bKhWxVF3kQoLY9kFmt91l+tDrEoZjqnWXzY9Eza")
hadoop_conf.set("fs.s3a.path.style.access","True")

parDF2=spark.read.parquet("s3a://tweets/")
parDF2.groupby('tag').count().show(truncate=False)