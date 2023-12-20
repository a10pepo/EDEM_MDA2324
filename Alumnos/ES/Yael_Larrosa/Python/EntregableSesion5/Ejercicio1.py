import pandas as pd

pokemon_df = pd.read_csv("pokemon_data.csv",
                        dtype={
                            'Name': str,
                            'Type 1': str,
                            'Type 2': str,
                            'Speed': int,
                            'Generation': int
                        })

#imprimir todos los valores
print(pokemon_df)

#IMPRIMIR LOS PRIMEROS 5
print(f'Las cinco primeras filas del DataFrame son las siguientes: \n{pokemon_df.head(5)}')

#IMPRIMIR LOS ÚLTIMOS 5
print(f'Las cinco últimas filas del DataFrame son las siguientes: \n {pokemon_df.tail(5)}')

#obtener nombre de las columnas 
print(f'Los nombres de las columnas son: \n{pokemon_df.columns}')

#obtener todos los nombres 
nombres = pokemon_df['Name']
print(f'Los nombres de cada pokemon son: \n{nombres}')

#obtener todos los nombres y sus velocidades 
nombres_velocidades = pokemon_df[['Name','Speed']]
print(f'Los nombres y las velocidades de cada pokemon son: \n {nombres_velocidades}')

#LOS PRIMEROS 5 NOMBRES USANDO [::]
primeros_5 = pokemon_df['Name'][0:5]
print(f'Los cinco primeros nombres son : \n{primeros_5}')

#obtener todas las filas
print(f'Todas las filas del DataFrame son:\n {pokemon_df.iloc[0:, ]}')

#obtener un rango de filas 
print(f'el rango de filas de la 6-12 son las siguientes: \n{pokemon_df.iloc[6:12]}')

#obtener el nombre de la fila 10
print(f'El nombre del pokemon de la fila 10 es: {pokemon_df.iloc[10,1]}')#fila 10 ,columna 1

#iterar por todas y por cada una de las filas mostrar el indice y el nombre de cada
for i,pokemon in pokemon_df.iterrows():
    print(i,pokemon['Name'])

#filtrar los de tipo 1 == water 
condicion_tipo_agua= pokemon_df['Type 1']=='Water'
tipo_agua= pokemon_df[condicion_tipo_agua]
print(f'los pokemons tipo agua son: \n {tipo_agua}')

#ESTADÍSTICAS (usando Describe del DafaFrame)
print(f' Las estadisticas del DF son:\n {pokemon_df.describe()}')

#ORDENACIÓN POR NOMBRE ASCENDENTE
print(f'Los nombres ordenados de forma ascendente son: \n{pokemon_df.sort_values("Name", ascending=True)}')

#CREAR UNA COLUMNA EXTRA CALCULADA --> La columna debe ser la suma de HP + ATAQUE + DEFENSA + VELOCIDAD ;La columna debe llamarse TOTAL
pokemon_df['Total'] = pokemon_df['HP'] + pokemon_df['Attack'] + pokemon_df['Defense']+pokemon_df['Speed']
print(f'La columna total es la siguiente:\n {pokemon_df["Total"]}')

#eliminar columna total
pokemon_df=pokemon_df.drop(columns=['Total'])
print(pokemon_df.columns)

#FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"
pokemon_filtrado = pokemon_df[(pokemon_df['Type 1'] == 'Grass') & (pokemon_df['Type 2'] == 'Poison')]
print(f'Pokemons filtrados por tipo "grass" y "pison": \n {pokemon_filtrado}')

#FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON
pokemon_filtrado2 = pokemon_df[(pokemon_df['Type 1'] == 'Fire') | (pokemon_df['Type 2'] == 'Poison')]
print(f'Pokemons filtrados por tipo "fire" o "pison": \n {pokemon_filtrado2}')

#FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
pokemon_filtrado3 = pokemon_df[(pokemon_df['Type 1'] == 'Grass') & (pokemon_df['Type 2'] == 'Poison') & (pokemon_df['HP'] >= 70)]
print(f'Pokemons filtrados por tipo "grass" y "pison" y un hp >= 70: \n {pokemon_filtrado3}')

#FILTRAR POKEMONS CON NOMBRE "MEGA"
pokemon_filtrado4 = pokemon_df[(pokemon_df['Name'].str.contains('Mega')) ]
print(f' pokemons que contienen Mega en el nombre: \n{pokemon_filtrado4}')

#FILTRAR POKEMONS SIN NOMBRE "MEGA"
pokemon_filtrado5 = pokemon_df[~pokemon_df['Name'].str.contains('Mega')]
print(f' pokemons que no contienen Mega en el nombre: \n{pokemon_filtrado5}')

#FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
pokemon_filtrado6 = pokemon_df[(pokemon_df['Name'].str.startswith('Pi'))]
print(f' pokemons que su nombre comienzan por PI: \n{pokemon_filtrado6}')

#RENOMBRADO DE COLUMNA "FIRE" a "FLAME"
pokemon_df['Type 1'] = pokemon_df['Type 1'].replace('Fire' , 'Flame')
print(f'Se ha renombrado en la columna Type 1 los elementos Fire a Flame: \n{pokemon_df}')

#RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA
pokemon_df['Type 1'] = pokemon_df['Type 1'].replace('Flame' , 'Fire')
print(f'La columna type 1 vuelve al estado original: \n {pokemon_df}')

#CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
pokemon_df.loc[pokemon_df['Legendary'] == True, 'Type 1'] = 'Fire'
print(pokemon_df)

#(Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA
agrupados1 = pokemon_df[['Type 1', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].groupby(['Type 1']).mean()
ordenados1 = agrupados1.sort_values(by = 'Defense', ascending=False)
print(f'ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA: \n{ordenados1}')

#(Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE
agrupados2 = agrupados1.sort_values(by = 'Attack',ascending=False)
print(f'ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE: \n{agrupados2}')

#(Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP
agrupados3 = agrupados1.sort_values(by = 'HP',ascending=False)
print(f'ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP: \n{agrupados3}')

#(Agrupación - groupBy) ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
suma_por_grupo = pokemon_df[['Type 1', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']].groupby('Type 1').sum()
print(f'ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON: \n{suma_por_grupo}')

#(Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1DE POKEMON
numero_pokemons = pokemon_df.groupby('Type 1')['Name'].count()
print(f' En cada Type 1 de pokemons hay los siguientes números de pokemons: \n {numero_pokemons}')

#(Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON
numero_pokemons2 = pokemon_df.groupby(['Type 1','Type 2'])['Name'].count()
print(f' En cada Type 1 y type 2 de pokemons hay los siguientes números de pokemons: \n {numero_pokemons2}')

#LEE EL ARCHIVO CVS SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE (chunksize=5)
chunks = pd.read_csv('pokemon_data.csv', chunksize=5)

# ITERA POR LOS CHUNKS Y MUÉSTRALOS POR CONSOLA
for chunk in chunks:
    print("Nuevo Chunk:")
    print(chunk)