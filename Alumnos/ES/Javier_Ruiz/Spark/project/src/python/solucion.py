from pyspark.sql import SparkSession
import zipfile
import os
from pyspark.sql.functions import *
from pyspark.sql.window import Window

# ejecutar desde spark-master
# bash /spark/bin/spark-submit --master local --jars /opt/project/resources/postgresql-42.7.1.jar opt/project/src/python/solucion.py


spark = SparkSession.builder.getOrCreate()


# Descomprimo el archivo ZIP (el csv pesaba demasiado para Github)
with zipfile.ZipFile("/opt/project/resources/mercadona.zip", 'r') as zip_ref:
    zip_ref.extractall("/opt/project/resources/")

mercadonaDF = spark.read.options(header='True', inferSchema='True').csv("/opt/project/resources/mercadona.csv")


# Inserto en la BDD
mercadonaDF.write \
  .format("jdbc") \
  .option("url", "jdbc:postgresql://host.docker.internal:5432/midatabase") \
  .option("dbtable", "mercadona") \
  .option("user", "jarupau") \
  .option("password", "hola") \
  .option("driver", "org.postgresql.Driver") \
  .mode("append") \
  .save()

clientesdf = spark.read.options(header='True', inferSchema='True').csv("/opt/project/resources/mocked_data.csv")

clientesdf.write \
  .format("jdbc") \
  .option("url", "jdbc:postgresql://host.docker.internal:5432/midatabase") \
  .option("dbtable", "clientes") \
  .option("user", "jarupau") \
  .option("password", "hola") \
  .option("driver", "org.postgresql.Driver") \
  .mode("append") \
  .save()



### TRANSFORMACIONES

# Todas las compras de 1/4 de Sandía : FILTER

Sandiasdf = mercadonaDF.select("id", "name", "price", "reference_price", "reference_unit") \
           .filter(col("name") == "1/4 Sandía")

Sandiasdf.write \
  .format("jdbc") \
  .option("url", "jdbc:postgresql://host.docker.internal:5432/midatabase") \
  .option("dbtable", "sandias") \
  .option("user", "jarupau") \
  .option("password", "hola") \
  .option("driver", "org.postgresql.Driver") \
  .mode("append") \
  .save()


###
# Categoria de comida más consumida por género y conteo

# JOIN Pequeña muestra de clientes de mercadona mockeada

joined_df = mercadonaDF.join(clientesdf, mercadonaDF.id == clientesdf.id, "inner")

# GROUPBY por genero + conteo total 
genre_df = joined_df.groupBy("gender") \
  .agg(count("*").alias("conteo_total"))

# Categoria más consumida por género : WINDOW PARTITIONING
category_df = joined_df.groupBy("gender", "category") \
  .agg(count("*").alias("category_count"))

window_spec = Window.partitionBy("gender").orderBy(desc("category_count"))
category_df = category_df.withColumn("dense_rank", dense_rank().over(window_spec))

category_df = category_df.filter(col("dense_rank") == 1) \
  .select("gender", "category") \
  .withColumnRenamed("category", "most_consumed_category")


joined_df = genre_df.join(category_df, "gender", "inner") 

joined_df.write \
  .format("jdbc") \
  .option("url", "jdbc:postgresql://host.docker.internal:5432/midatabase") \
  .option("dbtable", "generos") \
  .option("user", "jarupau") \
  .option("password", "hola") \
  .option("driver", "org.postgresql.Driver") \
  .mode("append") \
  .save()



###
# 10 frutas más caras : vista SQL
mercadonaDF.createTempView("mercadona")
frutacaraDF = spark.sql("""select name, avg(reference_price) as max_reference_price, reference_unit
                       from mercadona
                       where category == 'fruta'
                       group by name, reference_unit
                       order by max_reference_price desc
                       limit 10
                       """)

frutacaraDF.write \
  .format("jdbc") \
  .option("url", "jdbc:postgresql://host.docker.internal:5432/midatabase") \
  .option("dbtable", "frutacara") \
  .option("user", "jarupau") \
  .option("password", "hola") \
  .option("driver", "org.postgresql.Driver") \
  .mode("append") \
  .save()


###
# 10 frutas más baratas

frutaDF = mercadonaDF.select("name", "reference_price", "reference_unit") \
                     .where(mercadonaDF.category == "fruta")

frutabarataDF = frutaDF.groupBy(col("name"), "reference_unit") \
                       .agg(avg("reference_price").alias("AVG_reference_price")) \
                       .orderBy(col("AVG_reference_price")) \
                       .limit(10) \

frutabarataDF = frutabarataDF.select("name", "AVG_reference_price", "reference_unit")

frutabarataDF.write \
  .format("jdbc") \
  .option("url", "jdbc:postgresql://host.docker.internal:5432/midatabase") \
  .option("dbtable", "frutabarata") \
  .option("user", "jarupau") \
  .option("password", "hola") \
  .option("driver", "org.postgresql.Driver") \
  .mode("append") \
  .save()

os.remove("/opt/project/resources/mercadona.csv")
spark.stop()

