#creamos lista
lista = ['REMEDIO','PRONUNCIAR','MANEJAR','LEY','ELEFANTE']
alfabeto = ["A","B",'C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#hacemos las palabras por orden

n = 0
elemento = lista[n]

#pedimos que pruebe por una letra de la "a" a la "z"
intentos = 0

for palabra in lista:
    for letra in alfabeto:
        intentos = intentos + 1
        if letra in palabra:
            print ("letra encontrá")
        else:
            print ('letra no encontrá, chato')

print (intentos)
            

#empezamos a contar tiempo
import time
tiempo_inicio = time.time()

for i in range(10000000):
    pass

tiempo_fin = time.time()

tiempo_transcurrido = tiempo_fin - tiempo_inicio

print(f"El proceso tardó {tiempo_transcurrido} segundos.")

#contamos intento

#mostramos si está o no la letra

#bucle hasta completar la palabra

#mostramos la palabra

#mostramos tiempo

#mostramos intentos

#sumamos el total de tiempo y de intetos de todas las palabras

