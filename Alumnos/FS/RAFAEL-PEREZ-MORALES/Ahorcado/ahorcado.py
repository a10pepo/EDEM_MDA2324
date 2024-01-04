import csv
import datetime
import sys

lista_palabras = []
comienzo_tiempo = None
contador = 0
palabra = ""
adivinado = False
contador_intentos = 0
abecedario = list("WKXÑJZFHQYVGBPMUTCLDINRSOAE")

with open('archivo.csv', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        for value in row:
            lista_palabras.append(str(row))

def empezar_tiempo():
    global comienzo_tiempo
    comienzo_tiempo = datetime.datetime.now()

def finalizar_tiempo():
    fin_tiempo = datetime.datetime.now()
    tiempo_utilizado = fin_tiempo - comienzo_tiempo
    minutos, segundos = divmod(tiempo_utilizado.seconds, 60)
    segundos, decimas = divmod(tiempo_utilizado.microseconds / 100000, 1)
    segundos, centesimas = divmod(segundos, 0.1)
    segundos, milisegundos = divmod(segundos, 0.01)
    return f"Tiempo transcurrido: {minutos} minutos, {segundos} segundos, {int(decimas*10)} décimas, {int(centesimas*100)} centésimas, {int(milisegundos*1000)} milisegundis"

def extraer_palabra(adivinado):
    global abecedario
    abecedario = list("WKXÑJZFHQYVGBPMUTCLDINRSOAE")
    if lista_palabras[-1] == lista_palabras[contador]:
        tiempo_utilizado = finalizar_tiempo()
        print(tiempo_utilizado)
        print("Numero de intentos " + str(contador_intentos))
        sys.exit()
    else:
        adivinado = False
        global palabra
        palabra = lista_palabras[contador]
    palabra = palabra.upper()
    return adivinado

def comprobar_palabra(letra, incognita, adivinado):
    for i,letra_p in enumerate(palabra):
        if letra == letra_p:
            incognita_lista[i] = letra
        incognita_lista_correcta = incognita_lista[2:-2]
        if "".join(incognita_lista_correcta) == palabra[2:-2]:
            adivinado = True
    return adivinado

def nueva_letra():
    letra = abecedario.pop()
    return letra

def crear_incognita(palabra_actual):
    incognita = "-" * (len(palabra_actual))
    global incognita_lista
    incognita_lista = list(incognita)
    return incognita


empezar_tiempo()
while contador<15 :
    adivinado = extraer_palabra(adivinado)
    contador = contador + 1
    incognita = crear_incognita(palabra)
    while not adivinado:
        letra_actual = nueva_letra()
        contador_intentos = contador_intentos + 1
        adivinado = comprobar_palabra(letra_actual, incognita, adivinado)