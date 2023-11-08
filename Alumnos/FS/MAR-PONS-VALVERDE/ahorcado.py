lista_caracteres = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

palabras = ["REMEDIO", "PRONUNCIAR", "MANEJAR", "LEY", "ELEFANTE"]
intentos=0
for palabra in palabras:
    for letra in lista_caracteres:   
        if letra in palabra: 
           print("letra encontrada")
           intentos=intentos+1
        else: 
            print("letra no encontrada")
            intentos=intentos+1
print(intentos)



#contador de intentos

