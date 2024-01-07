import sys

print ('Hola. Bienvenido al sistema de cálculo de inversiones.')

while True:
    eligio = input('¿Qué quieres hacer? [1] Calcular mi inversión [X] Salir : ')

    if eligio == "1":
        cantidad = float(input("¿Cuánto quieres invertir? "))
        interes = (float(input('¿Cuál es el interés anual? ')))/100
        tiempo= int(input('¿Cuántos años vas a mantener la inversión? '))
        ganancia = (cantidad) * (interes) * (tiempo)
        resultado = (cantidad) + (ganancia)
        print (f"En {tiempo} años habrás recibido {ganancia}€ de interés")
        print (f"En total tendrás {resultado}€ al finalizar" )
        break
    elif eligio.upper() == "X":
        print ("¡Nos vemos!")
        sys.exit()
    else:
        print ("Por favor escoja 1 o X")