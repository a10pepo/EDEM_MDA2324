#LISTAS NECESARIAS
Lista_Revisar = ["REMEDIO","PRONUNCIAR","MANEJAR","LEY","ELEFANTE"]
Lista_solución = []
Lista_contar_iteraciones = []
Lista_caracteres = [ "E", "A", "O", "S", "R", "N", "I", "D", "L", "C", "T", "U", "M", "P", "B", "G", "V", "Y", "Q", "H", "F", "Z", "J", "Ñ", "X", "K", "W"]

#SCRIPT
def ahorcado ():
    iteracion = 0
    for palabra in Lista_Revisar:
        posiciones_cubiertas=0
        for letra in Lista_caracteres:
            iteracion += 1
            if  letra in palabra:
                Lista_solución.append(letra)
                posiciones_cubiertas += int(palabra.count(letra))
                if len(palabra) == posiciones_cubiertas:
                    break
            
    print (iteracion)
    print (Lista_solución)      

ahorcado()