import pandas as pd

pokemon_data = pd.read_csv("C:/Users/User/Documents/GitHub/EDEM_MDA2324/Profesores/Python/Datos/pokemon_data.csv")

# IMPRIMIR TODOS LOS VALORES
print(pokemon_data)

# IMPRIMIR LOS PRIMEROS 5
print(pokemon_data.head())

# IMPRIMIR LOS ÚLTIMOS 5
print(pokemon_data.tail())

# OBTENER NOMBRES DE LAS COLUMNAS
print(pokemon_data.columns)

# OBTENER TODOS LOS NOMBRES
print(pokemon_data['Name'])

# OBTENER TODOS LOS NOMBRES Y VELOCIDADES
print(pokemon_data[['Name', 'Speed']])

# LOS PRIMEROS 5 NOMBRES USANDO [::]
print(pokemon_data['Name'][::5])

# OBTENER TODAS LAS FILAS
print(pokemon_data.iloc[:])

# OBTENER UN RANGO DE FILAS
print(pokemon_data.iloc[5:10])

# OBTENER EL NOMBRE DE LA FILA 10
print(pokemon_data.iloc[10]['Name'])

# ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA
for indice, fila in pokemon_data.iterrows():
    print("Indice:", indice, "Nombre:", fila['Name'])

# POKEMONS DE TIPO 1 == WATER
pokemon_agua = pokemon_data[pokemon_data['Type 1'] == 'Water']
print(pokemon_agua)

# ESTADÍSTICAS (usando Describe del DataFrame)
print(pokemon_data.describe())

# ORDENACIÓN POR NOMBRE ASCENDENTE
print(pokemon_data.sort_values(by='Name', ascending=True))

# CREAR UNA COLUMNA EXTRA CALCULADA
pokemon_data['TOTAL'] = pokemon_data['HP'] + pokemon_data['Attack'] + pokemon_data['Defense'] + pokemon_data['Speed']
print(pokemon_data)
# ELIMINAR LA COLUMNA TOTAL
pokemon_data = pokemon_data.drop('TOTAL', axis=1)

# FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"
pokemon_hierba_veneno = pokemon_data[(pokemon_data['Type 1'] == 'Grass') & (pokemon_data['Type 2'] == 'Poison')]
print(pokemon_hierba_veneno)

# FILTRAR POKEMONS DE TIPO "FIRE" O "POISON"
pokemon_fuego_or_veneno = pokemon_data[(pokemon_data['Type 1'] == 'Fire') | (pokemon_data['Type 2'] == 'Poison')]
print(pokemon_fuego_or_veneno)

# FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
pokemon_hierba_veneno_hp70 = pokemon_data[(pokemon_data['Type 1'] == 'Grass') & (pokemon_data['Type 2'] == 'Poison') & (pokemon_data['HP'] >= 70)]
print(pokemon_hierba_veneno_hp70)

# FILTRAR POKEMONS CON NOMBRE "MEGA"
pokemon_mega = pokemon_data[pokemon_data['Name'].str.contains('Mega')]
print(pokemon_mega)

# FILTRAR POKEMONS SIN NOMBRE "MEGA"
sin_mega_pokemon = pokemon_data[~pokemon_data['Name'].str.contains('Mega')]   #invierto la seleccion anterior
print(sin_mega_pokemon)

# FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
pokemon_pi = pokemon_data[pokemon_data['Name'].str.startswith('Pi')]
print(pokemon_pi)

# RENOMBRADO DE COLUMNA "FIRE" a "FLAME"
pokemon_data = pokemon_data.rename(columns={'Fire': 'Flame'})

# RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA
pokemon_data = pokemon_data.rename(columns={'Flame': 'Fire'})

# CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
pokemon_data.loc[pokemon_data['Legendary'] == True, 'Type 1'] = 'Fire'

# ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA
estadisticas_tipos_def = pokemon_data.groupby('Type 1').mean().sort_values(by='Defense', ascending=False)
print(estadisticas_tipos_def)

# ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE
estadisticas_tipos_at = pokemon_data.groupby('Type 1').mean().sort_values(by='Attack', ascending=False)
print(estadisticas_tipos_at)

# ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP
estadisticas_tipos_hp = pokemon_data.groupby('Type 1').mean().sort_values(by='HP', ascending=False)
print(estadisticas_tipos_hp)

# ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
suma_pokemons_tipo = pokemon_data.groupby('Type 1').sum()
print(suma_pokemons_tipo)

# ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 DE POKEMON
num_pokemon_tipo1 = pokemon_data.groupby('Type 1').size()
print(num_pokemon_tipo1)

# ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON
num_pokemon_tipo1_tipo2 = pokemon_data.groupby(['Type 1', 'Type 2']).size()
print(num_pokemon_tipo1_tipo2)

# LEO EL CSV EN CHUNKS
csv_archivo = "C:/Users/User/Documents/GitHub/EDEM_MDA2324/Profesores/Python/Datos/pokemon_data.csv"

chunks = pd.read_csv(csv_archivo, chunksize=5)

#ITERO SOBRE LOS CHUNKS
for i, chunk in enumerate(chunks):
    print(f"\n### CHUNK {i+1} ###")  
    print(chunk)

