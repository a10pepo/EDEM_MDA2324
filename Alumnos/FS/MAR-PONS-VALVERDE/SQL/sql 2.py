import pyodbc as pdb
# Definición de la conexión, con los datos del primer dia. 
connection_target = psycopg2.connect(
 host=144.91.98.124:5432
 database=database, 
 user=user,
 password=password,
 port=port
 )

import pyodbc as pdb
# Creación del cursor
cur_target = conn_target.cursor()
# Creación del cursor
cur_target.execute("""SELECT * FROM PUBLIC.FILM""") 

