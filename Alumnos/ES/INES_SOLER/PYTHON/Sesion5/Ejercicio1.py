'''
Lee el archivo CSV con Pandas de 'pokemon_data.csv' alojado en la carpeta de datos de este repositorio y realizar las siguientes operaciones
'''
import pandas as pd
pokemon_df = pd.read_csv("pokemon_data.csv",
                        dtype={
                            'Name': str,
                            'Type 1': str,
                            'Type 2': str,
                            'Speed': int,
                            'Generation': int
                        })

# IMPRIMIR TODOS LOS VALORES
print(f'''Los valores del dataframe son: 
{pokemon_df}''')

# IMPRIMIR LOS PRIMEROS 5
print(f'''Las 5 primeras observaciones del dataframe son: 
{pokemon_df.head(5)}''')

# IMPRIMIR LOS ÚLTIMOS 5
print(f'''Las 5 últimas observaciones del dataframe son: 
{pokemon_df.tail(5)}''')

# OBTENER NOMBRES DE LAS COLUMNAS
print(f'''Los nombres de las columnas son: 
{pokemon_df.columns}''')

# OBTENER TODOS LOS NOMBRES
print(f'''Los nombres de los pokemon son: 
{pokemon_df["Name"]}''')

# OBTENER TODOS LOS NOMBRES Y VELOCIDADES
print(f'''Los nombres y las velocidades del dataframe son: 
{pokemon_df[["Name","Speed"]]}''')

# LOS PRIMEROS 5 NOMBRES USANDO [::]
print(f'''Los 5 primeros nombres son: 
{pokemon_df["Name"][0:5]}''')

# OBTENER TODAS LAS FILAS
print(f'''Las filas del dataframe son:
{pokemon_df.iloc[0:, ]}''')

# OBTENER UN RANGO DE FILAS
print(f'''Las 5 primeras filas son:
{pokemon_df.iloc[0:5]} ''')

# OBTENER EL NOMBRE DE LA FILA 10
print(f'''El nombre de la décima fila es:
{pokemon_df.iloc[10,1]}''')

# ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA
for i, pokemon in pokemon_df.iterrows():
    print(i, pokemon['Name'])

# POKEMONS DE TIPO 1 == WATER
type_water = pokemon_df.loc[pokemon_df['Type 1'] == 'Water']
print(f'''Los pokemons de tipo agua son:
{type_water}''')

# ESTADÍSTICAS (usando Describe del DafaFrame)
print(f'''A continuación se muestran algunas estadísticas del dataframe:
{pokemon_df.describe()}''')

# ORDENACIÓN POR NOMBRE ASCENDENTE
print(f'''A continuación se muestran los nombres de los pokemons ordenados alfabéticamente de forma ascendente(A - Z):
{pokemon_df.sort_values("Name", ascending = True)}''')

# CREAR UNA COLUMNA EXTRA CALCULADA
        # La columna debe ser la suma de HP + ATAQUE + DEFENSA + VELOCIDAD
        # La columna debe llamarse TOTAL
pokemon_df["Total"] = pokemon_df['HP'] + pokemon_df['Attack'] + pokemon_df['Defense'] + pokemon_df['Speed']
print(f'''Comprobamos que la columna "Total" se ha añadido y sumado correctamente:
{pokemon_df.head(5)[['Name', 'HP', 'Attack', 'Defense', 'Speed', 'Total']]}''')

# ELIMINAR LA COLUMNA TOTAL
pokemon_df = pokemon_df.drop(columns =['Total'])
print(f'''Comprobamos que la columna se ha eliminado correctamente:
{pokemon_df.columns}''')

# FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"
type_grassandpoison = pokemon_df.loc[(pokemon_df['Type 1'] == 'Grass') & (pokemon_df['Type 2'] == 'Poison')]
print(f'''Los pokemon de tipo 'Grass' y 'Poison' son: 
{type_grassandpoison}''')

# FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON
type_fireorpoison = pokemon_df.loc[(pokemon_df['Type 1'] == 'Fire') | (pokemon_df['Type 2'] == 'Poison')]
print(f''' Los pokemons que son de tipo 'Fire' o de tipo 'Poison' son:
{type_fireorpoison}''')

# FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
type_grassandpoison_70 = pokemon_df.loc[(pokemon_df['Type 1'] == 'Grass') & (pokemon_df['Type 2'] == 'Poison') & (pokemon_df['HP'] >= 70)]
print(f''' Los pokemons que son de tipo 'Grass' y de tipo 'Poison' y que además tienen un HP mayor o igual que 70 son:
{type_grassandpoison_70}''')

# FILTRAR POKEMONS CON NOMBRE "MEGA"
name_mega = pokemon_df[pokemon_df['Name'].str.contains('mega', case = False)]
print(f'''Los pokemons que contienen 'Mega' en su nombre son:
{name_mega}''')

# FILTRAR POKEMONS SIN NOMBRE "MEGA"
name_notmega = pokemon_df[~pokemon_df['Name'].str.contains('mega', case = False)]
print(f'''Los pokemons que NO contienen 'Mega' en su nombre son:
{name_notmega}''')

# FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
name_pi = pokemon_df[pokemon_df['Name'].str.startswith('Pi')]
print(f'''Los pokemons que empiezan por 'Pi' son:
{name_pi} ''')

# RENOMBRADO DE COLUMNA "FIRE" a "FLAME"
pokemon_df['Type 1'] = pokemon_df['Type 1'].replace('Fire', 'Flame')
print(pokemon_df['Type 1'].value_counts())

# RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA
pokemon_df['Type 1'] = pokemon_df['Type 1'].replace('Flame', 'Fire')
print(pokemon_df['Type 1'].value_counts())

# CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
pokemon_df.loc[pokemon_df['Legendary'] == True, 'Type 1'] = 'Fire'
legendarios = pokemon_df.loc[pokemon_df['Legendary']== True]
print(legendarios)

# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA
selected_columns = pokemon_df[['Type 1', 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']]
grupos_tipos_media = selected_columns.groupby(['Type 1']).mean()
orden_defensa = grupos_tipos_media.sort_values(by = 'Defense', ascending = False)
print(f'''Las medias por tipo 1 de pokemon ordenadas de mayor a menor puntuación de defensa son:
{orden_defensa}''')

# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE
orden_ataque = grupos_tipos_media.sort_values(by = 'Attack', ascending = False)
print(f'''Las medias por tipo 1 de pokemon ordenadas de mayor a menor puntuación de ataque son: 
{orden_ataque}''')

# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP
orden_hp = grupos_tipos_media.sort_values(by = 'HP', ascending = False)
print(f'''Las medias por tipo 1 de pokemon ordenadas de mayor a menor puntuación de HP son: 
{orden_hp}''')

# (Agrupación - groupBy) ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
grupos_tipos_suma = selected_columns.groupby(['Type 1']).sum()
print(f'''Las sumas de cada columna agrupada por tipo 1 de pokemon son: 
{grupos_tipos_suma}''')

# (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1DE POKEMON
grupos_tipos_numero =selected_columns.groupby(['Type 1']).size()
print(f'''En cada grupo del tipo 1 hay el siguiente número de pokemons:
{grupos_tipos_numero}''')

# (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON
grupos_tipos_2 = pokemon_df.groupby(['Type 1', 'Type 2']).size()
print(f'''Por cada agrupación del tipo 1 y 2 hay los siguientes pokemons:
{grupos_tipos_2}''')

'''Nota: SI TENEMOS ARCHIVOS ENORMES (1TB) PODEMOS LEERLOS POR PARTES. 
Cada fila podría estar acumulando cerca de 20 bytes, por lo que podríamos estar trabajando con cantidades enormes
'''

# LEE EL ARCHIVO CVS SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE (chunksize=5)
# ITERA POR LOS CHUNKS Y MUÉSTRALOS POR CONSOLA
for chunk in pd.read_csv("pokemon_data.csv",
                        dtype={
                            'Name': str,
                            'Type 1': str,
                            'Type 2': str,
                            'Speed': int,
                            'Generation': int
                        },
                        chunksize = 5):
    print(chunk)