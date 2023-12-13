# RETO 19

from datetime import datetime, timedelta

hoy = datetime.now()
pox_dia = hoy + timedelta(days = 1)
pox_dia2 = hoy + timedelta(days = 2)
pox_dia3 = hoy + timedelta(days = 3)

hoy = hoy.strftime('%Y-%m-%d')
pox_dia = pox_dia.strftime('%Y-%m-%d')
pox_dia2 = pox_dia2.strftime('%Y-%m-%d')
pox_dia3 = pox_dia3.strftime('%Y-%m-%d')

print(f'Hoy es {hoy}, mañana será {pox_dia}, pasado {pox_dia2} y al otro {pox_dia3}')