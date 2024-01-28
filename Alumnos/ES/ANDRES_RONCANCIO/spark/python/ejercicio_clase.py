from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

# Import sql functions
from pyspark.sql.functions import *

#Read CSV file
vgamesDF = spark.read.options(header='True', inferSchema='True').csv("/opt/project/resources/Video_Games_Sales_2018.csv")
vgames_spainDF = spark.read.option("header","True").option("delimiter", ";").csv("opt/project/resources/vgames_spain.csv")
#.show() 
vgamesDF.show(6);
vgames_spainDF.show(6);


# Sales critics by Genre and counting votes amount
sales_critics = vgamesDF.groupBy(col("Genre")).agg(
    count("*"),
    avg("Critic_Score").alias("calificacion_critica")
    ).orderBy(col("calificacion_critica").desc()).show() ;

#Global sales $ per Plataform(xbox, PS3, PS4, etc)
global_sales = vgamesDF.withColumn("Global_Sales", col("Global_Sales").cast("float"))
sum_global_sales = global_sales.groupBy("Platform").sum("Global_Sales")
sum_global_sales2= sum_global_sales.orderBy(col("sum(Global_Sales)").desc())
sum_global_sales2.show();

#Join with second DF:
vgamesDF.join(vgames_spainDF, "Platform").show();

#Join with everything from both:
joinCondition = vgamesDF.Platform == vgames_spainDF.Platform
vgames_inner = vgamesDF.join(vgames_spainDF, joinCondition, "inner").orderBy("Name")
vgames_inner.show(5);