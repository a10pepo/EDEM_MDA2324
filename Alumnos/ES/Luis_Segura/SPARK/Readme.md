# ANÁLISIS DE DATOS DE FÓRMULA 1

Para este entregable de Spark, se ha llevado a cabo un análisis de varias estadísticas anuales con respecto del mundial de la Fórmula 1. Se ha hecho uso de 10 datasets públicos de Kaggle relacionados con la temática mencionada, que permiten analizar en detalle las últimas carreras, puntuaciones y demás variables de la competición. Para ello, se han llevado a cabo los siguientes pasos:

Después de haber definido los entornos necesarios en Google Colab, se han cargado y visualizado, en primer lugar, los 10 datasets usados, que también se encuentran en esta misma carpeta.

Algunas de las peticiones elegidas son:
   - Conocer los pilotos y escuderías para las cuales han trabajado y, mediante el uso de "joins", agregarles información adicional como la vuelta más rápida de cada uno.
   
   - Hallar el número total de carreras en las que ha participado cada piloto, ordenándolos por su nombre y anexionando todos los datos pertinentes mediante "group by".
   
   - Extraer las escuderías con mayor puntuación del campeonato. Para una mejor visualización de datos, se ha utilizado el "withColumnRenamed" para cambiar los nombres de las columnas, de su nombre como variable, a uno más visual y legible
   
   - Por último, se han pedido algunas de las vueltas rápidas, tanto por circuito, como por piloto y temporada, de la historia de la competición.