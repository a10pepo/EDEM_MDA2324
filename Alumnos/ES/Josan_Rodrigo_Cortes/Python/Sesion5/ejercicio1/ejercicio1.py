""" Ejercicio 1
Lee el archivo CSV con Pandas de 'pokemon_data.csv' alojado en la carpeta de datos de este repositorio y realizar las siguientes operaciones
"""
import pandas as pd
import numpy as np

pokemon = pd.read_csv("C:\\Users\\josan\\Documents\\GitHub\\EDEM_MDA2324\\Alumnos\\ES\\Josan_Rodrigo_Cortes\\CursodePython\\Sesion5\\ejercicio1\\pokemon_data.csv",sep=',')
pokemondf=pd.DataFrame(pokemon)


# IMPRIMIR TODOS LOS VALORES
print(pokemondf)

# IMPRIMIR LOS PRIMEROS 5
print(pokemondf.head())

# IMPRIMIR LOS ÚLTIMOS 5
print(pokemondf.tail())

# OBTENER NOMBRES DE LAS COLUMNAS nos devuelve el nombre de las columnas
print(pokemondf.columns) 

# OBTENER TODOS LOS NOMBRES, obtenemos todos los valores de la columna 'Name'
print(pokemondf['Name'])
print(pokemondf.Name)
print(list(pokemondf.Name))

# OBTENER TODOS LOS NOMBRES Y VELOCIDADES, tres formas, la ultima en formato lista
print(pokemondf.columns)
print(pokemondf[['Name','Speed']])

# LOS PRIMEROS 5 NOMBRES USANDO [::]
listaPokemons=list(pokemondf.Name)
print(listaPokemons[0:5])

# OBTENER TODAS LAS FILAS
print(pokemondf[:])

# OBTENER UN RANGO DE FILAS
print(pokemondf[20:290])

# OBTENER EL NOMBRE DE LA FILA 10
print(pokemondf.loc[10,'Name'])

# ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA
'No se como hacerlo'

# POKEMONS DE TIPO 1 == WATER 
'No consigo que funcione'
nuevopokemondf=pokemondf[pokemondf['Type'].str.contains('Water', case=False, na=False)]
print(nuevopokemondf)


# ORDENACIÓN POR NOMBRE ASCENDENTE
pokemondfOrdenado= pokemondf.sort_values(by='Name',)
print(pokemondfOrdenado)

# CREAR UNA COLUMNA EXTRA CALCULADA
# La columna debe ser la suma de HP + ATAQUE + DEFENSA + VELOCIDAD (no me funciona)
# La columna debe llamarse TOTAL
pokemondf['Total']=pokemondf['HP']+pokemondf['Attack']+ pokemondf['Defense']+pokemondf['Sp. Atk']+pokemondf['Sp. Def']+pokemondf['Speed']
print(pokemondf)

# # ELIMINAR LA COLUMNA TOTAL
pokemondf=pokemondf.drop(columns='Total')
print(pokemondf)

# FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON"
print(pokemondf.head)
pokemondfFiltrado = pokemondf[(pokemondf['Type 1'] == "Fire") | (pokemondf['Type 1'] == "Poison")]
print(pokemondfFiltrado)

# FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON
print(pokemondf.head)
pokemondfFiltrado = pokemondf[(pokemondf['Type 1'] == "Fire") or (pokemondf['Type 1'] == "Poison")]
print(pokemondfFiltrado)

# FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
print(pokemondf.head)
pokemondfFiltrado = pokemondf[(pokemondf['Type 1'] == "Fire") | (pokemondf['Type 1'] == "Poison") | (pokemondf['HP'] >= 70)]
print(pokemondfFiltrado)

# FILTRAR POKEMONS CON NOMBRE "MEGA"
pokemonFiltrado= pokemondf[pokemondf['Name'].str.contains('mega', case=False, na=False, regex=True)]
print(pokemonFiltrado)

# FILTRAR POKEMONS SIN NOMBRE "MEGA"
pokemonFiltrado= pokemondf[~pokemondf['Name'].str.contains('mega', case=False, na=False, regex=True)]
print(pokemonFiltrado)

# FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
pokemonFiltrado= pokemondf[pokemondf['Name'].str.contains('pi', case=False, na=False, regex=True)]
print(pokemonFiltrado)

# RENOMBRADO DE COLUMNA "FIRE" a "FLAME"
print(pokemondf.columns)
pokemondfRenombradoValores= pokemondf['Type 1'].replace({'Fire':'Flame'})
print(pokemondfRenombradoValores)

# RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA
print(pokemondf.columns)
pokemondfRenombradoValores= pokemondf['Type 1'].replace({'Flame':'Fire'})
print(pokemondfRenombradoValores)

# CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
condicion = pokemondf['Legendary'] ==True
pokemondf.loc[condicion, 'Type 1'] = 'Fire'
print(pokemondf)

# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA
'No consigo que funcione'
# print(pokemondf['Type 1'].unique())
# media_por_tipo_defensa = pokemondf.groupby('Type 1')['Grass' 'Fire' 'Water' 'Bug' 'Normal' 'Poison' 'Electric' 'Ground'
#  'Fairy' 'Fighting' 'Psychic' 'Rock' 'Ghost' 'Ice' 'Dragon' 'Dark' 'Steel'
#  'Flying'] #.mean().reset_index()  Reset_index para convertir a DataFrame
# # media_ordenada = media_por_tipo_defensa.sort_values(by='Defense', ascending=False)
# print(media_por_tipo_defensa)

# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE
'No consigo que funcione'

# (Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP
'No consigo que funcione'

# (Agrupación - groupBy) ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON
'No consigo que funcione'

# (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1DE POKEMON
'No consigo que funcione'

# (Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON
'No consigo que funcione'

# Nota: SI TENEMOS ARCHIVOS ENORMES (1TB) PODEMOS LEERLOS POR PARTES Cada fila podría estar acumulando cerca de 20 bytes, por lo que podríamos estar trabajando con cantidades enormes

# LEE EL ARCHIVO CVS SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE (chunksize=5)
archivo_csv = 'pokemon_data.csv'
tamaño_chunk = 5
for chunk in pd.read_csv(archivo_csv, chunksize=tamaño_chunk):
    print(chunk)

""" APUNTES CURSO PANDAS:
print(pokemondf.info()) información sobre el dataframe
print(pokemondf.describe())
# print(pokemondf.Attack.describe()) describe solamente la columna Attack
print(pokemondf.describe(include=np.number)) describe las columnas de tipo numerico
# print(pokemondf.describe(include=object)) describe las de tipo no numérico
print(pokemondf.head()) 5 primeros registros
print(pokemondf.tail()) 5 ultimos registros
print(pokemondf.shape) Nos devuelve el total de filas y columnas
pokemondf.Name=pokemondf['Speed'] No lo ejecuto pero cambiaría los valores de una columna por los de otra, conserva la original
pokemondf.drop(['NombredelaColumnaaelimninar'],axis=1,inplace=True) eliminariá una columna del data frame
# media print(pokemondf.mean)
Renombrar una columna:
pokemondf.rename(columns={'nombreactual':'nuevonombre'},inplace=True)
Con la funcion map, podemos transformar los valores de una columna en otra columna
print(pokemondf['Name'])
Obtener la media metodo .mean()
print(pokemondf.mean()) No me funciona
print(pokemondf['Speed'].mean()) así si
values_counts
print(pokemondf["Type 2"].value_counts())
"""