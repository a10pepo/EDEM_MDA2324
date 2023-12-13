#leer archivo csv con pandas y realizar las siguientes operaciones:
#IMPRIMIR TODAS LAS VARIABLES: 
#primero instalamos pandas con pip intall pandas.
import pandas as pd
archivo_csv = 'C:/Users/marpo/OneDrive/Escritorio/EDEM/python/SESION 5/pokemon_data.csv'
data = pd.read_csv(archivo_csv) #leo el archivo CSV con pandas
print(data) #me imprime todos los valores.

#IMPRIMIR LOS PRIMEROS 5
print(data.head(5)) #el método head de pandas nos ayuda a contar.

#IMPRIMIR LOS ÚLTIMOS 5
print(data.tail(5)) #el método tail de pandas nos cuenta los últimos valores.

#OBTENER NOMBRES DE LAS COLUMNAS
nombre_columnas= data.columns #columns es un atributo del DataFrame que contiene el nombre de las columnas.
print(nombre_columnas)

#OBTENER TODOS LOS NOMBRES
nombre_columnas_enteras= data.columns.tolist() #convierte los nombres de las columnas en una lista de Python, 
# que puedes imprimir para ver todos los nombres de las columnas.
print(nombre_columnas_enteras)

#OBTENER TODOS LOS NOMBRES Y VELOCIDADES
columnas_nombres_velocidades = data[['Name','Speed']] #creas una condición específica para imprimir esos valores.
print(columnas_nombres_velocidades)

#LOS PRIMEROS 5 NOMBRES USANDO [::]
primeros_cinco_nombres = data['Name'][:5] # utilizamos la notación de slicing [::]
print(primeros_cinco_nombres)

#OBTENER TODAS LAS FILAS
todas_las_filas = data[:] #como no le indico número, me las imprime todas.
print(todas_las_filas)

#OBTENER UN RANGO DE FILAS
rango_de_filas = data.iloc[4:9] #el método iloc se utliza para acceder a las filas mediante números enteros.No me cogerá el 9
print(rango_de_filas)

#OBTENER EL NOMBRE DE LA FILA 10
nombre_fila_diez = data.iloc[10]
print(nombre_fila_diez)

#ITERAR POR TODOS Y MOSTRAR EL ÍNDICE Y NOMBRE DE CADA FILA
for indice, fila in data.iterrows(): #iterrows permite recorrer el DataFrame y proporciona el dato y el indice de cada fila en cada iteración.#POKEMONS DE TIPO 1 == WATER
    print(f"Índice: {indice}, Name: {fila['Name']}")

#POKEMONS DE TIPO 1 == WATER
water_pokemon = data[data['Type 1'] == 'Water']
print(water_pokemon)

#ESTADÍSTICAS (usando Describe del DafaFrame)
estadísticas= data.describe () #describe me devuelve estadisticas resumidas por columnas, incluyendo, recuento, media, desviación estándar, min, perecentiles y max.
print(estadísticas)

#ORDENACIÓN POR NOMBRE ASCENDENTE
datos_ordenados=data.sort_values(by='Name' , ascending=True)
print(datos_ordenados)

#CREAR UNA COLUMNA EXTRA CALCULADA
#La columna debe ser la suma de HP + ATAQUE + DEFENSA + VELOCIDAD
#La columna debe llamarse TOTAL

data['TOTAL']= data['HP']+ data['Attack']+ data['Defense']+ data['Speed'] #suma de columnas
print(data.head()) #meuestra las columnas sumadas

#ELIMINAR LA COLUMNA TOTAL
data_no_total=data.drop('TOTAL', axis=1)#uso el método drop con axis para indicar que me elimine una columna y no una fila.
print(data_no_total.head())

#FILTRAR POKEMONS DE TIPOS "GRASS" Y "POISON
grass_poison_pokemon = data[(data['Type 1'] == 'Grass') | (data['Type 2'] == 'Grass') |
                            (data['Type 1'] == 'Poison') | (data['Type 2'] == 'Poison')]
print(grass_poison_pokemon)

#FILTRAR POKEMONS DE TIPO "FIRE" Ó "POISON
fire_poison_pokemon = data[(data['Type 1'] == 'Fire') | (data['Type 2'] == 'Fire') |
                           (data['Type 1'] == 'Poison') | (data['Type 2'] == 'Poison')]
print(fire_poison_pokemon)

#FILTRAR POKEMONS DE TIPO "GRASS" Y "POISON" Y UN HP >= 70
grass_poison_hp_pokemon = data[((data['Type 1'] == 'Grass') | (data['Type 2'] == 'Grass') |
                                (data['Type 1'] == 'Poison') | (data['Type 2'] == 'Poison')) &
                               (data['HP'] >= 70)] #utliza el operador lógico & para combinar las condiciones de tipo POKEMON y HP
print(grass_poison_hp_pokemon)

#FILTRAR POKEMONS CON NOMBRE "MEGA"
mega_pokemon = data[data['Name'].str.contains('Mega')]#str.contains busca y selecciona las filas donde la columna Name contenga la palabra Mega.
print(mega_pokemon)

#FILTRAR POKEMONS SIN NOMBRE "MEGA"
non_mega_pokemon = data[~data['Name'].str.contains('Mega')] #utilizamos el método ~ para negar la condición de contains.
print(non_mega_pokemon)

#FILTRAR POKEMONS CUYOS NOMBRES COMIENCEN CON "PI"
pi_start_pokemon = data[data['Name'].str.startswith('PI')]
print(pi_start_pokemon)

#RENOMBRADO DE COLUMNA "FIRE" a "FLAME"
data.rename(columns={'Fire': 'Flame'}, inplace=True)# inplace True hace que el cambio se aplique al DataFrame original, no es necesario asignar el resultado a uuna nueva variable. 
print(data.head())

#RENOMBRAR DE NUEVO A "FIRE" LA COLUMNA "FLAME" RECIÉN CAMBIADA
print("Data original:")#verifico las primeras filas y me aseguro que la columna flame se ha cambiado.
print(data.head())

data.rename(columns={'FLAME': 'FIRE'}, inplace=True) #renombro la columna fire a flame

print("\nData con la columna 'FIRE' recién renombrada:") #verifico la columna recién nombrada.
print(data.head())

#CAMBIAR A TODOS LOS POKEMON LEGENDARIOS A TIPO "FIRE"
#Identifico y cambio a tipo FIRE

data.loc[data['Legendary'] == True, 'Type 1'] = 'FIRE'
data.loc[data['Legendary'] == True, 'Type 2'] = 'FIRE'

#Verifico el cambio.

legendarios_cambiados = data[data['Legendary'] == True] 
print("Tipos de los Pokémon legendarios después del cambio:")
print(legendarios_cambiados[['Name', 'Type 1', 'Type 2']])

#(Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR DEFENSA
#Se utiliza groupby() para agrupar los Pokémon por su tipo primario ('Type 1') y se calcula la media de la columna 'Defense' (defensa).
#Se utiliza reset_index() para reiniciar los índices y obtener un DataFrame más limpio.
#Se utiliza sort_values() para ordenar los resultados por la media de la defensa en orden descendente (de mayor a menor).

media_defensa_por_tipo = data.groupby('Type 1')['Defense'].mean().reset_index()
media_defensa_por_tipo = media_defensa_por_tipo.sort_values(by='Defense', ascending=False)

print("Estadísticas de media por tipo de Pokémon ordenadas por defensa:")
print(media_defensa_por_tipo)

#(Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR ATAQUE
media_ataque_por_tipo = data.groupby('Type 1')['Attack'].mean().reset_index()
media_ataque_por_tipo = media_ataque_por_tipo.sort_values(by='Attack', ascending=False)

print("Estadísticas de media por tipo de Pokémon ordenadas por ataque:")
print(media_ataque_por_tipo)

#(Agrupación - groupBy) ESTADÍSTICAS DE MEDIA POR TIPO DE POKEMON y ORDENADOS POR HP
media_hp_por_tipo = data.groupby('Type 1')['HP'].mean().reset_index()
media_hp_por_tipo = media_hp_por_tipo.sort_values(by='HP', ascending=False)

print("Estadísticas de media por tipo de Pokémon ordenadas por HP:")
print(media_hp_por_tipo)

#(Agrupación - groupBy) ESTADÍSTICAS DE SUMA POR TIPO DE POKEMON

#Se aplica sum() para calcular la suma de las columnas 'Attack', 'Defense' y 'HP' por tipo de Pokémon.
suma_por_tipo = data.groupby('Type 1')[['Attack', 'Defense', 'HP']].sum()

print("Estadísticas de suma por tipo de Pokémon:")
print(suma_por_tipo)

#(Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1DE POKEMON

num_por_tipo_1 = data['Type 1'].value_counts().reset_index() #utilizo value.counts para calcular el nº pokemos por tipo primario
num_por_tipo_1.columns = ['Tipo de Pokémon', 'Número de Pokémon']

print("Estadísticas del número de Pokémon por tipo 1:")
print(num_por_tipo_1)

#(Agrupación - groupBy) ESTADÍSTICAS DE NÚMERO DE POKEMONS POR TIPO 1 y 2 DE POKEMON

# Concatenar las columnas de tipo 1 y tipo 2 para obtener todos los tipos de cada Pokémon
tipos_combinados = pd.concat([data['Type 1'], data['Type 2']]).reset_index(drop=True) 

# Calcular el número de Pokémon por tipo 1 y tipo 2
num_por_tipo = tipos_combinados.value_counts().reset_index() #Se utiliza value_counts() sobre esta serie para contar el número de ocurrencias de cada tipo.
num_por_tipo.columns = ['Tipo de Pokémon', 'Número de Pokémon']

# Mostrar las estadísticas del número de Pokémon por tipo 1 y tipo 2
print("Estadísticas del número de Pokémon por tipo 1 y tipo 2:")
print(num_por_tipo)

#LEE EL ARCHIVO CVS SEPARÁNDOLO POR CHUNKS Y CON UN TAMAÑO DE (chunksize=5) e ITERA POR LOS CHUNKS Y MUÉSTRALOS POR CONSOLA

# Iterar sobre el archivo CSV en chunks de tamaño 5
for chunk in pd.read_csv(archivo_csv, chunksize=5): #aqui leo el archivo en bloques de 5 e itero
    # Procesar cada chunk (bloque) del archivo
    print("Nuevo chunk:")
    print(chunk)

