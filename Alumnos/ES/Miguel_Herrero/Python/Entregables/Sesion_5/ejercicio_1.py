import pandas as pd

pokemon_csv_df = pd.read_csv('pokemon_data.csv', 
                             dtype={
                               "Name": str, 
                               "Type 1": str,
                               "Type 2": str,
                               "Speed": int,
                               "Generation": int,
                               "HP": int,
                               "Attack": int,
                               "Defense": int
                             },
                             index_col=0)

pokemon_csv_df['Defense'] = pd.to_numeric(pokemon_csv_df['Defense'], errors='coerce')


# Imprimir los Valores
print(pokemon_csv_df)

# Imprimir los 5 primeros
print(pokemon_csv_df.head(5))

# Imprimir los 5 últimos
print(pokemon_csv_df.tail(5))


# Obtener nombres de columnas
print(pokemon_csv_df.columns)

# Obtener todos los nombres
nombres = pokemon_csv_df['Name']
print(*nombres)


# Obtener todos los nombres y sus velocidades
# Opción 1
nombres_velocidades = pokemon_csv_df[['Name','Speed']]
print(nombres_velocidades)

# Opción 2
lista_columnas = ['Name','Speed']
nombres_velocidades = pokemon_csv_df[lista_columnas]
print(nombres_velocidades)

# Obtener los primeros 5 nombres
primeros_5 = pokemon_csv_df['Name'][0:5]
print(primeros_5)

# Obtener primera fila --> INDEX LOCATION y luego se le pone la posición
print(pokemon_csv_df.iloc[0])

# Obtener las r filas por ÍNDICE
print(pokemon_csv_df.iloc[0:3])

'''
OBTENER EL NOMBRE DE LA FILA 10
'''
print(pokemon_csv_df.iloc[10, 1])

'''
ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA
'''

for i, pokemon in pokemon_csv_df.iterrows():
  print(f'{i} - {pokemon["Name"]}')
  print(i, pokemon['Name'])


'''
POKEMONS DE TIPO 1 == WATER --> USAREMOS LOC() para LOCALIZAR por una Condición
'''
# Separarado por variables:
condicion_tipo_1_agua = pokemon_csv_df['Type 1'] == 'Water'
pokemons_de_tipo_agua = pokemon_csv_df.loc[ condicion_tipo_1_agua ]
print(pokemons_de_tipo_agua)

# sin variables todo junto
print(pokemon_csv_df.loc[ pokemon_csv_df['Type 1'] == 'Water' ])

'''
ESTADÍSTICAS del DATA FRAME --> Usaremos DESCRIBE()
'''
print(pokemon_csv_df.describe())

'''
ORDENACIÓN --> Usaremos SORT_VALUES()
'''
print(pokemon_csv_df.sort_values('Name', ascending=True))

'''
ORDENACIÓN MÁS COMPLEJA
'''
(pokemon_csv_df.sort_values(['Type 1', 'HP'], ascending=[True, False])[['Name', 'Type 1', 'HP']])


'''
CREAR UNA COLUMNA EXTRA CALCULADA
'''
pokemon_csv_df['Total'] = pokemon_csv_df['HP'] + pokemon_csv_df['Attack'] + pokemon_csv_df['Defense'] + pokemon_csv_df['Speed']

print(pokemon_csv_df['Total'])
print(pokemon_csv_df.sort_values('Total', ascending=False).head(5)[['Name', 'Total']])


'''
ELIMINAR LA COLUMNA TOTAL --> Usaremos el DROP()
'''
print(pokemon_csv_df.columns) 
pokemon_csv_df = pokemon_csv_df.drop(columns=['Total'])
print(pokemon_csv_df.columns) 


