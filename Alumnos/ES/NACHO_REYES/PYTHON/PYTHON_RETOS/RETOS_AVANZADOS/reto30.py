# RETO 30

import ast

colores ="['Rojo', 'Verde', 'Blanco']"
type(colores)
colores_list = ast.literal_eval(colores)
type(colores_list)

print(f'La cadena de texto {colores}, de tipo {type(colores)}, se ha convertido a {type(colores_list)}, con este resultado: {colores_list}')