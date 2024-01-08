import pandas as pd
from KP_1_Definicion_clase import emergencia
from ZZ_Antiguo_Raw_Data import df_emergencias  


# Visualizar el DataFrame
print(df_emergencias.head(100))

# Por si quiero comprobarlo y guardarlo en un csv
df_emergencias.to_csv(r'G:\Mi unidad\EDEM\DATA PROJECT 1\FICHEROS FEED\DATA_SET_KAFKA_VOL1.csv', encoding='utf-8-sig', index=False)