import random
import time

palabras_diccionario = []
diccionario = []
abecedario_natural = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
abecedario_ordenado = ['e', 'a', 'o', 's', 'r', 'n', 'i', 'd', 'l', 'c', 't', 'u', 'm', 'p', 'b', 'g', 'v', 'y', 'q', 'h', 'f', 'z', 'j', 'ñ', 'x', 'k', 'w']

def cargar_palabras():
    fichero = "/Users/pedro.nieto/Documents/GitHub/EDEM_MDA2324/Profesores/Ahorcado/palabras.txt"
    #fichero = "palabras.txt"
    print(f"Cargando palabras del fichero {fichero}")
    with open(fichero, "r") as f:
        for linea in f:
            diccionario.append(linea.replace("\n", "").lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ü","u"))

def cargar_diccionario():
    fichero = "/Users/pedro.nieto/Documents/GitHub/EDEM_MDA2324/Profesores/Ahorcado/palabras_diccionario.txt"
    #fichero = "palabras_diccionario.txt"
    print(f"Cargando palabras del fichero {fichero}")
    with open(fichero, "r") as f:
        for linea in f:
            palabras_diccionario.append(linea.replace("\n", "").lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("ü","u"))

def proporciona_letra(conocidas, descartadas, longitud):

    print(len(palabras_diccionario))
    # Filtramos for tamaño
    palabras_validas_tamaño = []
    for palabra in palabras_diccionario:
        if len(palabra) == longitud:
            palabras_validas_tamaño.append(palabra)
    
    print(len(palabras_validas_tamaño))

    # Filtramos por letras conocidas
    palabras_validas_letras = []
    if len(conocidas) == 0:
        palabras_validas_letras = palabras_validas_tamaño
    else:
        for palabra in palabras_validas_tamaño:
            if all(letra in palabra for letra in conocidas):
                palabras_validas_letras.append(palabra)

    print(len(palabras_validas_letras))          

    # Filtramos por letras descartadas
    palabras_validas_noletras = []
    if len(descartadas) == 0:
        palabras_validas_noletras = palabras_validas_letras
    else:
        # 3. filtrar las palabras que no contengan las letras descartadas
        for palabra in palabras_validas_letras:
            if all(letra not in palabra for letra in descartadas):
                palabras_validas_noletras.append(palabra)

    print(len(palabras_validas_noletras))
    letras_dict = {}
    for palabra in palabras_validas_noletras:
        for letra in palabra:
            if letra not in conocidas:
                letras_dict[letra] = letras_dict.get(letra,0) + 1
    
    
    sorted_desserts = dict(sorted(letras_dict.items(), key=lambda item:item[1]))   
    return sorted_desserts.popitem()[0]

    



# Opcion 0: Definimos esta opción como la idea de resolver el listado de palabras de manera
# aleatoria
def opcion_0():
    print("___________________")
    print("Opcion 0")
    print("___________________")
    intentos = 0
    for palabra in diccionario:
        print(f"Palabra: {palabra}")
        aciertos = 0
        letras_usadas = []
        while aciertos < len(palabra):
            letra = random.choice(abecedario_natural)
            if letra not in letras_usadas:
                letras_usadas.append(letra)
                aciertos = aciertos + palabra.count(letra)
                intentos += 1
            
    return intentos

# Opcion 1: Resolvemos las palabras por orden de aparición en el diccionario
def opcion_1():
    print("___________________") # ANA
    print("Opcion 1")
    print("___________________")
    intentos = 0
    for palabra in diccionario:
        print(f"Palabra: {palabra}")
        aciertos = 0
        while aciertos < len(palabra):
            for letra in abecedario_natural:
                aciertos = aciertos + palabra.count(letra)
                intentos += 1
                if aciertos == len(palabra):
                    break
            
    return intentos

# Opcion 2: Resolvemos las palabras por orden de aparición en el diccionario
def opcion_2():
    print("___________________") # ANA
    print("Opcion 2")
    print("___________________")
    intentos = 0
    for palabra in diccionario:
        print(f"Palabra: {palabra}")
        aciertos = 0
        while aciertos < len(palabra):
            for letra in abecedario_ordenado:
                aciertos = aciertos + palabra.count(letra)
                intentos += 1
                if aciertos == len(palabra):
                    break
            
    return intentos

def opcion_3():
    print("___________________") # ANA
    print("Opcion 3")
    print("___________________")
    intentos = 0
    for palabra in diccionario:
        print(f"Palabra: {palabra}")
        letras_usadas = []
        letras_descartadas = []
        aciertos = 0
        while aciertos < len(palabra):
            letra = proporciona_letra(letras_usadas, letras_descartadas, len(palabra) )
            aciertos = aciertos + palabra.count(letra)
            intentos += 1
            if aciertos > 0:
                letras_usadas.append(letra)
            else:
                letras_descartadas.append(letra)
            
            if aciertos == len(palabra):
                break
            
    return intentos

def main():
    cargar_palabras()
    cargar_diccionario()
    if len(palabras_diccionario) == 0:
        print("ERROR002 - No se han cargado palabras")
    else:
        print(f"Se han cargado {len(palabras_diccionario)} palabras")
    if len(diccionario) == 0:
        print("ERROR001 - No se han cargado palabras")
    else:
        print(f"Se han cargado {len(diccionario)} palabras")
    
    t0 = time.time()
    intentos_op0=opcion_0()
    t1 = time.time()    
    

    t2 = time.time()
    intentos_op1=opcion_1()
    t3 = time.time()


    t4 = time.time()
    intentos_op2=opcion_2()
    t5 = time.time()

    # t6 = time.time()
    # intentos_op3=opcion_3()
    # t7 = time.time()

    print(f"Tiempo empleado opcion 1: {t1-t0} con intentos {intentos_op0}")
    print(f"Tiempo empleado opcion 2: {t3-t2} con intentos {intentos_op1}")
    print(f"Tiempo empleado opcion 3: {t5-t4} con intentos {intentos_op2}")
    #print(f"Tiempo empleado opcion 4: {t7-t6} con intentos {intentos_op3}")

    print("Arrancamos ahorcado")




if __name__ == '__main__':
    print("#### Ejecutando como programa principal ####")
    print("Aqui va el codigo principal")
    print("############################################")
    main()


