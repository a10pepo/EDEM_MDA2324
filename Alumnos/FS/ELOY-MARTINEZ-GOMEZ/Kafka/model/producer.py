from kfunctions import kconsumer, kproducer
from data.functions import *

sql_select = "select * from candle_prices"
results = execute_query("pruebas", sql_select)
column_names = ['id', 'volume', 'volume_weight', 'open', 'close', 'high', 'low', 'time', 'transaction']
kproducer("pricelist", column_names, results)