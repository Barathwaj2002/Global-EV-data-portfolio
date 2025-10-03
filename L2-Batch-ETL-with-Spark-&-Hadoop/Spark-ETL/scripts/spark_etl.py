import findspark
findspark.init()
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,sum

#Initializing SparkSession as spark
spark = SparkSession.builder.appName('EV-Sales-ELT').master("local[*]").getOrCreate()

#Loading data using spark into a dataframe 'df'
df = spark.read.csv('E:/PROJECT/Global-EV-data-portfolio/L1-DATA-ANALYSIS-USING-PYTHON/data/processed/cleaned_data.csv', header=True, inferSchema=True)

#Check df
df.show()
df.printSchema()

#Tranformation of df

#Global EV sales by year
sales_by_year = df.filter(col('parameter') == 'EV sales').groupBy("year").agg(sum('value').alias('Total_Sales')).orderBy('year')

#Global EV sales by region
sales_by_region = df.filter(col('parameter') == 'EV sales').groupBy('region').agg(sum('value').alias('Region_Sales')).orderBy(col('Region_Sales').desc())

sales_by_region.show(10)
sales_by_year.show(10)

#BEV vs PHEV share in 2023
bev_phev_share = df.filter((col('parameter') == 'EV stock') & (col('year') == 2023)).groupBy('powertrain').agg(sum(col('value')).alias('total_stock')).orderBy(col('total_stock'))

bev_phev_share.show(10)

#Saving results
sales_by_year.write.mode("overwrite").parquet('E:/PROJECT/Global-EV-data-portfolio/L2-Batch-ETL-with-Spark-&-Hadoop/outputs/aggregated/sales_by_year')
sales_by_region.write.mode("overwrite").parquet('E:/PROJECT/Global-EV-data-portfolio/L2-Batch-ETL-with-Spark-&-Hadoop/outputs/aggregated/sales_by_region')
bev_phev_share.write.mode("overwrite").parquet('E:/PROJECT/Global-EV-data-portfolio/L2-Batch-ETL-with-Spark-&-Hadoop/outputs/aggregated/bev_phev_share')

print('ETL job completed. Output saved in path "outputs/aggregated/"')