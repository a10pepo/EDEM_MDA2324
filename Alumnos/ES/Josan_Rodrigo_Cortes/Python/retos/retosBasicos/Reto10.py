""" Escribe un programa que guarde en una variable el siguiente contenido:"""

diccionario={'titulo':'El Más Allá','aka':'E tu vivrai nel terrore - Laldilà',
'director':'Lucio Fulci', 'año':1981, 'país':'Italia'} 

print(diccionario)
longitud_diccionario=len(diccionario)
nuevo_diccionario={}

for i in range(longitud_diccionario):

    diccionario_clave=input("Introduce la clave ")
    diccionario_valor=input("Intruduce el valor ")
    nuevo_diccionario[diccionario_clave]=diccionario_valor

print(nuevo_diccionario)

