import pyodbc as pdb

psycopg2 = ""
host = ""
database = ""
user = ""
password = ""
port = ""

# Definición de la conexión
connection_target = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password,
        port=port
)

# Creación del cursor
cur_target = conn_target.cursor()
# Creación del cursor
cur_target.execute("""select * from "language" where language_id = 1;""")
