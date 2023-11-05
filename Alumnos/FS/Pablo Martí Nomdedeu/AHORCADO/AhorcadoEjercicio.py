abecedario_mayusculas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
palabras = ["REMEDIO","PRONUNCIAR","MANEJAR","LEY","ELEFANTE"]


#for letras in abecedario_mayusculas:
# for palabra in palabras:
   #     longitud = len(palabra)
   #     print(f"La palabra '{palabra}' tiene {longitud} letras.")


#for palabra in palabras:
 #   for letra in abecedario_mayusculas:
        #contador = palabra.count(letra)
     #   if contador > 0:
     #       print(f'La letra "{letra}" aparece {contador} veces en la palabra "{palabra}"')
            
entradas = 0

#for palabra in palabras:
   # longitud = len(palabra)
   # for letra in abecedario_mayusculas:
    #    entradas += 1
    #    contador = palabra.count(letra)
     #   if contador > 0:
     #       print(f'La palabra {palabra} tiene {contador} vez/veces la letar {letra} y su longitud es {longitud}')
     #       print(entradas)
        
#print(entradas)

#entradas = 0

#for palabra in palabras:
#    longitud = len(palabra)
  #  for letra in abecedario_mayusculas:
  #      if letra in palabra:
  #          contador = palabra.count(letra)
  #          print(f'La palabra {palabra} tiene {contador} vez/veces la letra {letra} y su longitud es {longitud}')
 #           entradas += 1

#print("Cantidad total de entradas:", entradas)

entradas = 0
fallos = 0  

for palabra in palabras:
    longitud = len(palabra)
    for letra in abecedario_mayusculas:
        if letra in palabra:
            contador = palabra.count(letra)
            print(f'La palabra {palabra} tiene {contador} vez/veces la letra {letra} y su longitud es {longitud}')
            entradas += 1
        else:
            fallos += 1

print("Cantidad total de entradas:", entradas)
print("Cantidad total de fallos:", fallos)

            
        

           


        



 