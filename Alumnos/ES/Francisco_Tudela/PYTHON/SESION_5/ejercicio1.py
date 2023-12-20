import pandas as pd

#Lee el archivo CSV con Pandas de 'pokemon_data.csv' alojado en la carpeta de datos de este repositorio y realizar las siguientes operaciones
dfpokemon = pd.read_csv('C:/Users/Pacotm/Documents/GitHub/EDEM_MDA2324/pokemon_modified.csv')
#- IMPRIMIR TODOS LOS VALORES
print(dfpokemon)
#- IMPRIMIR LOS PRIMEROS 5
print(dfpokemon.head(5))
#- IMPRIMIR LOS ÚLTIMOS 5
print(dfpokemon.tail(5))
#- OBTENER NOMBRES DE LAS COLUMNAS
print(dfpokemon.columns)
#- OBTENER TODOS LOS NOMBRES
print(dfpokemon['Name'])
#- OBTENER TODOS LOS NOMBRES Y VELOCIDADES
print(dfpokemon[['Name','Speed']])
#- LOS PRIMEROS 5 NOMBRES USANDO [::]
print(dfpokemon['Name'][:5])
#- OBTENER TODAS LAS FILAS
print(dfpokemon.iloc[:])
#- OBTENER UN RANGO DE FILAS
print(dfpokemon.iloc[2:10])
#- OBTENER EL NOMBRE DE LA FILA 10
print(dfpokemon.iloc[9]['Name'])
#- ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA
for index, row in dfpokemon.iterrows():
    print(f"Índice: {index}, Nombre: {row['Name']}")
#- POKEMONS DE TIPO 1 == WATER
water_pokemons = dfpokemon[dfpokemon['Type 1'] == 'Water']
print(water_pokemons)
#- ESTADÍSTICAS (usando Describe del DafaFrame)
print(dfpokemon.describe())
#- ORDENACIÓN POR NOMBRE ASCENDENTE
dfpokemon_sorted = dfpokemon.sort_values(by='Name', ascending=True)
print(dfpokemon_sorted)
#- CREAR UNA COLUMNA EXTRA CALCULADA
#    - La columna debe ser la suma de HP + ATAQUE + DEFENSA + VELOCIDAD
#    - La columna debe llamarse TOTAL
dfpokemon['TOTAL'] =dfpokemon['HP']+ dfpokemon['Attack'] + dfpokemon['Defense'] + dfpokemon['Speed']
print(dfpokemon)
#- ELIMINAR LA COLUMNA TOTAL
dfpokemon = dfpokemon.drop(columns=['TOTAL'])
print(dfpokemon)
#- FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"
grass_poison_poke = dfpokemon[(dfpokemon['Type 1'] == 'Grass') & (dfpokemon['Type 2'] == 'Poison')]
print(grass_poison_poke)
#- FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON
fire_or_poison_poke = dfpokemon[(dfpokemon['Type 1'] == 'Fire') | (dfpokemon['Type 2'] == 'Poison')]
print(fire_or_poison_poke)
#- FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
gra_pois_hp70_poke = dfpokemon[(dfpokemon['Type 1'] == 'Grass') & (dfpokemon['Type 2'] == 'Poison') & (dfpokemon['HP'] >= 70)]
print(gra_pois_hp70_poke)
#- FILTRAR POKEMONS CON NOMBRE "MEGA"
mega_pokemons = dfpokemon[dfpokemon['Name'].str.contains("Mega")]
print(mega_pokemons)
#- FILTRAR POKEMONS SIN NOMBRE "MEGA"
non_mega_pokemons = dfpokemon[~dfpokemon['Name'].str.contains("Mega")] # Virgulilla para la negación not
print(non_mega_pokemons)
#- FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
pi_pokes = dfpokemon[dfpokemon['Name'].str.startswith("Pi")]
print(pi_pokes)
#- RENOMBRADO DE COLUMNA "FIRE" a "FLAME"
dfpokemon = dfpokemon.rename(columns={'Fire': 'Flame'})
#- RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA
dfpokemon = dfpokemon.rename(columns={'Flame': 'Fire'})
#- CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
dfpokemon.loc[dfpokemon['Legendary'] == True, 'Type 1'] = 'Fire'
print(dfpokemon)
#- (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA
group_defense_stats = dfpokemon.groupby('Type 1')['Defense'].mean().sort_values(ascending=False)
print(group_defense_stats)
#- (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE
group_attack_stats = dfpokemon.groupby('Type 1')['Attack'].mean().sort_values(ascending=False)
print(group_attack_stats)
#- (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP
group_hp_stats = dfpokemon.groupby('Type 1')['HP'].mean().sort_values(ascending=False)
print(group_hp_stats)
#- (Agrupación - groupBy) ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
group_sum_stats = dfpokemon.groupby('Type 1')[['Attack', 'Defense', 'HP']].sum()
print(group_sum_stats)
#- (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1DE POKEMON
group_count_type1_stats = dfpokemon.groupby('Type 1').size()
print(group_count_type1_stats)
#- (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON
group_count_type1_type2_stats = dfpokemon.groupby(['Type 1', 'Type 2']).size()
print(group_count_type1_type2_stats)
'''Nota: 
SI TENEMOS ARCHIVOS ENORMES (1TB) PODEMOS LEERLOS POR PARTES 
Cada fila podría estar acumulando cerca de 20 bytes, por lo que podríamos estar trabajando con cantidades enormes
'''
#- LEE EL ARCHIVO CVS SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE  (chunksize=5)
#- ITERA POR LOS CHUNKS Y MUÉSTRALOS POR CONSOLA'''
for chunk in pd.read_csv('C:/Users/Pacotm/Documents/GitHub/EDEM_MDA2324/pokemon_modified.csv', chunksize=5): 
    print(chunk)