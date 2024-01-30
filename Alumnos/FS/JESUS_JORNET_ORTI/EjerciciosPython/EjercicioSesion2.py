print ('Hola. Bienvenido al sistema de cálculo de inversiones.')

cantidad = float(input("¿Cuánto quieres invertir? "))

interes = (float(input('¿Cuál es el interés anual? ')))/100

tiempo= int(input('¿Cuántos años vas a mantener la inversión? '))

ganancia = (cantidad) * (interes) * (tiempo)

resultado = (cantidad) + (ganancia)

print (f"En {tiempo} años habrás recibido {ganancia}€ de interés")
print (f"En total tendrás {resultado}€ al finalizar" )