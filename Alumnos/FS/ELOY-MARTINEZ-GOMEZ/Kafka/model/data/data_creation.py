from functions import *
import time

start = time.time()
# ------------------------------

sql_create_table = "CREATE TABLE IF NOT EXISTS candle_prices (id INT AUTO_INCREMENT PRIMARY KEY, volume FLOAT, volume_weight FLOAT, open FLOAT, close FLOAT, high FLOAT, low FLOAT, time DATETIME, transaction FLOAT)"
execute_query('docker', sql_create_table)

# ------------------------------
end = time.time()
print(f"Tiempo de ejecución: {end - start} segundos.")