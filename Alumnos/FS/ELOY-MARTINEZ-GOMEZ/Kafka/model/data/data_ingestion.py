import time
from functions import *

sql_insert = "INSERT INTO candle_prices (id, volume, volume_weight, open, close, high, low, time, transaction) VALUES "

initial_date = datetime.datetime(2023, 12, 22)
days = 5 # Tomamos los datos de los 5 días periodo 18-12-23 / 22-12-23.
for e in range(days):
    date = initial_date + datetime.timedelta(days=-e)
    candle_prices = get_candle_prices(date)
    sql_insert_price = sql_insert + candle_prices
    execute_query('pruebas', sql_insert_price)
    time.sleep(13)
    