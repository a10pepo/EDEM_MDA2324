# Lee el archivo CSV con Pandas de 'pokemon_data.csv' alojado en la carpeta de datos de este repositorio y realizar las siguientes operaciones
import pandas as pd

df = pd.read_csv("pokemon_data.csv")

#IMPRIMIR TODOS LOS VALORES
print(df)

#IMPRIMIR LOS PRIMEROS 5
print(df.head())

#IMPRIMIR LOS ÚLTIMOS 5
print(df.tail())

#OBTENER NOMBRES DE LAS COLUMNAS
print(df.columns)   

#OBTENER TODOS LOS NOMBRES
print(df['Name'])

#OBTENER TODOS LOS NOMBRES Y VELOCIDADES
print(df[['Name', 'Speed']])  

#LOS PRIMEROS 5 NOMBRES USANDO [::]
print(df['Name'][:5])

#OBTENER TODAS LAS FILAS
print(df)

#OBTENER UN RANGO DE FILAS
print(df[5:11])

#OBTENER EL NOMBRE DE LA FILA 10
print(df.iloc[10]['Name'])

#ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA
for indice, fila in df.iterrows():
    print(f"Indice: {indice}, Nombre: {fila['Name']}")     

#POKEMONS DE TIPO 1 == WATER
print(df.loc[df['Type 1'] == 'Water'])

#ORDENACIÓN POR NOMBRE ASCENDENTE
print(df.sort_values(by= 'Name', ascending = True))

#CREAR UNA COLUMNA EXTRA CALCULADA
#La columna debe ser la suma de HP + ATAQUE + DEFENSA + VELOCIDAD
#La columna debe llamarse TOTAL
df['TOTAL'] = df['HP'] + df['Attack'] + df['Defense'] + df['Speed']
print(df)
df.to_csv('pokemon_data.csv', index=False)

#ELIMINAR LA COLUMNA TOTAL
df = df.drop(columns=['TOTAL'])
df.to_csv('pokemon_data.csv', index=False)

#FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"
print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')])

#FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON
print(df.loc[(df['Type 1'] == 'Fire') | (df['Type 2'] == 'Poison')])

#FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
print(df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] >= 70)])

#FILTRAR POKEMONS CON NOMBRE "MEGA"
print(df.loc[df['Name'] == 'MEGA'])

#FILTRAR POKEMONS SIN NOMBRE "MEGA"
print(df.loc[df['Name'] != 'MEGA'])

#FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
print(df.loc[df['Name'].str.startswith('Pi')])

#RENOMBRADO DE COLUMNA "Attack" a "Ataque"
df.rename(columns={'Attack': 'Ataque'}, inplace=True)
df.to_csv('pokemon_data.csv', index=False)

#RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA
df.rename(columns={'Ataque': 'Attack'}, inplace=True)
df.to_csv('pokemon_data.csv', index=False)

#CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
df.loc[df['Legendary'] == True, 'Type 1'] = 'Fire'
print(df)
df.to_csv('pokemon_data.csv', index=False)

# Imprime los tipos de datos de cada columna
print(df.dtypes)

#(Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA
avg_defense = df.groupby('Type 1')['Defense'].mean().sort_values(ascending=False).rename('AVG Defense')
print(avg_defense)

#(Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE
avg_attack = df.groupby('Type 1')['Attack'].mean().sort_values(ascending=False).rename('AVG Attack')
print(avg_attack)

#(Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP
avg_hp = df.groupby('Type 1')['HP'].mean().sort_values(ascending=False).rename('AVG HP')
print(avg_hp)

#(Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1DE POKEMON
num_pokemons = df.groupby('Type 1').size().sort_values(ascending=False).rename('NUM POKEMONS')
print(num_pokemons)

#LEE EL ARCHIVO CVS SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE (chunksize=5) E ITERA POR LOS CHUNKS Y MUÉSTRALOS POR CONSOLA
for chunk in pd.read_csv('pokemon_data.csv', chunksize = 5):
    print(chunk)

