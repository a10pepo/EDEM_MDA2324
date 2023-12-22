import pandas as pd

pokemon_csv_df = pd.read_csv('pokemon_data.csv',
                             dtype = {
                                 'Name': str,
                                 'Type 1': str,
                                 'Type 2': str,
                                 'Speed': int,
                                 'Generation': int,
                             })

print(pokemon_csv_df)
print(pokemon_csv_df.tail(5))
print(pokemon_csv_df.head(5))
print(pokemon_csv_df.columns)

# Opción 1
nombres_velocidades = pokemon_csv_df[{'Name', 'Speed'}]
print(nombres_velocidades)

# Opción 2
lista_columnas = ['Name', 'Speed']
nombres_velocidades = pokemon_csv_df[lista_columnas]
print(nombres_velocidades)

# Obtener los primeros 5 pokemons
primeros_5 = pokemon_csv_df['Name'][0:5]
print(primeros_5)

# Obtener la primera fila--> INDEX LOCATION y luego se pone la primera posición.
print(pokemon_csv_df.iloc(0))

# Obtener las n filas por ÍNDICE
print(pokemon_csv_df.iloc[0:3])

# OBTENER EL NOMBRE DE LA FILA 10
print(pokemon_csv_df.iloc[10, 1])

# ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y EL NOMBRE DE CADA

# for i, pokemon in pokemon_csv_df.iterrows():
#    print(f'{i} - {pokemon["Name"]})
#    print(i, pokemon['Name'])

# POKEMONS DE TIPO == WATER --> Usaremos .loc para LOCALIZAR por una Condición
condicion_tipo_1_agua = pokemon_csv_df['Type 1'] == 'water'
tipo_agua = pokemon_csv_df.loc[ condicion_tipo_1_agua ]

# ESTADÍSTICAS DEL DATAFRAME --> usaremos DESCRIBE()
print(pokemon_csv_df.describe())

# ORDENACIÓN --> Usaremos SORT_VALUES()
print(pokemon_csv_df.sort_values('Name', ascending = True))

# ORDENACIÓN MÁS COMPLEJA
print(pokemon_csv_df.sort_values(['Type 1', 'HP'], ascending = [True, False])['Name', 'Type 1', 'HP'])

# Columna EXTRA CALCULADA
pokemon_csv_df['Total'] = pokemon_csv_df['HP'] + pokemon_csv_df['Attack'] + pokemon_csv_df['Defense'] + pokemon_csv_df['Speed']
print(pokemon_csv_df['Total'])
print(pokemon_csv_df.sort_values('Total', ascending = False).head(5)(['Name', 'Total']))

# ELIMINAR la columna TOTAL
pokemon_csv_df = pokemon_csv_df.drop(columns = ['Total']) # Lo borramos
print(pokemon_csv_df.columns) # Aquí ya no lo tenemos

'''Guardar en un archivo CSV'''
#pokemon_csv_df.to_csv('pokemon_modified_csv', index = False)