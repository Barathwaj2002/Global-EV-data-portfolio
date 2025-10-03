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

#Tra
sales_by_year= df.filter(col('parameter'))





