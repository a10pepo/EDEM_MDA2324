#A la aplicación de la calculadora de inversión, deberás añadirle una opción para salir de la consola
def calculadora():
    print ("Hola. Bienvenido al sistema de cálculo de inversión") 
    seleccion_usuario= input("¿quieres invertir?/n pulsa 1 para invertir pulsa 0 para salir")
    if seleccion_usuario == "1": 
        cantidad_inversion = float (input ("¿cuánto quieres invertir?"))
        interes_anual = float (input ("¿Cuál es el interés anual?\n"))
        duracion_inversion = int (input ("¿Cuántos años vas a mentener la inversión?\n"))
        interes_generado = float (cantidad_inversion * (interes_anual/100) * duracion_inversion)
        print (f" Has invertido {cantidad_inversion} con un interés anual de {interes_anual}% durante {duracion_inversion} y has generado {interes_generado} de interés")     
    elif seleccion_usuario == "0": 
        print ("Nos vemos pronto")
calculadora()
